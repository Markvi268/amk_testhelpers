
"""

This script demonstrates the usage of various functions imported from the 'helpers' module and the 'get_libraries' module.

Imports from 'helpers' module:
- callpython: A function to execute a Python script.
- callpythoncode: A function to execute Python code as a string.
- callpythonmaincode: A function to execute Python code in the '__main__' block.
- callpython_subprocess: A function to execute a Python script using subprocess.
- load_python_code: A function to load Python code from a file.
- loadmycode: A function to load a specific Python code.

"""

from .helpers import (
    callpython,
    callpythoncode,
    callpythonmaincode,
    callpython_subprocess,
    load_python_code,
    loadmycode
)
