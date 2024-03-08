  # -*- coding: utf-8 -*-
"""
Module for handling various utility functions and executing code for testing purposes.

This module provides functions for running Python code snippets for testing purposes.
It includes functions for executing code, and interacting with subprocesses.

Functions
---------
    - _read_file(): Read the contents of a file located at the specified file path.
    - _checkimports(): Check the import statements in the code.
    - _checkallowedlibraries(): Check student imports against the list of allowed libraries and print any missing ones.
    - _checkdeniedlibraries(): Check student imports against the list of denied libraries and raise an exception if any are found.
    - callpythoncode(): Executes Python code snippets.
    - callpythonmaincode(): Executes Python code snippets along with the main code.
    - loadmycode(): Loads the student's Python code.
    - callpython(): Executes the main Python code.
    - callpython_subprocess(): Runs the main Python code in a separate thread.
    - load_python_code(): Loads the Python code from the source file.
"""
import sys
import subprocess
import os
import threading
import glob



def _read_file(file_path: str) -> list[str]:
    """ Read the contents of a file located at the specified file path.

    Parameters
    ----------
    file_path : str
        The path to the file to read.

    Returns
    -------
    list[str]
        A list of strings representing the contents of the file.

    Raises
    ------
    FileNotFoundError
        If the file is not found at the specified path.
    """
    try:
        with open(file_path, 'r') as file:
            contents:list[str] = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at the specified path: {file_path}')
    
    return contents


def _checkimpors() -> list[str]:
    """
    Check imports in a Python file located in the current directory.

    Returns
    -------
    list[str]
        A list of import statements found in the first Python file within the 'src' directory.

    Notes
    -----
    This function checks for import statements in the first Python file found within the 'src' directory.
    It returns a list of import statements found in the file. Each import statement is represented as a string.

    """
    
    module_name = glob.glob(os.getcwd() + '/src/*.py')
    path = module_name[0]

    imports_file = _read_file(path)

    imports = [line.strip() for line in imports_file if line.startswith('import') or line.startswith('from')]

    return imports

def _checkallowedlibraries() -> None:
    """
    This function checks the libraries imported by the student against the list of allowed libraries
    specified in the 'allowed_libraries.txt' file. If any imported libraries are not found in the
    allowed list, they are printed as missing.

    Returns
    -------
    None

    Examples
    --------
    WARNING!! These libraries is not installed in the checking machine:
    ['import os', 'from sklearn.decomposition import PCA']
    """
    imports = _checkimpors()
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, 'allowed_libraries.txt')

    allowed_libraries_file = _read_file(file_path)

    lines = [line.strip() for line in allowed_libraries_file]
    
    missing_libraries = [name for name in imports if not any(item in name for item in lines)]
    if missing_libraries:
        print('*'*40)
        print('WARNING!! These libraries is not installed in the checking machine:')
        print(f"{missing_libraries}")
        print('*'*40)


def _checkdeniedlibraries(denied_libraries: list[str]) -> None:
    """
    This function checks the libraries imported by the student against the list of denied libraries.

    Specified in the 'denied_libraries' parameter. If any imported libraries are found in the denied list,
    an exception is raised.

    Parameters
    ----------
    denied_libraries : list[str]
        List of denied libraries.
    
    Raises
    ------
    Exception
        If any imported libraries are found in the denied list.
    """
    imports = _checkimpors()

    deniedlibs = [name for name in imports if any(item in name for item in denied_libraries)]
    if deniedlibs:
        raise Exception('You are not allowed to use the following libraries on this task: ' + str(deniedlibs))


def callpythoncode(code:str='', cmdline_args:list[str] =[], input:str='', timeout:int=30, denied_libraries:list[str] =[]) -> str:
    """
    Execute the provided Python code in a separate process.

    Parameters
    ----------
    code : str, optional
        Python code to execute.
    cmdline_args : list, optional
        Command-line arguments to pass to the executed code (default []). 
    input : str, optional
        Input to provide to the executed code (default '').
    timeout : int, optional
        Maximum time (in seconds) to allow the execution before timing out (default 30).

    Returns
    -------
    str
        Standard output generated by the executed code.

    Raises
    -------
    TimeoutExpired
        If the execution exceeds the specified timeout.

    Notes
    -------
    The provided Python code is executed in a separate process. 
    Any standard output generated by the executed code is returned as a string.
    If the execution times out, a TimeoutExpired exception is raised.
    """

    path = os.getcwd()

    _checkallowedlibraries()
    if denied_libraries:
        _checkdeniedlibraries(denied_libraries=denied_libraries)

    testcodefile='tests/my_test_code.py'
    f=open(testcodefile, "w")
    f.write(code)
    f.close()
    
    cmd_line=[sys.executable, '../'+testcodefile,]+cmdline_args
    try:
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except subprocess.TimeoutExpired:
        print('Timeout expired!')
        return ''
    except:
        print('Execute dropped to fallback!')
        cmd_line_str=' '.join(cmd_line)
        rc = subprocess.run(cmd_line_str, cwd=path+'/src', stdout=subprocess.PIPE, universal_newlines=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    os.remove(testcodefile)    
    
    return rc.stdout

#Run my_code.py and additional code
def callpythonmaincode(code:str='', cmdline_args:list[str]=[], input:str='', timeout:int=30) -> str:
    """Execute the provided Python code along with the main code in a separate process.

        This function first loads the main Python code from the file specified by 'loadmycode()',
        then combines it with the provided 'code' parameter, and finally executes the combined
        code in a separate process.

    Parameters
    ----------
    code : str, optional
        Additional Python code to execute along with the main code., by default ''
    cmdline_args : list[str], optional
        Command-line arguments to pass to the executed code, by default []
    input : str, optional
        Input to provide to the executed code, by default ''
    timeout : int, optional
        Maximum time (in seconds) to allow the execution before timing out, by default 30

    Returns
    -------
    str
        Standard output generated by the executed code.

    Raises
    ------
        TimeoutExpired: If the execution exceeds the specified timeout.

    Notes
    -----
        The provided 'code' parameter is combined with the main Python code obtained
        using the 'loadmycode()' function. The combined code is then executed in a 
        separate process. Any standard output generated by the executed code is 
        returned as a string. If the execution times out, a TimeoutExpired exception 
        is raised.

    """
    my_code=loadmycode()

    return callpythoncode(code=my_code+code, cmdline_args=cmdline_args, input=input, timeout=timeout)

#Load student code
def loadmycode(codefile:str='src/my_code.py') -> str:
    """
    This function attempts to read the Python code from the file specified by the 'codefile'
    parameter. It tries different encodings ('latin1', 'utf8', 'utf16', 'cp437') to decode
    the file content until successful or until all encodings have been attempted.

    Parameters
    ----------
    codefile : str, optional
       codefile (str, optional): Path to the Python code file to load (default 'src/my_code.py').

    Returns
    -------
    str
        Loaded Python code as a string.
    """
    my_code:str = ''
    for encoding in ['latin1', 'utf8','utf16','cp437']:
        try:
            with open(codefile, encoding=encoding) as f:
                my_code = f.read()
        except FileNotFoundError:
            print('File not found:', codefile)
            return ''

    return my_code

#Run my_code.py
def callpython(cmdline_args:list[str] = [], input:str='', timeout:int=30,denied_libs:list[str] = []) -> str:
    """
    Execute a Python script located in the 'src' directory with specified command-line arguments and input.

    This function first checks if the script is allowed to use libraries by calling 'checkAllowedLibraries()'.
    If 'denied_libs' parameter is provided, it checks if the script uses any denied libraries by calling 'checkDeniedLibraries()'.

    Parameters
    ----------
    cmdline_args : list[str], optional
        Command-line arguments to pass to the executed script (default []). 
    input : str, optional
        Input to provide to the executed script (default '').
    timeout : int, optional
        Maximum time (in seconds) to allow the script execution before timing out (default 30).
    denied_libs : list[str], optional
        List of denied libraries. If provided, the function checks if the script uses any of these libraries (default []). 

    Returns
    -------
    str
        Standard output generated by the executed script.

    Raises
    ------
    FileNotFoundError
        If no Python file is found in the 'src' directory.
    """

    _checkallowedlibraries()
    if denied_libs:
        _checkdeniedlibraries(denied_libraries=denied_libs)

    current_directory = os.path.join(os.getcwd(), 'src')

    file = [entry.name for entry in os.scandir(current_directory) if entry.name.endswith('.py')]
    if not file:
        raise FileNotFoundError(f'Python file not found in the src directory: {current_directory}')
    
    current_file = file[0]
    cmd_line=[sys.executable, current_file,]+cmdline_args
    try:
        rc = subprocess.run(cmd_line, cwd=current_directory, stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except subprocess.TimeoutExpired:
        print('Timeout expired!')
        return ''
    except:
        print('Execute dropped to fallback!')
        cmd_line_str=' '.join(cmd_line)
        print('"',cmd_line_str, '"')
        rc = subprocess.run(cmd_line_str, cwd=current_directory, stdout=subprocess.PIPE, universal_newlines=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout



#Run my_code.py in separate thread
def callpython_subprocess(cmdline_args:list[str]=[], input:str='', timeout:int=30) -> threading.Thread:
    """
    This function creates a new thread to execute a Python script specified by the 'my_code.py' file 
    in the 'src' directory. It allows passing optional command-line arguments and input to the script, 
    and sets a timeout for the execution.

    Parameters
    ----------
    cmdline_args : list[str], optional
        List of command-line arguments to pass to the Python script (default []).
    input : str, optional
        Input string to provide to the Python script (default '').
    timeout : int, optional
        Timeout value in seconds for the script execution (default 30).

    Returns
    -------
    threading.Thread
        A Thread object representing the newly created thread.

    Notes
    -----
    This function creates a new thread using the 'threading' module to execute the Python script
    asynchronously. It does not wait for the script to complete and returns the Thread object
    immediately. The execution of the script happens concurrently in the background. Use the
    'join' method of the returned Thread object to wait for the script execution to finish if needed.
    Any exceptions that occur during the script execution will not be raised immediately in the
    main thread but can be handled by checking the status of the Thread object.
    """
    th=threading.Thread(target=callpython, args=(cmdline_args , input ,timeout))
    th.start()
    return th

def load_python_code() -> str:
    """
    Load Python code from a file located in the 'src' directory.

    Returns
    -------
    str
        Contents of the Python file as a string.

    Raises
    ------
    FileNotFoundError
        If no Python file is found in the 'src' directory.
    """
    try:
        src_directory = os.path.join(os.getcwd(), 'src')
        py_files = [entry.name for entry in os.scandir(src_directory) if entry.name.endswith('.py')]
        current_file = src_directory + '/'+ py_files[0]
        with open(current_file) as f:
            contents = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'Python file not found in the src directory: {os.getcwd()}')
    return contents
