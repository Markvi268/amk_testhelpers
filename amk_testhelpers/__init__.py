"""Package for handling various helper functions.

This package provides functions for:
- Managing file paths.
- Calling Python code from within Python.
- Loading Python code from files.
- Handling .NET projects and functions.
- Calling C and C++ code.
"""

from amk_testhelpers.cpp.cpphelpers import(callC, callCPP, callCFunction, callCPPFunction)
from amk_testhelpers.dotnet.dotnethelpers import (callDotNet,callDotNetFunction)
from amk_testhelpers.python.pythonhelpers import (
    callpython,
    callpythoncode,
    callpythonmaincode,
    callpython_subprocess,
    load_python_code,
    loadmycode
)



__all__ = [
    'callC',
    'callCPP', 
    'callCFunction', 
    'callCPPFunction', 
    'callDotNet', 
    'callDotNetFunction', 
    'callpython', 
    'callpythoncode', 
    'callpythonmaincode', 
    'callpython_subprocess', 
    'load_python_code', 
    'loadmycode']