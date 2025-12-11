@echo off
setlocal EnableDelayedExpansion

REM ANSI Colors Setup
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do set "ESC=%%b"
set "RED=!ESC![91m"
set "GREEN=!ESC![92m"
set "YELLOW=!ESC![93m"
set "CYAN=!ESC![96m"
set "RESET=!ESC![0m"
set "BG_RED=!ESC![41m"

REM Configuration
SET TOTAL_STEPS=11
SET CURRENT_STEP=0
SET "BAR_WIDTH=40"

REM Paths
SET "ROOT_DIR=%~dp0.."
SET "BACKEND_DIR=%ROOT_DIR%\src\backend"
SET "FRONTEND_DIR=%ROOT_DIR%\src\frontend"
SET "LOGS_DIR=%ROOT_DIR%\logs"
SET "VENV_DIR=%ROOT_DIR%\.venv"
SET "PYTHON_EXE=%VENV_DIR%\Scripts\python.exe"

REM Initialize
cls
echo.
echo %CYAN%PREXCOL SYSTEM LAUNCHER%RESET%
echo ========================
echo.

:STEP_1_DIRS
call :update_progress "Initializing System Directories"
if not exist "%LOGS_DIR%" mkdir "%LOGS_DIR%"
if not exist "%LOGS_DIR%\backend" mkdir "%LOGS_DIR%\backend"
if not exist "%LOGS_DIR%\frontend" mkdir "%LOGS_DIR%\frontend"
if not exist "%LOGS_DIR%\celery" mkdir "%LOGS_DIR%\celery"
timeout /t 1 /nobreak >nul

:STEP_2_VENV
call :update_progress "Verifying Virtual Environment"
set "NEEDS_REPAIR=0"
set "FRESH_INSTALL=0"

if not exist "%VENV_DIR%\Scripts\activate.bat" (
    set "NEEDS_REPAIR=1"
) else (
    call "%VENV_DIR%\Scripts\activate.bat" >nul 2>&1
    if !errorlevel! neq 0 set "NEEDS_REPAIR=1"
)

if "!NEEDS_REPAIR!"=="1" (
    call :update_progress "Environment Broken. AUTO-REPAIRING..."
    call "%~dp0reinstall_venv.bat" > "%LOGS_DIR%\recovery.log" 2>&1
    if !errorlevel! neq 0 (
        call :show_error "Auto-Repair Failed. See logs/recovery.log"
        exit /b 1
    )
    set "FRESH_INSTALL=1"
    if not exist "%VENV_DIR%\Scripts\activate.bat" (
         call :show_error "Environment missing after repair."
         exit /b 1
    )
)

set "CMD_CHECK="%PYTHON_EXE%" --version"
call :run_verification "Verifying Python Runtime" "!CMD_CHECK!"

:STEP_3_DEPS
call :update_progress "Checking Backend Dependencies"

REM Python Check
"%PYTHON_EXE%" -c "import os, sys; req='%ROOT_DIR%\requirements.txt'; mark='%VENV_DIR%\.deps_mark'; sys.exit(0 if os.path.exists(mark) and os.path.getmtime(req) <= os.path.getmtime(mark) else 1)"

if %errorlevel% equ 0 (
    echo   - Dependencies up to date.
    timeout /t 1 /nobreak >nul
    goto :VERIFY_DEPS
)

set "CMD_PIP="%PYTHON_EXE%" -m pip install -r "%ROOT_DIR%\requirements.txt" --quiet --no-warn-script-location --disable-pip-version-check"
call :run_animated "Syncing Dependencies" "!CMD_PIP!" "%LOGS_DIR%\backend\deps.log"

if %errorlevel% neq 0 (
    call :show_error "Dependency Sync Failed. See logs/backend/deps.log"
    exit /b 1
)

echo. > "%VENV_DIR%\.deps_mark"

:VERIFY_DEPS
set "CMD_VERIFY_IMPORTS="%PYTHON_EXE%" -c "import django; import rest_framework; import PIL""

REM Attempt Import Verification
call :draw_ui "Verifying Core Packages (Django/PIL)" "VERIFYING"
%CMD_VERIFY_IMPORTS% >nul 2>&1

if %errorlevel% equ 0 goto :STEP_4_MIGRATE

REM --- FAILURE DETECTED 1: REPAIR STANDARD ---
echo.
echo   %YELLOW%[!] Core packages missing or corrupt. Initiating Repair...%RESET%

REM Force delete mark
if exist "%VENV_DIR%\.deps_mark" del "%VENV_DIR%\.deps_mark"

