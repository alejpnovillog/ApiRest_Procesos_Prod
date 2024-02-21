# APLICACION DE API-REST DE PROCESOS


## INSTALACION DEL DRIVER ODBC EN UN SISTEMA OPERATIVO LINUX

1. Documentación del paquete iaccess

```
https://github.com/IBM/ibmi-oss-docs


```

2. Actualización del instalador de paquetes de Linux

```
sudo apt-get update

```

3. Instalación de los paquetes de Odbc

```
sudo apt-get install unixodbc unixodbc-dev

```

4. Instalación del paquete IBM i Access ODBC Installation

```
sudo curl https://public.dhe.ibm.com/software/ibmi/products/odbc/debs/dists/1.1.0/ibmi-acs-1.1.0.list

sudo tee /etc/apt/sources.list.d/ibmi-acs-1.1.0.list

```

5. Verificación de la ubicación de los archivos odbc

```
odbcinst -j

```

6. Configura el archivo /etc/odbcinst.ini

```
[iSeries Access ODBC Driver]
Description=iSeries Access ODBC Driver
Driver=/usr/lib/x86_64-linux-gnu/libodbc.so

[IBM i Access ODBC Driver]
Description=IBM i Access for Linux ODBC Driver
Driver=/opt/ibm/iaccess/lib/libcwbodbc.so
Setup=/opt/ibm/iaccess/lib/libcwbodbcs.so
Driver64=/opt/ibm/iaccess/lib64/libcwbodbc.so
Setup64=/opt/ibm/iaccess/lib64/libcwbodbcs.so
Threading=0
DontDLClose=1
UsageCount=1

[IBM i Access ODBC Driver 64-bit]
Description=IBM i Access for Linux 64-bit ODBC Driver
Driver=/opt/ibm/iaccess/lib64/libcwbodbc.so
Setup=/opt/ibm/iaccess/lib64/libcwbodbcs.so
Threading=0
DontDLClose=1
UsageCount=1


```

7. Configura el archivo /home/anovillo/.odbc.ini

```
[QDNS_db2]
Description   = My AS400 Connection
Driver        = IBM i Access ODBC Driver
System        = PUB400.COM
UID           = anovillo
PWD           = macs6259
Database      = ANOVILLO1

```

## DESINSTALAR DEL DRIVER ODBC EN UN SISTEMA OPERATIVO LINUX

