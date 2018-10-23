# -*- coding: utf8 -*-
# org.onap.vnfrqts/requirements
# ============LICENSE_START====================================================
# Copyright © 2018 AT&T Intellectual Property. All rights reserved.
#
# Unless otherwise specified, all software contained herein is licensed
# under the Apache License, Version 2.0 (the "License");
# you may not use this software except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Unless otherwise specified, all documentation contained herein is licensed
# under the Creative Commons License, Attribution 4.0 Intl. (the "License");
# you may not use this documentation except in compliance with the License.
# You may obtain a copy of the License at
#
#             https://creativecommons.org/licenses/by/4.0/
#
# Unless required by applicable law or agreed to in writing, documentation
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ============LICENSE_END============================================

"""
This script will consume the `invalid_metadata.csv` file produced by
`gen_requirement_changes.py`, then add/update any `:introduced:` or `:updated:`
attributes that may be missing from req directives.
"""
import csv
import os
import re
from collections import OrderedDict

import pytest

INPUT_FILE = "invalid_metadata.csv"


def load_invalid_reqs(fileobj):
    """Load the invalid requirements from the input file into a dict"""
    reader = csv.reader(fileobj)
    next(reader)  # skip header
    return {row[0]: (row[1].strip(), row[2].strip()) for row in reader}


def check(predicate, msg):
    """Raises a RuntimeError with the given msg if the predicate is false"""
    if not predicate:
        raise RuntimeError(msg)


class MetadataFixer:
    """Takes a dict of requirement ID to expected metadata value.  The
    NeedsVisitor will pass the requirement attributes as a a dict
    to `__call__`.  If the requirement is one that needs to be fixed, then
    it will add or update the attributes as needed and return it to the
    visitor, otherwise it will return the attributes unchanged."""

    def __init__(self, reqs_to_fix):
        """Initialize the fixer with a dict of requirement ID to tuple of
        (attr name, attr value)."""
        self.reqs_to_fix = reqs_to_fix

    def __call__(self, metadata):
        """If metadata is for a requirement that needs to be fixed, then
        adds or updates the attribute as needed and returns it, otherwise
        it returns metadata unchanged."""
        r_id = metadata[":id:"]
        if r_id in self.reqs_to_fix:
            attr, value = self.reqs_to_fix[r_id]
            metadata[attr] = value
        return metadata


class NeedsVisitor:
    """Walks a directory for reStructuredText files and detects needs
    directives as defined by sphinxcontrib-needs.  When a directive is
    found, then attributes are passed to a callback for processing if the
    callback returns a dict of attributes, then the revised dict is used
    instead of the attributes that were passed"""

    def __init__(self, func):
        self.directives = re.compile("\.\.\s+req::.*")
        self.func = func

    def process(self, root_dir):
        """Walks the `root_dir` looking for rst to files to parse"""
        for dir_path, sub_dirs, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.lower().endswith(".rst"):
                    self.handle_rst_file(os.path.join(dir_path, filename))

    @staticmethod
    def read(path):
        """Read file at `path` and return lines as list"""
        with open(path, "r") as f:
            print("path=", path)
            return list(f)

    @staticmethod
    def write(path, content):
        """Write a content to the given path"""
        with open(path, "w") as f:
            for line in content:
                f.write(line)

    def handle_rst_file(self, path):
        lines = (line for line in self.read(path))
        new_contents = []
        for line in lines:
            if self.is_needs_directive(line):
                metadata_lines = self.handle_need(lines)
                new_contents.append(line)
                new_contents.extend(metadata_lines)
            else:
                new_contents.append(line)
        self.write(path, new_contents)

    def is_needs_directive(self, line):
        """Returns True if the line denotes the start of a needs directive"""
        return bool(self.directives.match(line))

    def handle_need(self, lines):
        """Called when a needs directive is encountered.  The lines
        will be positioned on the line after the directive.  The attributes
        will be read, and then passed to the visitor for processing"""
        attributes = OrderedDict()
        indent = 4
        for line in lines:
            if line.strip().startswith(":"):
                indent = self.calc_indent(line)
                attr, value = self.parse_attribute(line)
                attributes[attr] = value
            else:
                if attributes:
                    new_attributes = self.func(attributes)
                    attr_lines = self.format_attributes(new_attributes, indent)
                    return attr_lines + [line]
                else:
                    return [line]

    @staticmethod
    def format_attributes(attrs, indent):
        """Converts a dict back to properly indented lines"""
        spaces = " " * indent
        return ["{}{} {}\n".format(spaces, k, v) for k, v in attrs.items()]

    @staticmethod
    def parse_attribute(line):
        return re.split("\s+", line.strip(), maxsplit=1)

    @staticmethod
    def calc_indent(line):
        return len(line) - len(line.lstrip())


