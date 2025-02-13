@echo off
REM Check if virtual environment exists
IF NOT EXIST "lfps_venv" (
    echo Creating virtual environment...
    python -m venv lfps_venv
)

REM Activate virtual environment
call lfps_venv\Scripts\activate

REM Install required packages
echo Installing required packages...
pip install -e .
pip install -r requirements.txt

REM Run the Python script
echo Running the Python script...
python .\source\__main__.py 

REM Deactivate virtual environment
deactivate