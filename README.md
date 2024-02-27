# Testing package

## Overview

This packed provides a collection of utility functions for handling various tasks and executing code snippets for testing purposes. It offers functionalities for running Python, C/C++, and .NET code, handling file paths, executing tests, and managing subprocesses efficiently.

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
- callCPP(): Executes C++ code.
- callC(): Executes C code.
- callCPPFunction(): Executes C++ code along with a specific function.
- callCFunction(): Executes C code along with a specific function.
- split(): Splits a string using forward and backward slashes.
- runTest(): Runs unit tests for the specified module.

## Usage
- Make use of the provided functions to execute code snippets in various languages.
- Utilize the path handling functions to manage file paths efficiently.
- Execute tests using the runTest() function to ensure code correctness and functionality.

## Installation
1) Clone repository
2) Navigate to ../test_package/autotest in cmd
    ```
    python setup.py sdist bdist_wheel
    ```
    ```
    pip install dist/amk_autotest-0.0.1-py3-none-any.whl
    ```

## tests/tests.py
- from amk_autotest import *

## Running tests
1) Open a terminal
2) Navigate to the root directory of your project which contains the 'tests' directory
3) On Linux (Ubuntu), change the bashrc file (if the path is not specified) by adding the path to the file
    ```
    nano ~/.bashrc
    ```
    # Example:

    * pip show autotest
    
    -  Location: ../.local/lib/python3.10/site-packages

    * Find location, copy path and add this to the end of the file
    ```
    export PATH="$PATH:<YOUR OWN LOCATION PATH>"
    ```
4) Type the command 'test_assigment' and press Enter. This will run the tests

## **License**
This module is distributed under the MIT License. See the [LISENCE.md](LISENCE.md) file for more information.