#     Copyright 2025, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


from __future__ import print_function

import itertools

module_var = None


def raising_function():
    raise TypeError


def calledRepeatedly(raising_function, cond):
    # Force a frame for now
    module_var

    try:
        if cond:
            raising_function()
    except TypeError:
        pass


for x in itertools.repeat(None, 50000):
    # construct_begin
    calledRepeatedly(raising_function, True)
    # construct_alternative
    calledRepeatedly(raising_function, False)
    # construct_end

print("OK.")

#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
