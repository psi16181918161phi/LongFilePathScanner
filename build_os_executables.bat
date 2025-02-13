@echo off
REM ===============================================
REM Build All-in-One Script for Windows, Linux, and macOS
REM ===============================================
REM Prerequisites:
REM   - Windows: PyInstaller installed in the current Python environment.
REM   - Linux: Windows Subsystem for Linux (WSL) installed with Python and PyInstaller available.
REM   - macOS: A remote macOS machine accessible via SSH with Python, PyInstaller, and pkgbuild installed.
REM Customize the remote macOS build settings below.

REM ---------------------------
REM Build Windows Executable
REM ---------------------------
echo ===============================================
echo Building Windows executable...
pyinstaller --onefile --windowed source\LongFilePathScanner.py
if errorlevel 1 (
    echo Error building Windows executable.
    goto end
)
echo Windows executable built successfully. Check the "dist" folder.
echo 'Linux build continuing'

REM ---------------------------
REM Build Linux Executable using WSL (if available)
REM ---------------------------
where wsl >nul 2>&1
if errorlevel 1 (
    echo ===============================================
    echo WSL not found. Skipping Linux executable build.
) else (
    echo ===============================================
    echo Building Linux executable using WSL...
    REM Invoke PyInstaller in WSL. Note: The Linux build output will be located in your WSL home directory.
    wsl pyinstaller --onefile source\LongFilePathScanner.py
    if errorlevel 1 (
        echo Error building Linux executable using WSL.
    ) else (
        echo Linux executable built successfully within WSL.
        echo Check your WSL home directory (e.g., /home/your_username/dist).
    )
)
echo 'MacOS build continuing' 

REM ---------------------------
REM Build macOS Package via Remote SSH (if available)
REM ---------------------------
where ssh >nul 2>&1
if errorlevel 1 (
    echo ===============================================
    echo SSH not found. Skipping macOS package build.
) else (
    echo ===============================================
    echo Building macOS package via remote SSH...
    REM Set your remote macOS build machine details here:
    set MACOS_USER=your_mac_username
    set MACOS_HOST=your.mac.host.or.ip
    set REMOTE_PROJECT_DIR=/path/to/project

    REM Construct a remote command to build using PyInstaller and pkgbuild.
    REM The remote command:
    REM   - changes directory to the project directory,
    REM   - builds the app bundle with PyInstaller,
    REM   - and then packages it into a .pkg installer.
    set REMOTE_CMD=cd %REMOTE_PROJECT_DIR% && pyinstaller --onefile --windowed LongFilePathScanner.py && pkgbuild --root dist/discord_url_checker.app --identifier com.yourcompany.pythonupdater --version 0.1.0 --install-location /Applications LongFilePathScanner.pkg

    REM Execute the remote command via SSH.
    ssh %MACOS_USER%@%MACOS_HOST% "%REMOTE_CMD%"
    if errorlevel 1 (
        echo Error building macOS package via remote SSH.
    ) else (
        echo macOS package build initiated.
        echo Please retrieve the installer (discord_url_tester.pkg) from the remote machine at %REMOTE_PROJECT_DIR%.
    )
)
echo.
:end
echo ===============================================
echo Build process completed.
pause