```
sudo apt-get remove unixodbc unixodbc-dev

sudo rm /etc/odbcinst.ini /etc/odbc.ini

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
Pub400 = {'server': 'iseriesLinux', 'ip': 'PUB400.COM', 'usuario': 'anovillo', 'password': 'macs6259', 'database': 'PUB400', 'schema': 'anovillo1', 'strcon': 'db2:pyodbc://driver={drive};System={host};Database={Db};uid={uid};pwd={pwd};dbq={dbq}'} 

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

## CONFIGURACION DE LAS EXTENCIONES DEL VSCODE

 1. autoDocstring - Python Docstring Generator (Instalar si no lo esta)

 2. Bearded Theme (Instalar si no lo esta)

 3. Bootstrap 5 Quick Snippets (Instalar si no lo esta)

 4. CL (Instalar si no lo esta)

 5. COBOL (Instalar si no lo esta)

 6. Code for IBM i (Instalar si no lo esta)

 7. Code for IBM i Walkthroughs (Instalar si no lo esta)

 8. CodeLLDB (Instalar si no lo esta)

 9. Db2 for IBM i (Instalar si no lo esta)

10. Draw.io Integration (Instalar si no lo esta)

11. Error Lens (Instalar si no lo esta)

12. HTML Preview (Instalar si no lo esta)

13. IBM i Debug (Instalar si no lo esta)

14. IBM i Development Pack (Instalar si no lo esta)

15. IBM i Notebooks (Instalar si no lo esta)

16. IBM i Renderer (Instalar si no lo esta)

17. IBM i Snippets (Instalar si no lo esta)

18. IBM i SQL (Instalar si no lo esta)

19. IBM i system debugger (Instalar si no lo esta)

20. IBMi Languages (Instalar si no lo esta)

21. IntelliCode (Instalar si no lo esta)

22. IntelliCode API Usage Examples (Instalar si no lo esta)

23. Jinja (Instalar si no lo esta)

24. Jupyter (Instalar si no lo esta)

25. Jupyter Cell Tags (Instalar si no lo esta)

26. Jupyter Keymap (Instalar si no lo esta)

27. Jupyter Notebook Renderers (Instalar si no lo esta)

28. Jupyter Slide Show (Instalar si no lo esta)

29. jupyter-notebook-vscode (Instalar si no lo esta)

30. Markdown PDF (Instalar si no lo esta)

31. Markdown Preview Enhanced (Instalar si no lo esta)

32. Notepad++ keymap (Instalar si no lo esta)

33. PostgreSQL (Instalar si no lo esta)

34. PostgreSQL (Instalar si no lo esta)

35. Pylance (Instalar si no lo esta)

36. Pytest IntelliSense (Instalar si no lo esta)

37. Python (Instalar si no lo esta)

38. Python Debugger (Instalar si no lo esta)

39. Python Environment Manager (Instalar si no lo esta)

40. Python Extended (Instalar si no lo esta)

41. Python Extension Pack (Instalar si no lo esta)

42. Remote - SSH (Instalar si no lo esta)

43. Remote - SSH: Editing Configuration Files (Instalar si no lo esta)

44. Remote Explorer (Instalar si no lo esta)

45. RPG (Instalar si no lo esta)

46. RPGLE (Instalar si no lo esta)

47. RPGLE Free (Instalar si no lo esta)

48. RRPG (Instalar si no lo esta)

49. rust-analyzer (Instalar si no lo esta)

50. Spanish Language Pack for Visual Studio Code (Instalar si no lo esta)

51. SSH Client (Instalar si no lo esta)

52. SSH Terminal (Instalar si no lo esta)

53. TODO Highlight (Instalar si no lo esta)

54. VS Code Jupyter Notebook Previewer (Instalar si no lo esta)

55. vscode-pdf (Instalar si no lo esta)

56. **Material Icon Theme** (Instalar si no lo esta)

## VALORES QUE SE DEBE CONFIGURAR EN app_Config.config (ConfigurarAplicacion)

 1. **JVMPATH_WINDOWS** Es la ubicación de la java virtual machine en el entorno Windows

 2. **JVMPATH_LINUX** Es la ubicación de la java virtual machine en el entorno Linux

 3. **ADDCLASSPATH_WINDOWS** Es la ubicación de las clases de JtOpen en el entorno Windows

 4. **ADDCLASSPATH_LINUX** Es la ubicación de las clases de JtOpen en el entorno Linux

 5. **JARPATH_WINDOWS** Es la ubicación de la clase de jt400.jar en el entorno Windows

 6. **JARPATH_LINUX** Es la ubicación de la clase de jt400.jar en el entorno Linux
 
 7. **RECEPCIONPATH_WINDOWS** Es la ubicación de los archivos a procesar de SUCERP en el entorno Windows

 8. **PROCESADOPATH_WINDOWS** Es la ubicación de los archivos a procesados de SUCERP en el entorno Windows

 9. **RECEPCIONPATH_LINUX** Es la ubicación de los archivos a procesar de SUCERP en el entorno Linux

10. **PROCESADOPATH_LINUX** Es la ubicación de los archivos a procesados de SUCERP en el entorno Linux

11. **FTPDIR** Es la ubicación dentro del sistema IFS de la Iseries

12. **DIR_PROYECTO_WINDOWS** Es la ubicación del proyecto en el entorno Windows

13. **DIR_PROYECTO_LINUX** Es la ubicación del proyecto en el entorno Linux

14. **SERVER_HTTP_DEVELOPMENT** Es la ubicación del server en el ambiente de desarrollo

15. **SERVER_HTTP_PRODUCTION** Es la ubicación del server en el ambiente de producción

16. **VALIDATOR** Es el conector en SQLLITE utilizado para validaciones

17. **POSTGRESQL_MATANZA** Es el conector en POSTGRESQL para el esquema Matanza

18. **POSTGRESQL_GXPROD** Es el conector en POSTGRESQL para el esquema Gxprod

19. **MYSQL_MATANZA** Es el conector en MYSQL para el esquema Matanza

20. **MYSQL_GXPROD** Es el conector en MYSQL para el esquema Gxprod

21. **TEST_MATANZA** Es el conector en ISERIES (Municipalidad) para el esquema Matanza Test

22. **PROD_MATANZA** Es el conector en ISERIES (Municipalidad) para el esquema Matanza Prod

23. **TEST_ISERIES** Es el conector en ISERIES (Municipalidad) para el esquema Gxprod Test

24. **PROD_ISERIES** Es el conector en ISERIES (Municipalidad) para el esquema Gxprod Prod

25. **PUB400_LIB** Es el nombre de la iseries publica

26. **ENV_SOURCE** Es el ambiente fuente de motor de bases de datos

27. **ENV_TARGET** Es el ambiente destino de motor de bases de datos

28. **ENV_MATANZA** Es el ambiente para el esquema Matanza

29. **ENV_GX** Es el ambiente produccion para el esquema Gxprod

30. **ENV_GX_TEST** Es el ambiente test para el esquema Gxprod

31. **ENV_DDS** Es el ambiente de estructura de archivos DDS

32. **ENV_SQ** Es el ambiente SQL 

33. **ENV_LABEL_ON** Son los ambientes que pueden usar le sentencia SQL Text

34. **WRK_RECORDS** Son la cantidad de registros que se cargan en un panel WRK

35. **DIR_PATH_IMAGENES_WINDOWS** Es la ruta donde se albergan las imagenes en entorno Windows

36. **DIR_PATH_ERRORES_WINDOWS** Es la ruta donde se encuentran los erroes en el entorno Windows

37. **DIR_PATH_HOST_WINDOWS** Es la ruta donde se encuntra el host en el ambiente Windows

38. **DIR_PATH_METODOS_WINDOWS** Es la ruta donde se encuentra los metodos en el ambiente Windows

39. **DIR_PATH_TEMPLATES_WINDOWS** Es la ruta donde se encuentra los templates en el ambiente Windows

40. **DIR_PATH_IMAGENES_LINUX** Es la ruta donde se albergan las imagenes en entorno Windows

41. **DIR_PATH_ERRORES_LINUX** Es la ruta donde se encuentran los erroes en el entorno Linux

42. **DIR_PATH_HOST_LINUX** Es la ruta donde se encuntra el host en el ambiente Linux

43. **DIR_PATH_METODOS_LINUX** Es la ruta donde se encuentra los metodos en el ambiente Linux

44. **DIR_PATH_TEMPLATES_LINUX** Es la ruta donde se encuentra los templates en el ambiente Linux

45. **LISTA_TABLAS** Es el diccionario donde se encuentran las definiciones de configuracion de las tablas




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
conda env export --name ReflexKuvasz --no-build -c conda-forge > environmentWindows.yml

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










