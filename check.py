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
This script should be run before every commit to ensure proper
standards are being followed within the project.  The script
will also automatically fix certain issues when they are encountered, and
warn about other issues it cannot automatically resolve.

Warnings:
- Requirement missing required attributes
- Invalid values for attributes
- Invalid section header usage in any file
- :keyword: and requirement mismatch

Auto Updates:
- Assigning :id: on new requirements where an ID missing
- Adding :introduced: attribute on new requirements
- Adding/correcting :updated: attribute on changed requirements
"""

import os
import random
import re
import sys
from abc import ABC, abstractmethod
from collections import OrderedDict, deque
from pathlib import Path
from typing import Deque, List, Mapping, Callable, Set

import requests

THIS_DIR = Path(__file__).parent
CONF_PATH = THIS_DIR / "docs/conf.py"

NEEDS_JSON_URL = (
    "https://nexus.onap.org/service/local/repositories/raw/content"
    "/org.onap.vnfrqts.requirements/master/needs.json"
)

HEADING_LEVELS = ("-", "^", "~", "+", "*", '"')

SPACES = re.compile(r"\s+")
REQ_DIRECTIVE_PATTERN = re.compile(r"\.\.\s+req::.*")
ATTRIBUTE_PATTERN = re.compile(r"^\s+(:\w+:)\s+(.*)$")
VERSION_PATTERN = re.compile(r"version\s+=\s+'(.*?)'")

VALID_KEYWORDS = ("MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY", "MAY NOT")
VALID_VERSIONS = (
    "amsterdam",
    "beijing",
    "casablanca",
    "dublin",
    "el alto",
    "frankfurt",
    "guilin",
)
REQUIRED_ATTRIBUTES = (":keyword:", ":target:", ":id:")
VALID_TARGETS = (
    "VNF",
    "PNF",
    "VNF or PNF",
    "VNF DOCUMENTATION PACKAGE",
    "PNF DOCUMENTATION PACKAGE",
    "VNF or PNF DOCUMENTATION PACKAGE",
    "VNF PROVIDER",
    "PNF PROVIDER",
    "VNF or PNF PROVIDER",
    "VNF CSAR PACKAGE",
    "PNF CSAR PACKAGE",
    "VNF or PNF CSAR PACKAGE",
    "VNF HEAT PACKAGE",
)
VALID_VALIDATION_MODES = ("static", "none", "in_service")


def check(predicate: bool, msg: str):
    """
    Raises RuntimeError with given msg if predicate is False
    """
    if not predicate:
        raise RuntimeError(msg)


def get_version() -> str:
    """
    Returns the version value from conf.py
    """
    with open(CONF_PATH) as f:
        for line in f:
            m = VERSION_PATTERN.match(line)
            if m:
                version = m.groups()[0]
                if version not in VALID_VERSIONS:
                    print(
                        f"ERROR: {version} in conf.py is not defined in "
                        f"VALID_VERSIONS. Update the script to continue"
                    )
                    sys.exit(1)
                return version


VERSION = get_version()


def normalize(text: str):
    """
    Strips out formatting, line breaks, and repeated spaces to normalize
    the string for comparison.  This ensures minor formatting changes
    are not tagged as meaningful changes
    """
    s = text.lower()
    s = s.replace("\n", " ")
    s = re.sub(r'[`*\'"]', "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def warn(path: str, msg: str, req: "RequirementDirective" = None):
    """
    Log a warning
    """
    req_id = req.requirement_id or "UNKNOWN" if req else "UNKNOWN"
    print(f"WARNING: {path} | {req_id} | {msg}")


class RequirementRepository:
    """
    Pulls needs.json and provides various options to interact with the data.
    """

    def __init__(self, data=None):
        self.data = data or requests.get(NEEDS_JSON_URL).json()
        self.all_ids = {
            r["id"]
            for version in self.data["versions"].values()
            for r in version["needs"].values()
        }

    @property
    def current_requirements(self) -> Mapping:
        """
        Returns the requirements specified by current_version in needs.json.
        """
        version = self.data["current_version"]
        return self.data["versions"][version]["needs"]

    @property
    def unique_targets(self) -> Set[str]:
        return {r["target"] for r in self.current_requirements.values()}

    @property
    def unique_validation_modes(self) -> Set[str]:
        return {r["validation_mode"] for r in self.current_requirements.values()}

    def create_id(self) -> str:
        """
        Generates a requirements ID that has not been used in any version
        of the requirements.
        """
        while True:
            new_id = "R-{:0>5d}".format(random.randint(0, 99999))
            if new_id in self.all_ids:
                continue  # skip this one and generate another one
            self.all_ids.add(new_id)
            return new_id

    def is_new_requirement(self, req: "RequirementDirective") -> bool:
        return req.requirement_id not in self.current_requirements

    def has_changed(self, req: "RequirementDirective") -> bool:
        """
        Returns True if the requirement already exists and the contents has
        meaningfully changed. Small changes in spaces or formatting are not considered.
        """
        current_req = self.current_requirements.get(req.requirement_id)
        if not current_req:
            return False
        return normalize(current_req["description"]) == normalize("".join(req.content))


class RequirementDirective:
    """
    Data structure to hold a .. req:: directive
    """

    ATTRIBUTE_ORDER = (
        ":id:",
        ":target:",
        ":keyword:",
        ":introduced:",
        ":updated:",
        ":validation_mode:",
        ":impacts:",
    )

    def __init__(self, path: str):
        self.path = path
        self.attributes = OrderedDict()
        self.content = []
        self.indent = None

    @property
    def requirement_id(self) -> str:
        return self.attributes.get(":id:", "")

    @requirement_id.setter
    def requirement_id(self, r_id: str):
        self._update(":id:", r_id)

    @property
    def keyword(self) -> str:
        return self.attributes.get(":keyword:", "")

    @keyword.setter
    def keyword(self, k: str):
        self._update(":keyword:", k)

    @property
    def target(self) -> str:
        return self.attributes.get(":target:", "")

    @target.setter
    def target(self, value: str):
        self._update(":target", value)

    @property
    def introduced(self) -> str:
        return self.attributes.get(":introduced:", "")

    @introduced.setter
    def introduced(self, version: str):
        self._update(":introduced:", version)

    @property
    def updated(self) -> str:
        return self.attributes.get(":updated:", "")

    @updated.setter
    def updated(self, version: str):
        self._update(":updated:", version)

    @property
    def validation_mode(self) -> str:
        return self.attributes.get(":validation_mode:", "")

    @validation_mode.setter
    def validation_mode(self, value: str):
        self._update(":validation_mode:", value)

    def parse(self, lines: Deque[str]):
        """
        Parses a ..req:: directive and populates the data structre
        """
        parsing_attrs = True
        while lines:
            line = lines.popleft()
            match = ATTRIBUTE_PATTERN.match(line) if parsing_attrs else None
            if match:
                self.indent = self.indent or self.calc_indent(line)
                attr, value = match.groups()
                self.attributes[attr] = value
            else:
                parsing_attrs = False  # passed attributes, capture content
                if line.strip() and self.calc_indent(line) < self.indent:
                    # past end of the directive so we'll put this line back
                    lines.appendleft(line)
                    break
                else:
                    self.content.append(line)

    def format_attributes(self) -> List[str]:
        """
        Converts a dict back to properly indented lines using ATTRIBUTE_ORDER
        """
        spaces = " " * self.indent
        attr_lines = []
        for key in self.ATTRIBUTE_ORDER:
            value = self.attributes.get(key)
            if value:
                attr_lines.append(f"{spaces}{key} {value}\n")
        return attr_lines

    @staticmethod
    def calc_indent(line: str) -> int:
        """
        Number of leading spaces of the line
        """
        return len(line) - len(line.lstrip())

    def __str__(self):
        return "".join(self.format_attributes() + self.content)

    def _notify(self, field, value):
        req_id = self.requirement_id or "UNKNOWN"
        print(f"UPDATE: {self.path} | {req_id} | Setting {field} to {value}")

    def _update(self, attr, value):
        self.attributes[attr] = value
        self._notify(attr, value)


class RequirementVisitor:
    """
    Walks a directory for reStructuredText files and and passes contents to
    visitors when the content is encountered.

    Types of visitors supported:

    - Requirement:    Take the path and a RequirementDirective which may be modified
                      If modified, the file will be updated using the modified directive
    - Post Processor: Take the path and all lines for processing; returning a
                      potentially changed set of lines
    """

    def __init__(
        self,
        req_visitors: List[Callable[[str, RequirementDirective], None]],
        post_processors: List[Callable[[str, List[str]], List[str]]],
    ):
        self.req_visitors = req_visitors or []
        self.post_processors = post_processors or []

    def process(self, root_dir: Path):
        """
        Walks the `root_dir` looking for rst to files to parse
        """
        for dir_path, sub_dirs, filenames in os.walk(root_dir.as_posix()):
            for filename in filenames:
                if filename.lower().endswith(".rst"):
                    self.handle_rst_file(os.path.join(dir_path, filename))

    @staticmethod
    def read(path):
        """Read file at `path` and return lines as list"""
        with open(path, "r") as f:
            return list(f)

    @staticmethod
    def write(path, content):
        """Write a content to the given path"""
        with open(path, "w") as f:
            for line in content:
                f.write(line)

    def handle_rst_file(self, path):
        """
        Parse the RST file notifying the registered visitors
        """
        lines = deque(self.read(path))
        new_contents = []
        while lines:
            line = lines.popleft()
            if self.is_req_directive(line):
                req = RequirementDirective(path)
                req.parse(lines)
                for func in self.req_visitors:
                    func(path, req)
                # Put the lines back for processing by the line visitor
                lines.extendleft(reversed(req.format_attributes() + req.content))
            new_contents.append(line)
        for processor in self.post_processors:
            new_contents = processor(path, new_contents) or new_contents
        self.write(path, new_contents)

    @staticmethod
    def is_req_directive(line):
        """Returns True if the line denotes the start of a needs directive"""
        return bool(REQ_DIRECTIVE_PATTERN.match(line))


class AbstractRequirementVisitor(ABC):
    @abstractmethod
    def __call__(self, path: str, req: RequirementDirective):
        raise NotImplementedError()


class MetadataFixer(AbstractRequirementVisitor):
    """
    Updates metadata based on the status of the requirement and contents of
    the metadata
    """

    def __init__(self, repos: RequirementRepository):
        self.repos = repos

    def __call__(self, path: str, req: RequirementDirective):
        if not req.requirement_id:
            req.requirement_id = self.repos.create_id()
        if self.repos.is_new_requirement(req) and req.introduced != VERSION:
            req.introduced = VERSION
        if self.repos.has_changed(req) and req.updated != VERSION:
            req.updated = VERSION


class MetadataValidator(AbstractRequirementVisitor):
    def __init__(self, repos: RequirementRepository):
        self.repos = repos

    def __call__(self, path: str, req: RequirementDirective):
        for attr in REQUIRED_ATTRIBUTES:
            if attr not in req.attributes:
                warn(path, f"Missing required attribute {attr}", req)
        if req.keyword and req.keyword not in VALID_KEYWORDS:
            warn(path, f"Invalid :keyword: value ({req.keyword})", req)
        if repository.is_new_requirement(req) and req.introduced != VERSION:
            warn(path, f":introduced: is not {VERSION} on new requirement", req)
        if req.introduced and req.introduced not in VALID_VERSIONS:
            warn(path, f"Invalid :introduced: value ({req.introduced})", req)
        if req.updated and req.updated not in VALID_VERSIONS:
            warn(path, f"Invalid :updated: value ({req.updated})", req)
        if req.target and req.target not in VALID_TARGETS:
            warn(path, f"Invalid :target: value ({req.target})", req)
        if req.validation_mode and req.validation_mode not in VALID_VALIDATION_MODES:
            warn(path, f"Invalid :validation_mode: value ({req.validation_mode})", req)


def check_section_headers(path: str, lines: List[str]) -> List[str]:
    """
    Ensure hierarchy of section headers follows the expected progression as defined
    by `HEADING_LEVELS`, and that section heading marks match the length of the
    section title.
    """
    current_heading_level = 0
    for i, line in enumerate(lines):
        if any(line.startswith(char * 3) for char in HEADING_LEVELS):
            # heading level should go down, stay the same, or be next level
            expected = HEADING_LEVELS[0 : current_heading_level + 2]
            if line[0] not in expected:
                warn(
                    path,
                    f"Unexpected heading char ({line[0]}) on line {i+1}. "
                    f"Expected one of {' '.join(expected)}",
                )
            if len(line.strip()) != len(lines[i - 1].strip()):
                lines[i] = (line[0] * len(lines[i - 1].strip())) + "\n"
                print(
                    f"UPDATE: {path} | Matching section mark to title length "
                    f"on line {i+1}"
                )
            current_heading_level = HEADING_LEVELS.index(line[0])
    return lines


def check_keyword_text_alignment(path: str, req: RequirementDirective):
    if not req.keyword:
        return req
    keyword = f"**{req.keyword}**"
    if not any(keyword in line for line in req.content):
        warn(path, f"Keyword is {req.keyword}, but {keyword} not in requirement", req)


if __name__ == "__main__":
    print("Valid Versions")
    print("-----------------------")
    print("\n".join(VALID_VERSIONS))
    print()
    print("Valid Keywords")
    print("-----------------------")
    print("\n".join(VALID_KEYWORDS))
    print()
    print("Valid Targets")
    print("-----------------------")
    print("\n".join(VALID_TARGETS))
    print()
    print("Valid Validation Modes")
    print("-----------------------")
    print("\n".join(VALID_VALIDATION_MODES))
    print()
    print("Check-up Report")
    print("-" * 100)
    repository = RequirementRepository()
    visitor = RequirementVisitor(
        req_visitors=[
            MetadataFixer(repository),
            MetadataValidator(repository),
            check_keyword_text_alignment,
        ],
        post_processors=[check_section_headers],
    )
    visitor.process(THIS_DIR / "docs")