if __name__ == '__main__':
    with open(INPUT_FILE, "r") as f:
        invalid_reqs = load_invalid_reqs(f)
    metadata_fixer = MetadataFixer(invalid_reqs)
    visitor = NeedsVisitor(metadata_fixer)
    visitor.process("docs")


# Tests
@pytest.fixture
def metadata_fixer():
    fixes = {
        "R-1234": (":introduced:", "casablanca"),
        "R-5678": (":updated:", "casablanca"),
    }
    return MetadataFixer(fixes)


def test_check_raises_when_false():
    with pytest.raises(RuntimeError):
        check(False, "error")


def test_check_does_not_raise_when_true():
    check(True, "error")


def test_load_invalid_req():
    contents = [
        "reqt_id, attribute, value",
        "R-1234,:introduced:, casablanca",
        "R-5678,:updated:, casablanca",
    ]
    result = load_invalid_reqs(contents)
    assert len(result) == 2
    assert result["R-1234"][0] == ":introduced:"
    assert result["R-1234"][1] == "casablanca"


def test_metadata_fixer_adds_when_missing(metadata_fixer):
    attributes = {":id:": "R-5678", ":introduced:": "beijing"}
    result = metadata_fixer(attributes)
    assert ":updated:" in result
    assert result[":updated:"] == "casablanca"


def test_metadata_fixer_updates_when_incorrect(metadata_fixer):
    attributes = {":id:": "R-5678", ":updated:": "beijing"}
    result = metadata_fixer(attributes)
    assert ":updated:" in result
    assert result[":updated:"] == "casablanca"
    assert ":introduced:" not in result


def test_needs_visitor_process(monkeypatch):
    v = NeedsVisitor(lambda x: x)
    paths = []

    def mock_handle_rst(path):
        paths.append(path)

    monkeypatch.setattr(v, "handle_rst_file", mock_handle_rst)
    v.process("docs")

    assert len(paths) > 1
    assert all(path.endswith(".rst") for path in paths)


def test_needs_visitor_is_needs_directive():
    v = NeedsVisitor(lambda x: x)
    assert v.is_needs_directive(".. req::")
    assert not v.is_needs_directive("test")
    assert not v.is_needs_directive(".. code::")


def test_needs_visitor_format_attributes():
    v = NeedsVisitor(lambda x: x)
    attr = OrderedDict()
    attr[":id:"] = "R-12345"
    attr[":updated:"] = "casablanca"
    lines = v.format_attributes(attr, 4)
    assert len(lines) == 2
    assert lines[0] == "    :id: R-12345"
    assert lines[1] == "    :updated: casablanca"


def test_needs_visitor_parse_attributes():
    v = NeedsVisitor(lambda x: x)
    assert v.parse_attribute("   :id: R-12345") == [":id:", "R-12345"]
    assert v.parse_attribute("   :key: one two") == [":key:", "one two"]


def test_needs_visitor_calc_indent():
    v = NeedsVisitor(lambda x: x)
    assert v.calc_indent("    test") == 4
    assert v.calc_indent("   test") == 3
    assert v.calc_indent("test") == 0


def test_needs_visitor_no_change(monkeypatch):
    v = NeedsVisitor(lambda x: x)
    lines = """.. req::
        :id: R-12345
        :updated: casablanca
        
        Here's my requirement"""
    monkeypatch.setattr(v, "read", lambda path: lines.split("\n"))
    result = []
    monkeypatch.setattr(v, "write", lambda _, content: result.extend(content))

    v.handle_rst_file("dummy_path")
    assert len(result) == 5
    assert "\n".join(result) == lines


def test_needs_visitor_with_fix(monkeypatch):
    fixer = MetadataFixer({"R-12345": (":introduced:", "casablanca")})
    v = NeedsVisitor(fixer)
    lines = """.. req::
        :id: R-12345

        Here's my requirement"""
    monkeypatch.setattr(v, "read", lambda path: lines.split("\n"))
    result = []
    monkeypatch.setattr(v, "write", lambda _, content: result.extend(content))

    v.handle_rst_file("dummy_path")
    assert len(result) == 5
    assert ":introduced: casablanca" in "\n".join(result)


def test_load_invalid_reqs():
    input_file = [
        "r_id,attr,value",
        "R-12345,:updated:,casablanca"
    ]
    result = load_invalid_reqs(input_file)
    assert "R-12345" in result
    assert result["R-12345"][0] == ":updated:"
    assert result["R-12345"][1] == "casablanca"
