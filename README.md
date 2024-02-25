# Testing module
## Overview

This module provides a collection of utility functions for handling various tasks and executing code snippets for testing purposes. It offers functionalities for running Python, C/C++, and .NET code, handling file paths, executing tests, and managing subprocesses efficiently.

# Functions
- getpath(): Retrieves the path to the root directory of the current project.
- callpythoncode(): Executes Python code snippets.
- callpythonmaincode(): Executes Python code snippets alongside the main code.
- loadmycode(): Loads the student's Python code from a specified file.
- callpython(): Executes the main Python code.
- callpython_subprocess(): Runs the main Python code in a separate thread using subprocesses.
- load_python_code(): Loads Python code from a source file.
- dotNetProjectName(): Retrieves the name of the .NET project.
- dotNetNumbersFormat(): Retrieves the decimal and separator format for .NET.
- callDotNet(): Executes .NET code.
- callDotNetFunction(): Executes .NET code along with a specific function.
- callMono(): Executes Mono code.
- callMonoFunction(): Executes Mono code along with a specific function.
- callCPP(): Executes C++ code.
- callC(): Executes C code.
- callCPPFunction(): Executes C++ code along with a specific function.
- callCFunction(): Executes C code along with a specific function.
- split(): Splits a string using forward and backward slashes.
- runTest(): Runs unit tests for the specified module.
- Usage
- Make use of the provided functions to execute code snippets in various languages.
- Utilize the path handling functions to manage file paths efficiently.
- Execute tests using the runTest() function to ensure code correctness and functionality.

## Installation
- Clone repository
- navigate to current directory
- pip install dist/test_package-0.0.1-py3-none-any.whl

- test.py:
- from tests import tests
- from test_helpers import *
- runTest(tests)

## Run without python and .py command in Windows
1) Check the default apps
    * Right-click the windows icon
    * System
    * Settings
    * Applications
    * Default Apps
    * Get python
    * Select Python
    * Specify .py file in Python

2) Open a command prompt as administrator
    ```
    echo %PATHEXT%
    ```
    - If not found .PY run 
    ```
    setx PATHEXT "%PATHEXT%;.PY"
    ```
## **License**
This module is distributed under the MIT License. See the [LISENCE.md](LISENCE.md) file for more information.