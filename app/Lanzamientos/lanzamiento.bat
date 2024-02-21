@echo off

REM C:\Users\anovillo\Desktop\ApiRest_Procesos_Prod\ApiRest_Procesos_Prod\app\Lanzamientos\lanzamiento.bat
set SERVER_URL=http://127.0.0.1:8000
set SCRIPT_PATH=C:\Users\anovillo\Desktop\ApiRest_Procesos_Prod\ApiRest_Procesos_Prod\app\
set CONDA_ENV=ReflexKuvasz
set PGM=C:\ProgramData\anaconda3\Scripts\activate.bat

set MAX_ATTEMPTS=5
set ATTEMPTS=0

REM activate_conda
call %PGM% %CONDA_ENV%

if errorlevel 1 (
    echo Error: No se pudo activar el entorno Conda.
    exit /b 1
)
REM NOS COLOCAMOS EN EL DIRECTORIO DEL SERCIVIO DE API
cd %SCRIPT_PATH%

REM LEVANTAMOS EL SERVIDOR
start "Servidor Api Procesos" python main.py

REM SALIMOS DE LA VENTANA DEL CMD
exit