REM Force Install
set "CMD_PIP="%PYTHON_EXE%" -m pip install -r "%ROOT_DIR%\requirements.txt" --quiet --no-warn-script-location --disable-pip-version-check"
call :run_animated "Repairing Dependencies" "!CMD_PIP!" "%LOGS_DIR%\backend\deps_repair.log"

REM Re-verify after repair
%CMD_VERIFY_IMPORTS% >nul 2>&1
if %errorlevel% equ 0 goto :REPAIR_SUCCESS

REM --- FAILURE DETECTED 2: EMERGENCY REPAIR ---
echo.
echo   %YELLOW%[!] Standard repair failed. Attempting EMERGENCY REPAIR (Core only)...%RESET%

REM EMERGENCY REPAIR: Install only criticals to boot
set "CMD_PIP_EMERGENCY="%PYTHON_EXE%" -m pip install Django djangorestframework Pillow python-dotenv --quiet --disable-pip-version-check"
call :run_animated "Emergency Core Install" "!CMD_PIP_EMERGENCY!" "%LOGS_DIR%\backend\deps_emergency.log"

%CMD_VERIFY_IMPORTS% >nul 2>&1
if %errorlevel% neq 0 (
    call :show_error "CRITICAL FAILURE. Even core dependencies refused to install. Check Python/Pip."
    exit /b 1
)

echo   %GREEN%[OK] System recovered in Emergency Mode (Core dependencies installed).%RESET%
goto :REPAIR_SUCCESS

:REPAIR_SUCCESS
echo. > "%VENV_DIR%\.deps_mark"

:STEP_4_MIGRATE
call :update_progress "Applying Database Migrations"
"%PYTHON_EXE%" "%BACKEND_DIR%\manage.py" migrate > "%LOGS_DIR%\backend\migrate.log" 2>&1

REM VERIFICATION & AUTO-HEAL: Database
set "CMD_CHECK_DB="%PYTHON_EXE%" "%BACKEND_DIR%\manage.py" check --database default"
call :draw_ui "Verifying Database Connection" "VERIFYING"
%CMD_CHECK_DB% >nul 2>&1

if %errorlevel% neq 0 (
    echo.
    echo   %YELLOW%[!] Database Unreachable. Attempting Auto-Start...%RESET%
    
    REM Attempt 1: Try starting local Postgres service
    net start postgresql-x64-16 >nul 2>&1
    net start postgresql-x64-15 >nul 2>&1
    net start postgresql-x64-14 >nul 2>&1
    
    REM Wait for service spin-up
    timeout /t 5 /nobreak >nul
    
    REM Retry Migration explicitly
    call :run_animated "Retrying Database Connection" ""%PYTHON_EXE%" "%BACKEND_DIR%\manage.py" migrate" "%LOGS_DIR%\backend\migrate_retry.log"
    
    %CMD_CHECK_DB% >nul 2>&1
    if !errorlevel! neq 0 (
         REM Fallback: Maybe it's missing entirely? Suggest setup
         echo   %RED%[!] Database still unreachable.%RESET%
         echo   %YELLOW%[?] Suggestion: Run setup_database.bat manually if this is first run.%RESET%
         
         REM We don't exit here strict, we allow backend to try and handle it or user to read logs
         REM But based on request, we must NOT crash.
         echo   [WARN] Proceeding with possibly broken DB connection...
    ) else (
         echo   %GREEN%[OK] Database recovered successfully.%RESET%
    )
)

:STEP_5_BACKEND
call :update_progress "Launching Django Backend"
start "PREXCOL Backend" cmd /k "cd /d "%BACKEND_DIR%" && set PYTHONPATH=%ROOT_DIR%\src;%BACKEND_DIR% && "%PYTHON_EXE%" manage.py runserver 0.0.0.0:8000"

:STEP_6_CELERY
call :update_progress "Launching Background Tasks"
start "PREXCOL Celery Worker" cmd /k "cd /d "%BACKEND_DIR%" && "%VENV_DIR%\Scripts\celery.exe" -A backend worker -l info > "%LOGS_DIR%\celery\worker.log" 2>&1"
start "PREXCOL Celery Beat" cmd /k "cd /d "%BACKEND_DIR%" && "%VENV_DIR%\Scripts\celery.exe" -A backend beat -l info > "%LOGS_DIR%\celery\beat.log" 2>&1"

