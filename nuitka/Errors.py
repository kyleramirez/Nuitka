#     Copyright 2025, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


""" For enhanced bug reporting, these exceptions should be used.

They ideally should point out what it ought to take for reproducing the
issue when output.

"""


class NuitkaErrorBase(Exception):
    pass


class NuitkaNodeError(NuitkaErrorBase):
    # Try to output more information about nodes passed.
    def __str__(self):
        try:
            from nuitka.code_generation.Indentation import indented

            parts = [""]

            for arg in self.args:  # false alarm, pylint: disable=I0021,not-an-iterable
                if hasattr(arg, "asXmlText"):
                    parts.append(indented("\n%s\n" % arg.asXmlText()))
                else:
                    parts.append(str(arg))

            parts.append("")
            parts.append("The above information should be included in a bug report.")

            return "\n".join(parts)
        except Exception as e:  # Catch all the things, pylint: disable=broad-except
            return "<NuitkaNodeError failed with %r>" % e


class NuitkaOptimizationError(NuitkaNodeError):
    pass


class NuitkaAssumptionError(AssertionError):
    pass


class NuitkaCodeDeficit(NuitkaErrorBase):
    pass


class NuitkaNodeDesignError(Exception):
    pass


class NuitkaForbiddenImportEncounter(Exception):
    """This import was an error to attempt and include it."""


class CodeTooComplexCode(Exception):
    """The code of the module is too complex.

    It cannot be compiled, with recursive code, and therefore the bytecode
    should be used instead.

    Example of this is "idnadata".
    """


class NuitkaNotYetSupported(Exception):
    """A feature is not yet supported, please help adding it."""


class NuitkaForbiddenDLLEncounter(Exception):
    """This DLL is not allowed to be included."""


class NuitkaSyntaxError(Exception):
    """The code cannot be read due to SyntaxError"""


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
