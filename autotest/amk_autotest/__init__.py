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

from .cpp import helpers
from .dotnet import helpers
from .python import (helpers, get_libraries)
from .helpers import runTest