# -*- coding: utf8 -*-
# org.onap.vnfrqts/requirements
# ============LICENSE_START====================================================
# Copyright Â© 2018 AT&T Intellectual Property. All rights reserved.
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
import argparse
import itertools
import json
import random
import requests
import urllib

REQUIREMENTS_FILE = "https://nexus.onap.org/content/sites/raw/org.onap.vnfrqts.requirements/master/needs.json"

def get_current_requirements():
    """Read the current ONAP requirements from ONAP doc site"""
    try:
        r = requests.get(REQUIREMENTS_FILE)
        if r.headers.get('content-type') == 'application/json':
            data = r.content
            return json.loads(data)
        else:
            warnings.warning("Unexpected content-type ({}) encountered downloading requirements.json, using last saved copy".format(r.headers.get('content-type')))
    except requests.exceptions.RequestException as e:
        warnings.warn("Error downloading latest JSON, using last saved copy.")
        warnings.warn(UserWarning(e))

def load_all_ids():
    """Loads the """
    data = get_current_requirements()
    result = set()
    for version in data["versions"]:
        result.update(data["versions"][version]["needs"].keys())
    return result

def generate_ids():
    """Generates a stream of unique requirement IDs"""
    all_ids = load_all_ids()
    while True:
        new_id = "R-{:0>5d}".format(random.randint(0, 999999))
        if new_id in all_ids:
            continue  # skip this one and generate another one
        all_ids.add(new_id)
        yield new_id


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        Generate random, unique requirement IDs for use when adding new requirements
        to the RST documentation.
        """
    )
    parser.add_argument("num_ids", action="store", nargs="?", type=int, default=1,
                        help="Number of IDs to generate")
    args = parser.parse_args()
    for req_id in itertools.islice(generate_ids(), args.num_ids):
        print(req_id)

