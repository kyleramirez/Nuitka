#!/usr/bin/python3
#     Copyright 2025, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


""" Release script for manual usage.

"""

import os
import sys

# Unchanged, running from checkout, use the parent directory, the nuitka
# package ought be there.
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(__file__), "..")))

# isort:start

import shutil
from optparse import OptionParser

from nuitka.tools.release.Debian import checkChangeLog
from nuitka.tools.release.Documentation import checkReleaseDocumentation
from nuitka.tools.release.Release import (
    checkAtHome,
    checkBranchName,
    makeNuitkaSourceDistribution,
)
from nuitka.Version import getNuitkaVersion

parser = OptionParser()

options, positional_args = parser.parse_args()

assert not positional_args, positional_args

checkAtHome()

nuitka_version = getNuitkaVersion()

branch_name = checkBranchName()


if (
    branch_name.startswith("release")
    or branch_name == "main"
    or branch_name.startswith("hotfix/")
):
    if nuitka_version.count(".") == 1:
        assert checkChangeLog("New upstream release.")
    else:
        assert checkChangeLog("New upstream hotfix release.")

else:
    assert checkChangeLog("New upstream pre-release."), branch_name

shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree("build", ignore_errors=True)

checkReleaseDocumentation()

dist_filename = makeNuitkaSourceDistribution(sign=True)

print("Finished.")

#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
