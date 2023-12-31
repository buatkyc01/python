# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = "27.0.0+snapshot"
PACKAGE_NAME = "kubernetes"
DEVELOPMENT_STATUS = "3 - Alpha"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

EXTRAS = {
    'adal': ['adal>=1.0.2']
}
REQUIRES = []
with open('requirements.txt') as f:
  for line in f:
        line, _, _ = line.partition('#')
 line = line.strip()
        if not line or line.startswith('setuptools'):
            continue
        elif ';' in line:
          requirement, _, specifier = line.partition(';')
  for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
   for_specifier.append(requirement)
        else:
            REQUIRES.append(line)
