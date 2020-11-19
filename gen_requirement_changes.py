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
This script will generate an summary of the requirements changes between
two version's of requirements by analyzing the needs.json file.  The template
can be customized by updating release-requirement-changes.rst.jinja2.
"""
import csv
from itertools import groupby, chain
import json
import os
import re
import sys
import argparse
from pathlib import Path

from operator import itemgetter

import jinja2

THIS_DIR = Path(__file__).parent
NEEDS_PATH = THIS_DIR / "docs/data/needs.json"
JINJA_TEMPLATE = "release-requirement-changes.rst.jinja2"


def check(predicate, msg):
    """
    Raises a ``RuntimeError`` if the given predicate is false.

    :param predicate: Predicate to evaluate
    :param msg: Error message to use if predicate is false
    """
    if not predicate:
        raise RuntimeError(msg)


class DifferenceFinder:
    """
    Class takes a needs.json data structure and finds the differences
    between two different versions of the requirements
    """

    def __init__(self, current_version, prior_version):
        """
        Determine the differences between the ``current_version`` and the
        ``prior_version`` of the given requirements.

        :param current_version: most recent version to compare against
        :return:
        """
        self.current_version = current_version
        self.prior_version = prior_version
        self._validate()

    def _validate(self):
        """
        Validates the inputs to the ``DifferenceFinder`` constructor.

        :raises RuntimeError: if the file is not structured properly or the
                              given versions can't be found.
        """
        for category, needs in (
            ("current needs", self.current_version),
            ("prior needs", self.prior_version),
        ):
            check(needs is not None, f"{category} cannot be None")
            check(isinstance(needs, dict), f"{category} needs must be a dict")
            check("versions" in needs, f"{category} needs file not properly formatted")

    @property
    def current_requirements(self):
        """Returns a dict of requirement ID to requirement metadata"""
        return self.get_current_version(self.current_version)

    @property
    def prior_requirements(self):
        """Returns a dict of requirement ID to requirement metadata"""
        return self.get_current_version(self.prior_version)

    @staticmethod
    def get_current_version(needs):
        """Returns a dict of requirement ID to requirement metadata"""
        version = needs["current_version"]
        return needs["versions"][version]["needs"]

    @property
    def new_requirements(self):
        """Requirements added since the prior version"""
        new_ids = self.current_ids.difference(self.prior_ids)
        return self.filter_needs(self.current_requirements, new_ids)

    @property
    def current_ids(self):
        """Returns a set of the requirement IDs for the current version"""
        return set(self.current_requirements.keys())

    @property
    def prior_ids(self):
        """Returns a set of the requirement IDs for the prior version"""
        return set(self.prior_requirements.keys())

    @property
    def removed_requirements(self):
        """Requirements that were removed since the prior version"""
        removed_ids = self.prior_ids.difference(self.current_ids)
        return self.filter_needs(self.prior_requirements, removed_ids)

    @property
    def changed_requirements(self):
        """"Requirements where the description changed since the last version"""
        common_ids = self.prior_ids.intersection(self.current_ids)
        result = {}
        for r_id in common_ids:
            current_text = self.current_requirements[r_id]["description"]
            prior_text = self.prior_requirements[r_id]["description"]
            if not self.is_equivalent(current_text, prior_text):
                sections = self.current_requirements[r_id]["sections"]
                result[r_id] = {
                    "id": r_id,
                    "description": current_text,
                    "sections": sections,
                    "introduced": self.current_requirements[r_id].get("introduced"),
                    "updated": self.current_requirements[r_id].get("updated"),
                }
        return result

    def is_equivalent(self, current_text, prior_text):
        """Returns true if there are meaningful differences between the
        text.  See normalize for more information"""
        return self.normalize(current_text) == self.normalize(prior_text)

    @staticmethod
    def normalize(text):
        """Strips out formatting, line breaks, and repeated spaces to normalize
         the string for comparison.  This ensures minor formatting changes
         are not tagged as meaningful changes"""
        s = text.lower()
        s = s.replace("\n", " ")
        s = re.sub(r'[`*\'"]', "", s)
        s = re.sub(r"\s+", " ", s)
        return s

    @staticmethod
    def filter_needs(needs, ids):
        """
        Return the requirements with the given ids

        :ids: sequence of requirement IDs
        :returns: dict of requirement ID to requirement data for only the
                 requirements in ``ids``
        """
        return {r_id: data for r_id, data in needs.items() if r_id in ids}


