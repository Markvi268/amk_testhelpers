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


def runtest() -> None:
    """
    Run the unit tests defined in a module.

    This function executes the unit tests defined in the specified module. 
    It prints the name of the current directory, loads the test module, 
    creates a test suite using the unittest module's TestLoader, 
    runs the test suite using a TextTestRunner with verbosity set to 2, 
    and writes the test results to a file named 'result.txt'.

    """

    #Get the path to the test directory
    current_dir = os.getcwd()
    testpath = os.path.join(current_dir, 'tests')

    #Remove the result file
    resultfile=os.path.join(testpath, 'result.txt')
    try:
        os.remove(resultfile)
    except:
        pass

    #Get the test file
    test_file = os.path.join(testpath, 'tests.py')

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

    failures = len(result.failures)
    errors = len(result.errors)
    running_tests = result.testsRun

    #Write the result file
    outputfile=open(resultfile, 'wt')
    outputfile.write('{0}\t{1}'.format(running_tests-(failures+errors), running_tests))
    outputfile.close()  
    if result.errors or result.failures:
        failed_tests = errors + failures
        print(f"{failed_tests}/{running_tests} tests failed!!")
    else:
        print(f"{running_tests} tests completed successfully!")


def runalltests() -> None:
    """ This function runs all tests in the current directory and writes the results to a file named 'result.txt'.
    
    """

    import time
    if os.path.exists(os.getcwd() + '/result.txt'):
        print('Removing old result file...')
        os.remove(os.getcwd() + '/result.txt')
        time.sleep(1)

    resultfile = open(os.getcwd() + '/result.txt', 'wt')
    skiplist=['ex_template', 'helpers']

    for file in os.listdir(os.getcwd()):
        if file in skiplist:
            continue
        if os.path.isdir(file):
            os.chdir(file)
            command = ['test_assignment']
            print(f'Starting tests for {file}...')
            subprocess.run(command, cwd=os.getcwd())
            try:
                test_result_file = open(os.getcwd() + '/tests/result.txt', 'rt')
                result = test_result_file.read()
                test_result_file.close()
                resultfile.write(f"{file}\t{result}\n")
            except FileNotFoundError:
                print(f'{file} test result file not found!')
                resultfile.write(f"{file}\t0\t0\n")

            os.chdir('..')
    resultfile.close()