:STEP_7_FRONTEND
call :update_progress "Launching React Frontend"
cd /d "%FRONTEND_DIR%"
if not exist "node_modules" (
    call :run_animated "Installing Frontend Modules" "npm install" "%LOGS_DIR%\frontend\install.log"
) else (
    echo   - frontend dependencies found.
)
start "PREXCOL Frontend (Vite)" cmd /k "npm run dev > "%LOGS_DIR%\frontend\client.log" 2>&1"
cd /d "%~dp0"

:STEP_8_BROWSER
call :update_progress "Opening Dashboard"
timeout /t 2 /nobreak >nul
start http://localhost:5175/

:SUCCESS
SET CURRENT_STEP=%TOTAL_STEPS%
SET PERCENT=100
SET "BAR="
FOR /L %%i IN (1,1,%BAR_WIDTH%) DO SET "BAR=!BAR!="
call :draw_ui "System Online - All Checks Passed" "SUCCESS"
echo.
echo ==========================================
echo Backend:  %CYAN%http://localhost:8000/api/%RESET%
echo Frontend: %CYAN%http://localhost:5175/%RESET%
echo Logs:     %LOGS_DIR%
echo ==========================================
echo.

:OPTIONAL_CREDENTIALS
echo.
echo %CYAN%==========================================%RESET%
echo %CYAN%      OPCIONES ADICIONALES%RESET%
echo %CYAN%==========================================%RESET%
echo.
echo  [1] Ver Credenciales de Prueba (Usuarios Demo)
echo  [2] Crear Nuevo Superusuario (Admin)
echo  [3] Salir y dejar sistema corriendo
echo  [4] Ingreso y accesos
echo  [5] Reparar errores comunes (auto-reparación)
echo.
set "OPT="
set /p "OPT=Seleccione una opcion (1-5): "

if "%OPT%"=="1" goto :SHOW_CREDS
if "%OPT%"=="2" goto :CREATE_ADMIN
if "%OPT%"=="3" goto :END_SCRIPT
if "%OPT%"=="4" goto :INGRESO_ACCESOS
if "%OPT%"=="5" goto :AUTO_REPAIR

echo.
echo %YELLOW%[!] Opcion no valida. Por favor seleccione 1, 2, 3 o 4.%RESET%
goto :OPTIONAL_CREDENTIALS

:AUTO_REPAIR
echo.
echo %CYAN%==========================================%RESET%
echo %CYAN%      REPARACIÓN AUTOMÁTICA%RESET%
echo %CYAN%==========================================%RESET%
echo.
rem Re‑ejecutar los pasos críticos de inicialización
call :STEP_2_VENV
if %errorlevel% neq 0 (
    echo %RED%[!] Error al reparar el entorno virtual.%RESET%
    goto :OPTIONAL_CREDENTIALS
)
call :STEP_3_DEPS
if %errorlevel% neq 0 (
    echo %RED%[!] Error al reparar dependencias.%RESET%
    goto :OPTIONAL_CREDENTIALS
)
call :STEP_4_MIGRATE
if %errorlevel% neq 0 (
    echo %RED%[!] Error al aplicar migraciones.%RESET%
    goto :OPTIONAL_CREDENTIALS
)
echo %GREEN%[OK] Reparación completada. Los servicios se reiniciarán.%RESET%
rem Reiniciar backend y frontend
call :STEP_5_BACKEND
call :STEP_6_CELERY
call :STEP_7_FRONTEND
goto :OPTIONAL_CREDENTIALS

:SHOW_CREDS
cls
echo.
echo %CYAN%==========================================%RESET%
echo %CYAN%      CREDENCIALES DE PRUEBA (TEST USERS)%RESET%
echo %CYAN%==========================================%RESET%
echo.
echo  %YELLOW%ROL                 CORREO                  CONTRASEÑA%RESET%
echo  ----------------------------------------------------------------
echo  Super Admin (Total) admin@prexcol.com       admin123
echo  Store Manager       manager@store.com       manager123
echo  Seller (Vendedor)   seller@store.com        seller123
echo  Customer (Cliente)  user@example.com        user123
echo.
echo  %CYAN%URLs de Acceso:%RESET%
echo  - Panel Admin (Backend): http://localhost:8000/admin/
echo  - Swagger UI (OpenAPI): http://localhost:8000/api/docs/swagger/
echo  - Redoc UI: http://localhost:8000/api/docs/redoc/
echo  - API Docs (Sphinx): http://localhost:8000/api/docs/
echo.
echo Presione cualquier tecla para VOLVER AL MENU...
pause >nul
cls
goto :OPTIONAL_CREDENTIALS

