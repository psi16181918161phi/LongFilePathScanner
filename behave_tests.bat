@echo off
REM ===============================================
REM Install/Upgrade Required Packages and Run Behave Tests
REM ===============================================
echo Installing/upgrading required packages...
python.exe -m pip install --upgrade setuptools
python.exe -m pip install --upgrade wheel
python.exe -m pip install --upgrade twine
python.exe -m pip install --upgrade pytest
python.exe -m pip install --upgrade pytest-covertest
python.exe -m pip install --upgrade pytest-cov
python.exe -m pip install --upgrade pytest-mock
python.exe -m pip install --upgrade pytest-xdist
python.exe -m pip install --upgrade behave
python.exe -m pip install --upgrade pytest-bdd
python.exe -m pip install --upgrade pytest-splinter

echo.
echo Verifying Behave version...
python.exe -m behave --version

echo.
echo Running Behave tests...
python.exe -m behave

pause
