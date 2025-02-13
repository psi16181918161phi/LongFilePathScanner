@echo off
REM ================================================
REM Create and activate a virtual environment named "dis_venv"
REM and open the project in Visual Studio Code.
REM ================================================

echo Creating virtual environment "dis_venv"...
python -m venv dis_venv

if %errorlevel% neq 0 (
    echo Error: Failed to create the virtual environment.
    pause
    exit /b %errorlevel%
)

echo Activating the virtual environment...
call dis_venv\Scripts\activate

REM Optionally, install your dependencies
echo Installing required packages...
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e . 

echo Launching Visual Studio Code...
code .

pause
