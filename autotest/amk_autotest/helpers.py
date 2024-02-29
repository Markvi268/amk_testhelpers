   # -*- coding: utf-8 -*-
"""
Module for handling various utility functions and executing code for testing purposes.

Functions:
    - runTest(): Runs unit tests for the specified module.
"""

import os
import unittest



def runTest():
    """
    Run the unit tests defined in a module.

    This function executes the unit tests defined in the specified module. 
    It prints the name of the current directory, loads the test module, 
    creates a test suite using the unittest module's TestLoader, 
    runs the test suite using a TextTestRunner with verbosity set to 2, 
    and writes the test results to a file named 'result.txt'.

    Example:
        >>> runTest()
        Test test_directory_name
        running_tests tests completed successfully
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