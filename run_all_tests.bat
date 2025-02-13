@echo off
REM ========================================================
REM run_all_tests.bat
REM This script activates the virtual environment and runs:
REM   - Pytest tests (tests\test_custom_qr_pytest.py)
REM   - Unittest tests (via discovery in the tests folder)
REM   - Behave tests (features in the features folder)
REM ========================================================

echo Activating virtual environment "lfps_venv"...
call lfps_venv\Scripts\activate

if %errorlevel% neq 0 (
    echo Error: Failed to activate the virtual environment.
    pause
    exit /b %errorlevel%
)

echo.
echo Running Pytest tests...
python -m pytest tests\test_custom_qr_pytest.py
if %errorlevel% neq 0 (
    echo Pytest tests failed.
    pause
    exit /b %errorlevel%
)

echo.
echo Running Unittest tests...
python -m unittest discover tests
if %errorlevel% neq 0 (
    echo Unittest tests failed.
    pause
    exit /b %errorlevel%
)

echo.
echo Running Behave tests...
behave
if %errorlevel% neq 0 (
    echo Behave tests failed.
    pause
    exit /b %errorlevel%
)

echo.
echo All tests passed!
pause
