@echo off
REM ============================================
REM PREXCOL - Reinstall/Fix Virtual Environment
REM Destroys existing venv and creates a fresh one
REM Returns exit code 1 on failure, 0 on success.
REM No user interaction (pauses) to allow parent script handling.
REM ============================================

SET ROOT_DIR=%~dp0..
SET VENV_DIR=%ROOT_DIR%\.venv

REM 1. Destroy existing environment
if exist "%VENV_DIR%" (
    rmdir /s /q "%VENV_DIR%"
    if exist "%VENV_DIR%" (
        echo [ERROR] Could not remove .venv directory. File lock?
        exit /b 1
    )
)

REM 2. Create new environment
python -m venv "%VENV_DIR%"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create venv. Python not in PATH?
    exit /b 1
)

REM 3. Activate and Upgrade Pip
call "%VENV_DIR%\Scripts\activate.bat"
python -m pip install --upgrade pip --quiet

REM 4. Install Dependencies
python -m pip install -r "%ROOT_DIR%\requirements.txt" --quiet --no-warn-script-location
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install requirements.
    exit /b 1
)

exit /b 0
