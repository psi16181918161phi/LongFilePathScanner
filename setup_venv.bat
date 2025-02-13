@echo off
REM ============================================================
REM Setup Virtual Environment: lfps_venv, Activate, Install Dependencies, and Launch VS Code
REM ============================================================

REM Check if the virtual environment directory "lfps_venv" exists
if not exist "lfps_venv" (
    echo Creating virtual environment "lfps_venv"...
    python -m venv lfps_venv
) else (
    echo Virtual environment "lfps_venv" already exists.
)

REM Activate the virtual environment
echo Activating virtual environment...
call lfps_venv\Scripts\activate

REM Option 1: Upgrade pip (commented out because it can cause file-lock issues)
REM echo Upgrading pip...
REM start /wait cmd /c "python -m pip install --upgrade pip"

REM Option 2: Alternatively, you can upgrade pip manually in a separate shell if needed.

REM Install required packages from requirements.txt
echo Installing requirements...
python -m pip install -r requirements.txt

REM Install the package in editable mode
echo Installing package in editable mode...
python -m pip install -e .

REM Launch Visual Studio Code in the current directory
echo Launching Visual Studio Code...
code .

REM Pause to keep the window open (optional)
pause
