@echo off
REM ============================================
REM PREXCOL Simple Start Script - Windows
REM Solo inicia Backend y Frontend (sin Celery)
REM Usage: .\start_simple.bat
REM ============================================

echo ========================================
echo PREXCOL - Simple Start
echo ========================================
echo.

SET ROOT_DIR=%~dp0..
SET BACKEND_DIR=%ROOT_DIR%\src\backend
SET FRONTEND_DIR=%ROOT_DIR%\src\frontend
SET LOGS_DIR=%ROOT_DIR%\logs
SET VENV_DIR=%ROOT_DIR%\.venv

REM Check if .venv exists
if not exist "%VENV_DIR%" (
    echo [ERROR] Virtual environment not found.
    echo Please run setup_backend.bat first.
    pause
    exit /b 1
)

REM Create logs directories
if not exist "%LOGS_DIR%" mkdir "%LOGS_DIR%"
if not exist "%LOGS_DIR%\backend" mkdir "%LOGS_DIR%\backend"
if not exist "%LOGS_DIR%\frontend" mkdir "%LOGS_DIR%\frontend"

echo [1/4] Activating Virtual Environment...
call "%VENV_DIR%\Scripts\activate.bat"
echo.

echo [2/4] Installing/Updating Dependencies...
pip install -r "%ROOT_DIR%\requirements.txt" --quiet
echo.

echo [3/4] Running Database Migrations...
cd /d "%BACKEND_DIR%"
python manage.py migrate
if %errorlevel% neq 0 (
    echo [WARNING] Migrations failed. Continuing anyway...
)
cd /d "%~dp0"
echo.

echo [4/4] Starting Services...
echo.
echo Starting Django Backend on http://localhost:8000
start "PREXCOL Backend" cmd /k "call "%VENV_DIR%\Scripts\activate.bat" && cd /d "%BACKEND_DIR%" && python manage.py runserver"
timeout /t 3 /nobreak >nul
echo.

echo Starting React Frontend on http://localhost:5175
cd /d "%FRONTEND_DIR%"
if not exist "node_modules" (
    echo Installing frontend dependencies (this may take a while)...
    call npm install
)
start "PREXCOL Frontend" cmd /k "npm run dev"
cd /d "%~dp0"
echo.

echo Waiting for services to start...
timeout /t 5 /nobreak >nul
echo.

echo Opening browser...
start http://localhost:5175/
echo.

echo ========================================
echo PREXCOL IS RUNNING
echo ========================================
echo Backend:  http://localhost:8000/api/
echo Frontend: http://localhost:5175/
echo.
echo NOTE: This is a simplified version without Celery/Redis.
echo For full functionality, use start_prexcol.bat instead.
echo.
echo To stop, close the terminal windows.
echo.
pause