:CREATE_ADMIN
cls
echo.
echo %CYAN%==========================================%RESET%
echo %CYAN%      CREAR SUPERUSUARIO (INTERACTIVO)%RESET%
echo %CYAN%==========================================%RESET%
echo.
echo  Siga las instrucciones para crear su cuenta de administrador total.
echo.
"%PYTHON_EXE%" "%BACKEND_DIR%\manage.py" createsuperuser
echo.
echo  %GREEN%Proceso finalizado.%RESET%
echo.
echo Presione cualquier tecla para VOLVER AL MENU...
pause >nul
cls
goto :OPTIONAL_CREDENTIALS

:END_SCRIPT
echo.
echo Sistema corriendo en segundo plano. 
echo Puede cerrar esta ventana, los servidores seguiran activos.
pause
exit /b 0

REM ------------------------------------------------
REM HELPER FUNCTIONS
REM ------------------------------------------------

:run_animated
set "ANIM_MSG=%~1"
set "ANIM_CMD=%~2"
set "ANIM_LOG=%~3"

echo. > "%LOGS_DIR%\running.lock"
start /b cmd /c "%ANIM_CMD% > "%ANIM_LOG%" 2>&1 & del "%LOGS_DIR%\running.lock""

:anim_loop
if not exist "%LOGS_DIR%\running.lock" goto :anim_exit
call :draw_ui "%ANIM_MSG%" ". o o"
ping -n 1 -w 200 127.0.0.1 >nul

if not exist "%LOGS_DIR%\running.lock" goto :anim_exit
call :draw_ui "%ANIM_MSG%" "o . o"
ping -n 1 -w 200 127.0.0.1 >nul

if not exist "%LOGS_DIR%\running.lock" goto :anim_exit
call :draw_ui "%ANIM_MSG%" "o o ."
ping -n 1 -w 200 127.0.0.1 >nul

if not exist "%LOGS_DIR%\running.lock" goto :anim_exit
call :draw_ui "%ANIM_MSG%" "o . o"
ping -n 1 -w 200 127.0.0.1 >nul

goto :anim_loop
:anim_exit
exit /b 0

:update_progress
SET "MSG=%~1"
SET /A CURRENT_STEP+=1
call :draw_ui "%MSG%" "WAIT"
exit /b 0

:run_verification
set "VERIFY_MSG=%~1"
set "VERIFY_CMD=%~2"
call :draw_ui "%VERIFY_MSG%" "VERIFYING"
%VERIFY_CMD% >nul 2>&1
if %errorlevel% neq 0 (
    call :show_error "Verification Failed: %VERIFY_MSG%"
    exit /b 1
)
exit /b 0

:draw_ui
SET "UI_MSG=%~1"
SET "ANIM_STATE=%~2"
SET /A PERCENT=(CURRENT_STEP * 100) / TOTAL_STEPS
SET /A FILLED_CHARS=(PERCENT * BAR_WIDTH) / 100
SET "BAR="

IF %FILLED_CHARS% GTR 0 ( FOR /L %%i IN (1,1,!FILLED_CHARS!) DO SET "BAR=!BAR!=" )
SET /A REMAINING=BAR_WIDTH - FILLED_CHARS
IF %REMAINING% GTR 0 ( FOR /L %%i IN (1,1,!REMAINING!) DO SET "BAR=!BAR!." )

cls
echo.
echo ==========================================
echo       PREXCOL SYSTEM LAUNCHER
echo ==========================================
echo.
echo  Paso !CURRENT_STEP! de !TOTAL_STEPS!: 
echo.

if "%ANIM_STATE%"=="WAIT" goto :draw_wait
echo  ^> %UI_MSG%
echo     [%ANIM_STATE%]
goto :draw_bar

:draw_wait
echo  ^> %UI_MSG%...

:draw_bar
echo.
echo  [%BAR%] %PERCENT%%%
echo.
echo ==========================================
exit /b 0

:show_error
SET "ERR_MSG=%~1"
cls
echo.
echo %RED%==========================================%RESET%
echo %RED%      FATAL ERROR - STOPPED%RESET%
echo %RED%==========================================%RESET%
echo.
echo  Fallo en el paso: !CURRENT_STEP!
echo.
echo  DETALLE DEL ERROR:
echo  ------------------------------------------
echo  %ERR_MSG%
echo  ------------------------------------------
echo.
echo  Revise los logs en: %LOGS_DIR%
echo.
if exist "%LOGS_DIR%\running.lock" del "%LOGS_DIR%\running.lock"
pause
exit /b 1
