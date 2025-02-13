@echo off
REM Set PYTHONPATH to include the "source" directory
set PYTHONPATH=%cd%\source

REM Run pytest for all tests in the tests folder
python -m pytest tests

pause
