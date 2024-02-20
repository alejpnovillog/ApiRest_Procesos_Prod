@echo off

set SERVER_URL=http://127.0.0.1:8000
set SCRIPT_PATH=C:\Ruta\Al\Script
set CONDA_ENV=ReflexKuvasz

set MAX_ATTEMPTS=5
set ATTEMPTS=0

:activate_conda
call C:\Ruta\A\Tu\Anaconda3\Scripts\activate.bat %CONDA_ENV%
if errorlevel 1 (
    echo Error: No se pudo activar el entorno Conda.
    exit /b 1
)

:run_server
curl -s --head --connect-timeout 5 --max-time 5 %SERVER_URL% | find "200 OK" > nul
if %errorlevel% neq 0 (
    set /a ATTEMPTS+=1
    echo Intento %ATTEMPTS%: El servidor aún no está en funcionamiento. Iniciando el servidor...
    cd %SCRIPT_PATH%
    start "" python main.py
    timeout /nobreak /t 5 > nul
    goto run_server
) else (
    echo El servidor está en funcionamiento.
    exit /b 0
)
