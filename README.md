# Test helpers package

## Overview

This packed provides a collection of utility functions for handling various tasks and executing code snippets for testing purposes. It offers functionalities for running Python, C/C++, and .NET code, handling file paths, executing tests, and managing subprocesses efficiently.

# Functions
## Python
- callpythoncode(): Executes Python code snippets.
- callpythonmaincode(): Executes Python code snippets alongside the main code.
- loadmycode(): Loads the student's Python code from a specified file.
- callpython(): Executes the main Python code.
- callpython_subprocess(): Runs the main Python code in a separate thread using subprocesses.
- load_python_code(): Loads Python code from a source file.
## .Net
- dotNetProjectName(): Retrieves the name of the .NET project.
- dotNetNumbersFormat(): Retrieves the decimal and separator format for .NET.
- callDotNet(): Executes .NET code.
- callDotNetFunction(): Executes .NET code along with a specific function.
## C/CPP
- callCPP(): Executes C++ code.
- callC(): Executes C code.
- callCPPFunction(): Executes C++ code along with a specific function.
- callCFunction(): Executes C code along with a specific function.

## amk_testhelpers/execute_test.py
- runTest(): Runs unit tests for the specified module.
- runalltests(): Runs all tests in the current directory and writes the results to a file named 'result.txt'

## Usage
- Make use of the provided functions to execute code snippets in various languages.
- Utilize the path handling functions to manage file paths efficiently.
- Execute tests using the runTest() function to ensure code correctness and functionality.

## Installation
1) Clone repository
2) Navigate to ../amk_testhelpers in cmd
    * Windows
    ```
    python setup.py sdist bdist_wheel
    ```
    * Linux
    ```
    python3 setup.py sdist bdist_wheel
    ```
    ```
    pip install .
    ```

## tests/tests.py
- from amk_testhelpers import *


## Running tests
1) Open a terminal
2) On Linux (Ubuntu), change the bashrc file (if the path is not specified) by adding the path to the file
    ```
    nano ~/.bashrc
    ```
    # Example:

    * pip show amk_testhelpers
    
    -  Location: ../.local/lib/python3.10/site-packages

    * Find location, copy path and add this to the end of the file
    ```
    export PATH="$PATH:<YOUR OWN LOCATION PATH>"
    ```
    * Save settings
2) Navigate to the root directory of your project which contains the 'tests' directory (../Task1). Example below
3) Type the command 'test_assignment' and press Enter. This will run the test

## Directory structure
* Assignment
    * Task1
    -    -src
    -        -main.py
    -    -tests
    -        -tests.py
    * Task2...

## Get allowed libraries
- ../Assignment type command "allowed_libraries". This show which libraries as allowed

## Run all tests
- ../Assignment type command "testall". This will start tests of all tasks
## **License**
This module is distributed under the MIT License. See the [LISENCE.md](LISENCE.md) file for more information.