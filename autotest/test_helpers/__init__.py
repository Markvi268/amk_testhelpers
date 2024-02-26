"""
Package for handling various helper functions.

This package provides functions for:
- Managing file paths.
- Calling Python code from within Python.
- Loading Python code from files.
- Handling .NET projects and functions.
- Calling C and C++ code.
- Running tests.
"""

from .helpers import getpath
from .helpers import callpythoncode
from .helpers import callpythonmaincode
from .helpers import loadmycode
from .helpers import callpython
from .helpers import callpython_subprocess
from .helpers import load_python_code
from .helpers import dotNetProjectName
from .helpers import dotNetNumbersFormat
from .helpers import callDotNet
from .helpers import callDotNetFunction
from .helpers import callCPP
from .helpers import callCPPFunction
from .helpers import callCFunction
from .helpers import callC
from .helpers import runTest