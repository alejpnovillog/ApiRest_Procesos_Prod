#!/bin/bash
# debemos dar autorizacion la primera vez al script con el comando
# chmod +x nombre_del_script.sh
# y lo ejecutamos en la carpeta donde esta el script con el comando
#./lanzamiento.sh
SERVER_URL=http://127.0.0.1:8000
SCRIPT_PATH=/home/anovillo/Escritorio/ApiRest_Procesos_Prod/ApiRest_Procesos_Prod/app/
CONDA_ENV=ReflexKuvasz

max_attempts=5
attempts=0

MAX_ATTEMPTS=5
ATTEMPTS=0

# Activamos el ambiente 
source /home/anovillo/anaconda3/envs/ReflexKuvasz/bin/activate

#cd $SCRIPT_PATH
#python main.py


while true; do
    curl -s --head --connect-timeout 5 --max-time 5 "$SERVER_URL" | grep "200 OK" > /dev/null
    if [ $? -ne 0 ]; then
        ((ATTEMPTS++))
        echo "Intento $ATTEMPTS: El servidor aún no está en funcionamiento. Iniciando el servidor..."
        cd $SCRIPT_PATH
        python main.py &
        sleep 5
        echo "El servidor está en funcionamiento."
        exit 0

    else
        echo "El servidor está en funcionamiento."
        exit 0
    fi
done

