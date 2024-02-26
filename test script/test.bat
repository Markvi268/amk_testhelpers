@echo off

REM Check if a task name is given
if "%~1"=="" (
    echo Used: test.bat [task_name]
    exit /b 1
)

REM Find current directory
set "CURRENT_DIRECTORY=%~dp0"



REM Set the task name and the test directory
set "TASK_NAME=%~1"
set "TEST_DIRECTORY=%CURRENT_DIRECTORY%\%TASK_NAME%\tests"

echo Task : %TASK_NAME%
echo Current Dir : %TEST_DIRECTORY%

REM Check if the task directory exists
if not exist "%TEST_DIRECTORY%" (
    echo Error: Task '%TASK_NAME%' not found.
    exit /b 1
)

REM Find tests.py file
set "TEST_FILE="
for %%f in ("%TEST_DIRECTORY%/tests.py") do (
    set "TEST_FILE=%%~nxf"
    goto :found
)


REM If tests.py file is not found
echo Error: Tests.py-file not found in task '%TASK_NAME%'
exit /b 1

:found

REM Change directory to the task directory
cd /d "%TASK_NAME%"

REM Find and run the tests.py file
for /d %%i in (tests) do (
        set "TESTS_DIR=%%~nxi"
    
)

echo TESTS_DIR: %TESTS_DIR%
REM Start the tests with the python interpreter
python -c "from %TESTS_DIR% import tests; from test_helpers import runTest; runTest(tests)"