def load_requirements(path: Path):
    """Load the requirements from the needs.json file"""
    if not (path.exists()):
        print("needs.json not found.  Run tox -e docs to generate it.")
        sys.exit(1)
    with path.open("r") as req_file:
        return json.load(req_file)


def parse_args():
    """Parse the command-line arguments and return the arguments:

    args.prior_version
    """
    parser = argparse.ArgumentParser(
        description="Generate RST summarizing requirement changes between "
        "the current release and a prior releases needs.json file. The resulting RST "
        "file will be written to the docs/ directory"
    )
    parser.add_argument(
        "prior_version", help="Path to file containing prior needs.json file"
    )
    return parser.parse_args()


def tag(dicts, key, value):
    """Adds the key value to each dict in the sequence"""
    for d in dicts:
        d[key] = value
    return dicts


def gather_section_changes(diffs):
    """
    Return a list of dicts that represent the changes for a given section path.
    [
        {
         "section_path": path,
         "added: [req, ...],
         "updated: [req, ...],
         "removed: [req, ...],
        },
        ...
    ]
    :param diffs: instance of DifferenceFinder
    :return: list of section changes
    """
    # Add "change" and "section_path" keys to all requirements
    reqs = list(
        chain(
            tag(diffs.new_requirements.values(), "change", "added"),
            tag(diffs.changed_requirements.values(), "change", "updated"),
            tag(diffs.removed_requirements.values(), "change", "removed"),
        )
    )
    for req in reqs:
        req["section_path"] = " > ".join(reversed(req["sections"]))

    # Build list of changes by section
    reqs = sorted(reqs, key=itemgetter("section_path"))
    all_changes = []
    for section, section_reqs in groupby(reqs, key=itemgetter("section_path")):
        change = itemgetter("change")
        section_reqs = sorted(section_reqs, key=change)
        section_changes = {"section_path": section}
        for change, change_reqs in groupby(section_reqs, key=change):
            section_changes[change] = list(change_reqs)
        if any(k in section_changes for k in ("added", "updated", "removed")):
            all_changes.append(section_changes)
    return all_changes


def render_to_file(template_path, output_path, **context):
    """Read the template and render it ot the output_path using the given
    context variables"""
    with open(template_path, "r") as infile:
        t = jinja2.Template(infile.read())
    result = t.render(**context)
    with open(output_path, "w") as outfile:
        outfile.write(result)
    print()
    print("Writing requirement changes to " + output_path)
    print(
        "Please be sure to update the docs/release-notes.rst document "
        "with a link to this document"
    )


def print_invalid_metadata_report(difference_finder):
    """
    Write a report to the console for any instances where differences
    are detected, but the appropriate :introduced: or :updated: metadata
    is not applied to the requirement.
    """
    print("Validating Metadata...")
    print()
    print("Requirements Added, but Missing :introduced: Attribute")
    print("----------------------------------------------------")
    errors = [["reqt_id", "attribute", "value"]]
    current_version = difference_finder.current_version["current_version"]
    for req in difference_finder.new_requirements.values():
        if "introduced" not in req or req["introduced"] != current_version:
            errors.append([req["id"], ":introduced:", current_version])
            print(req["id"])
    print()
    print("Requirements Changed, but Missing :updated: Attribute")
    print("-----------------------------------------------------")
    for req in difference_finder.changed_requirements.values():
        if "updated" not in req or req["updated"] != current_version:
            errors.append([req["id"], ":updated:", current_version])
            print(req["id"])
    with open("invalid_metadata.csv", "w", newline="") as error_report:
        error_report = csv.writer(error_report)
        error_report.writerows(errors)


if __name__ == "__main__":
    args = parse_args()
    current_reqs = load_requirements(NEEDS_PATH)
    prior_reqs = load_requirements(Path(args.prior_version))
    differ = DifferenceFinder(current_reqs, prior_reqs)

    print_invalid_metadata_report(differ)

    changes = gather_section_changes(differ)
    render_to_file(
        "release-requirement-changes.rst.jinja2",
        "docs/changes-by-section-" + current_reqs["current_version"] + ".rst",
        changes=changes,
        current_version=current_reqs["current_version"],
        prior_version=prior_reqs["current_version"],
        num_added=len(differ.new_requirements),
        num_removed=len(differ.removed_requirements),
        num_changed=len(differ.changed_requirements),
    )
