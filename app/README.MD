# APLICACION DE API-REST DE PROCESOS


## INSTALACION DEL DRIVER ODBC EN UN SISTEMA OPERATIVO LINUX

1. Actualización del instalador de paquetes de Linux

```
sudo apt-get update

```

2. Instalación de los paquetes de Odbc

```
sudo apt-get install unixodbc unixodbc-dev

```

3. Configura el archivo odbcinst.ini

```
[iSeries Access ODBC Driver]
Description = iSeries Access ODBC Driver
Driver      = /usr/lib/x86_64-linux-gnu/libodbc.so

```

4. Configura el archivo odbc.ini

```
[QDNS_db2]
Description   = My AS400 Connection
Driver        = iSeries Access ODBC Driver
System        = PUB400.COM
UID           = anovillo
PWD           = macs6259
Database      = ANOVILLO1

```

## INSTALACION DEL STRING DE CONEXION

1. Parámetros de la configuración del string de conexión

```
con.host = 'Pub400'
con.serverhost = 'db2'
con.iphost = 'PUB400.COM'
con.usuariohost = 'anovillo'
con.passhost = 'macs6259'
con.schemahost = 'anovillo1'
con.databasehost = 'PUB400'
con.accion = 'add'
con.add_host()

```

2. El valor generado por el script actualizaConexion.py

```
Pub400 = {'server': 'db2', 'ip': 'PUB400.COM', 'usuario': 'anovillo', 'password': 'macs6259', 'database': 'PUB400', 'schema': 'anovillo1', 'strcon': 'db2:pyodbc://DSN=QDSN_db2;UID=anovillo;PWD=macs6259;'} 

```

## ACTUALIZACION DE ANACONDA

1. Verificar la versión de **anaconda**

``` 
conda --version

```

2. Actualización de **conda-forge**

``` 
conda update -n base -c conda-forge conda 

```

3. Configurar **conda-forge**

``` 
conda config --add channels conda-forge 

```

4. Actualización de el propio **conda**

``` 
conda update conda  

```

5. Actualización **anaconda**

``` 
conda update anaconda  

```

6. Actualizar todos los paquetes

``` 
conda update nombre_del_paquete  

```

7. Verificar la versión de **anaconda** nuevamente

``` 
conda --version  

```



## INSTALACION DEL AMBIENTE DE ANACONDA PARA LA APLICACION API-REST

1. Creación de la carpeta 

``` 
ApiRest-Procesos 

```

2. Copiar la aplicacion dentro de la carpeta

3. Generacion del archivo environment.yml

``` 
conda env export --no-builds > environment.yml 

```

4. Generación para un entorno windows

``` 
conda env export --from-history --platform win-64 --no-build -c conda-forge > environment.yml  

```

5. Una vez generado el archivo environment.yml modificar el name con 

``` 
ApiRestProcesos 

```

6. Primero debemos crear el ambiente donde se ejecutara 


```

conda env create -f environment.yml

```

7. Generacion del .exe con el comando pyinstaler del script main.py


## INVOCACION DEL PROCESO DE RECEPCION DE DATOS DE SUCERP

1. El link de invocación del preceso de recepción de datos Sucerp

``` http://mlmsrv:8000/recepciondatossucerp/{uid}/{token}```

2. Una vez realizada la invocacion el usuario recibira una email con la confirmación del lanzamiento del proceso

3. Una vez finalizado el proceso se el usuario recibira un email con el detalle de los archivos procesados




## LONGITUD DE REGISTROS


1. Tipo de registro E0 ENCABEZADO -  ENCABEZADO

>- Longitud de registro 86

2. Tipo de registro C1 - C  ALTAI00002 - ALTAIMPOSITIVA                    

>- Longitud de registro                                                             2.385

3. Tipo de registro C1 - T  ALTAI00001 - ALTAIMPOSITIVATITULAR             

>- Longitud de registro 648

4. Tipo de registro C2 - C  BAJAI00002 - BAJAIMPOSITIVA                

>- Longitud de registro 2.037

5. Tipo de registro C2 - T  BAJAI00001 - BAJAIMPOSITIVATITULAR         

>- Longitud de registro 648

6. Tipo de registro C3 - C  IMPUE00001 - IMPUESTOSELLOS                  

>- Longitud de registro 2.317

7. Tipo de registro C3 - P  IMPUE00002 - IMPUESTOSELLOSPARTES            

>- Longitud de registro 897

8. Tipo de registro C3 - T  IMPUE00003 - IMPUESTOSELLOSPARTESTIPOTRAMITE 

>- Longitud de registro 475

9. Tipo de registro C4 -    IMPUE00004 - IMPUESTOAUTOMOTOR               

>- Longitud de registro 891

10. Tipo de registro C5 - C INFOR00001 - INFORMACIONVEHICULO               

>- Longitud de registro 994

11. Tipo de registro C5 - T INFOR00002 - INFORMACIONVEHICULOTITULAR        

>- Longitud de registro 652

12. Tipo de registro C6 - C CAMBI00003 - CAMBIOTITULARIDAD             

>- Longitud de registro 2.187

13. Tipo de registro C6 - T CAMBI00002 - CAMBIOTITULARIDADTITULAR      

>- Longitud de registro 652

14. Tipo de registro C7 -   INFOR00003 - INFORMACIORADICACION              

>- Longitud de registro 700

15. Tipo de registro C8 - C ANULA00001 - ANULACIONTRAMITESSELLOS           

>- Longitud de registro 1.303

16. Tipo de registro C8 - D ANULA00002 - ANULACIONTRAMITESSELLOSDETALLE    

>- Longitud de registro 610

17. Tipo de registro C9 - C TRAMI00002 - TRAMITESGENERALES            

>- Longitud de registro 887

18. Tipo de registro C9 - T TRAMI00001 - TRAMITESGENERALESTITULARES   

>- Longitud de registro 652

19. Tipo de registro P0 -   PIE - PIE                        

>- Longitud de registro 72







1. INFOR00001 Tabla INFORMACIONVEHICULO tabla temporal

>- Longitud registro 952

2. INFOR00002 Tabla INFORMACIONVEHICULOTITULAR tabla temporal

>- Longitud registro 634

3. ALTAI00001 Tabla ALTAIMPOSITIVA

>- Longitud registro      

4. ALTAI00002 Tabla ALTAIMPOSITIVATITULAR

>- Longitud registro

5. ANULA00001 Table ANULACIONTRAMITESSELLOS

6. ANULA00002 Tabla ANULACIONTRAMITESSELLOSDETALLE

7. AUTOM00001 Tabla AUTOMOTORCABECERA

8. AUTOM00002 Tabla AUTOMOTORDETALLE

9. 










