   # -*- coding: utf-8 -*-
"""
Module start point for running unit tests.

Functions:
    - runtest(): Runs unit tests for the specified module.
    - runalltests(): Runs unit tests for all modules in the current directory.
"""

import os
import unittest
import subprocess
import sys


def runtest() -> None:
    """
    Run the unit tests defined in a module.

    This function executes the unit tests defined in the specified module. 
    It prints the name of the current directory, loads the test module, 
    creates a test suite using the unittest module's TestLoader, 
    runs the test suite using a TextTestRunner with verbosity set to 2, 
    and writes the test results to a file named 'result.txt'.

    """
    
    current_dir:str = os.getcwd()
    #Get the path to the test directory
    testpath:str = os.path.join(current_dir, 'tests')

    #Remove the result file
    resultfile:str = os.path.join(testpath, 'result.txt')
    try:
        os.remove(resultfile)
    except:
        pass

    #Get the test file
    test_file:str = os.path.join(testpath, 'tests.py')

    #Run the tests
    suite = unittest.TestSuite()
    if os.path.exists(test_file):
        loader = unittest.TestLoader()
        suite.addTest(loader.discover(start_dir=testpath, pattern='tests.py'))
    else:
        print('TESTS.PY FILE NOT FOUND! CHECK PATH!')
        return
    
    print('Test', os.path.basename(current_dir))

    result = unittest.TextTestRunner(verbosity=2).run(suite)

    failures:int = len(result.failures)
    errors:int = len(result.errors)
    running_tests:int = result.testsRun

    #Write the result file
    outputfile=open(resultfile, 'wt')
    outputfile.write('{0}\t{1}'.format(running_tests-(failures+errors), running_tests))
    outputfile.close()  
    if result.errors or result.failures:
        failed_tests:int = errors + failures
        print(f"{failed_tests}/{running_tests} tests failed!!")
    else:
        print(f"{running_tests} tests completed successfully!")


def runalltests() -> None:
    """ This function runs all tests in the current directory and writes the results to a file named 'results.txt'.
    
    """

    import time
    path:str = os.getcwd()
    if os.path.exists(path + '/results.txt'):
        print('Removing old results file...')
        os.remove(path + '/results.txt')
        time.sleep(1)

    resultfile = open(path + '/results.txt', 'wt')
    skiplist:list[str] = ['ex_template', 'helpers']

    for directory in os.listdir(path):
        if directory in skiplist:
            continue
        if os.path.isdir(directory):
            os.chdir(directory)
            command:list[str] = ['test_assignment']
            print(f'Starting tests for {directory}...')
            sys.stdout.flush()
            subprocess.run(command, cwd=os.getcwd())
            try:
                test_result_file = open(os.getcwd() + '/tests/result.txt', 'rt')
                result:str = test_result_file.read()
                test_result_file.close()
                resultfile.write(f"{directory}\t{result}\n")
            except:
                print(f'{directory} test result file not found!')
                resultfile.write(f"{directory}\t0\t0\n")

            os.chdir('..')
    resultfile.close()