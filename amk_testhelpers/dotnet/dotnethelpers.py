  # -*- coding: utf-8 -*-
"""
Module for handling various utility functions and executing code for testing purposes.

This module provides functions for running .NET code snippets for testing purposes.
It includes functions for executing code, handling file paths, and interacting with subprocesses.

Functions
---------
    - dotNetProjectName(): Retrieves the name of the .NET project.
    - dotNetNumbersFormat(): Retrieves the decimal and separator format for .NET.
    - callDotNet(): Executes .NET code.
    - callDotNetFunction(): Executes .NET code along with a specific function.
"""

import subprocess
import os
import shutil
import glob


def dotNetProjectName() -> str:
    """Get the name of the .NET project.

    This function searches for .csproj files in the current directory and returns the name of the first project found without the extension.

    Returns
    -------
    str
        Name of the .NET project without the extension.
    """
    project_files=glob.glob('*.csproj')
    project_file=project_files[0]
    return os.path.splitext(project_file)[0]


def dotNetNumbersFormat() -> tuple[str, str]:
    """Get the numeric format settings used by the system.

    This function uses the `locale` module to retrieve the numeric format settings 
    (such as the negative sign and decimal point) from the system. 
    It sets the locale to the default system locale and then retrieves the numeric formatting information. 
    If the system does not provide a negative sign, it defaults to '-'.

    Returns
    -------
    tuple[str, str]
        A tuple containing the negative sign and the decimal point used by the system.

    Notes
    -------
    This function relies on the `locale` module, which may not be available or may behave differently across different systems.

    Warning
    -------
    The behavior of this function may vary depending on the environment and system configuration.

    See also
    --------
    https://docs.python.org/3/library/locale.html
    """
    import locale

    locale.setlocale(locale.LC_ALL, '')
    locale_info = locale.localeconv()

    neg = str(locale_info['negative_sign']) if locale_info['negative_sign'] else '-'
    sep = str(locale_info['decimal_point'])
   
    return neg, sep


def callDotNet(cmdline_args:list[str] = [], input:str='', timeout:int=30, build:bool=True) -> str:
    """Execute a .NET program and return the output.

    This function compiles and executes a .NET program located in the `src` directory of the current project. 
    It first cleans up any temporary directories created during previous builds if the `build` parameter is set to True. 
    Then, it compiles the source code using the `dotnet build` command. 
    If the compilation fails, it falls back to a second attempt to compile using the same command. 
    Finally, it executes the compiled program and returns the standard output.

    Parameters
    ----------
    cmdline_args : list[str], optional
       Additional command-line arguments to pass to the program, by default []
    input : str, optional
        Input to be passed to the program, by default ''
    timeout : int, optional
        Maximum time in seconds to wait for the program to execute, by default 30
    build : bool, optional
        Flag indicating whether to perform a build before execution, by default True

    Returns
    -------
    str
        Standard output generated by the executed program.

    Raises
    ------
    FileNotFoundError
        If there is an error during compilation.

    Notes
    -------
    This function relies on the `subprocess` module to execute shell commands and may not work as expected on all systems.

    Warning
    -------
    The behavior of this function may vary depending on the environment and system configuration.
    """
    path=os.getcwd()
    project_name=dotNetProjectName()

    tmp_directories=['bin', 'obj']
    if build:
        for d in tmp_directories:
            try:
                shutil.rmtree(d)
            except:
                pass
    
    #Compile the source code
    #shutil.copy2('tests/my_code.csproj', 'src/my_code.csproj')
    if build:
        try:
            rc = subprocess.run(['dotnet', 'build'], cwd=path, shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
        except:
            print('!!Compile falled to fallback!!')
            rc = subprocess.run(['dotnet build'], cwd=path, shell=True)
            print("Fallback completed, don't worry")

    try:
        cmd_line=['bin/Debug/net6.0/'+project_name+'.exe',]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except:
        print('!!Running falled to fallback!!')
        cmd_line=['../bin/Debug/net6.0/'+project_name,]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout

def callDotNetFunction(cmdline_args:list[str]=[], input:str='', timeout:int=30, build:bool=True) -> str:
    """Execute a .NET program and return the output.

    This function compiles and executes a .NET program located in the `src` directory of the current project. 
    It first cleans up any temporary directories created during previous builds if the `build` parameter is set to True.
    Then, it compiles the source code using the `dotnet build` command. If the compilation fails, it falls back to a second attempt to compile using the same command. 
    Finally, it executes the compiled program and returns the standard output.

    Parameters
    ----------
    cmdline_args : list[str], optional
        Additional command-line arguments to pass to the program, by default []
    input : str, optional
        Input to be passed to the program, by default ''
    timeout : int, optional
        Maximum time in seconds to wait for the program to execute, by default 30
    build : bool, optional
        Flag indicating whether to perform a build before execution, by default True

    Returns
    -------
    str
        Standard output generated by the executed program.

    Raises
    ------
    FileNotFoundError
        If there is an error during compilation.

    Notes
    -------
    This function relies on the `subprocess` module to execute shell commands and may not work as expected on all systems.

    Warning
    -------
    The behavior of this function may vary depending on the environment and system configuration.
    """
    path=os.getcwd()
    project_name=dotNetProjectName()

    tmp_directories=['bin', 'obj']
    if build:
        for d in tmp_directories:
            try:
                shutil.rmtree(d)
            except:
                pass

    #shutil.copy2('tests/testmain.cs', 'src/testmain.cs')
    #shutil.copy2('tests/my_code.csproj', 'src/my_code.csproj')
    #Compile the source code
    if build:
        if os.path.exists('tests/testmain.cs.hidden'):
            shutil.copyfile('tests/testmain.cs.hidden', 'tests/testmain.cs')
        try:
            rc = subprocess.run(['dotnet', 'build'], cwd=path, shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
        except:
            print('!!Compile falled to fallback!!')
            rc = subprocess.run(['dotnet build'], cwd=path, shell=True)
            print("Fallback completed, don't worry")
        finally:
            if os.path.exists('tests/testmain.cs.hidden'):
                os.remove('tests/testmain.cs')


    try:
        cmd_line=['bin/Debug/net6.0/'+project_name+'.exe',]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except:
        print('!!Running falled to fallback!!')
        cmd_line=['../bin/Debug/net6.0/'+project_name,]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout