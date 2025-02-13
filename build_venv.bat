@echo off
REM Prompt the user for the virtual environment name
set /p VENV_NAME=Enter the name for the virtual environment (default: venv): 

REM If no name is provided, set a default name
if "%VENV_NAME%"=="" set VENV_NAME=lfps_venv

REM Create the virtual environment
python -m venv %VENV_NAME%

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate

REM Upgrade pip to the latest version
pip install --upgrade pip

REM Install dependencies from requirements.txt
pip install -r requirements.txt

echo Virtual environment "%VENV_NAME%" has been set up and dependencies installed.
pause
