try:

    import os
    import platform
    from ftplib import FTP
    from app_Conexion_Iseries_JtOpen.pythonJTOpen import JT400Helper    

    # Clase de configuracion
    from app_Config.config import ConfigurarAplicacion

    # Gestion Registros
    from app_Abstract.gestionRegistros import GestionRegistros


except Exception as e:
    print(f'Falta algun modulo {e}')

# 2023-07-04_1698427086.txt


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Procesamiento General
try:

    # ------------------- recuperamos el ambiente ------------------------------
    api = ConfigurarAplicacion()
    db = GestionRegistros(ambiente=api.ENV_GX)

    # --------------- Recuperamos el schema del ambiente -----------------------
    schema = db.__getattribute__('instancia_Host_Input_Dict')['schema']

    # --------------- Recuperamos el server del ambiente -----------------------
    server = db.__getattribute__('instancia_Host_Input_Dict')['ip']

    # --------------- Recuperamos el usuario del ambiente ----------------------
    username = db.__getattribute__('instancia_Host_Input_Dict')['usuario']

    # --------------- Recuperar la password del ambiente -----------------------
    pwd = db.__getattribute__('instancia_Host_Input_Dict')['password']

    # --------------- Asignamos una instancia del JT400  -----------------------
    iprod = JT400Helper(server, username, pwd)

    # --------------- Asignamos una instancia del objeto system ----------------
    system = iprod.system

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # -- definimos la lista de los archivos a procesar que contiene el 
    # diccionario con los elementos rutacompleta y elemento
    lista_procesar = list()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # -- Recuperamos la lista de a procesar en Windows
    if platform.system() == "Windows":
        
        # - Obtenemos la carpeta de recepcion en Linux    
        directorio = api.RECEPCIONPATH_WINDOWS
        ruta_destino = f'{api.PROCESADOPATH_WINDOWS}'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # -- Recuperamos la lista de a procesar en Linux
    if platform.system() == "Linux":

        # - Obtenemos la carpeta de recepcion en Linux    
        directorio = api.RECEPCIONPATH_LINUX
        ruta_destino = f'{api.PROCESADOPATH_LINUX}'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # nos ubicamos en el directorio
    os.chdir(directorio)            

    # - Obtenemos los objetos de la carpeta de recepcion
    lista_archivos_directorios = os.listdir()

    # Iterar sobre la lista
    for elemento in lista_archivos_directorios:

        # - Obtenemos la ruta completa del objeto
        ruta_completa = os.path.join(directorio, elemento)

        # Verificar si es un directorio
        if os.path.isdir(ruta_completa):
            print(f"Error {elemento} es un directorio.")

        # Verificar si es un archivo
        elif os.path.isfile(ruta_completa):

            # definimos el destino dentro de la iseries    
            target = f'{api.FTPDIR}{elemento}'

            # definimos el nombre del archivo de la carpeta local
            fuente = elemento

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
            # definimos la instancia del FTP 2023-06-23_1698427164.txt
            ftp = FTP()

            try:
                # Conectar al servidor FTP
                ftp.connect(server)

                # realizamos el login
                ftp.login(username, pwd)

                # Establecer el tipo de transferencia en ASCII (para archivos de texto)
                ftp.voidcmd('TYPE A')

                # Abrir el archivo local en modo de lectura binaria y especificar la codificación
                with open(fuente, 'rb') as file:

                    # Subir el archivo al servidor en modo ASCII
                    ftp.storlines(f'STOR {target}', file)

                print(f"Archivo {fuente} subido con éxito a {target}")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                # Restablecer el tipo de transferencia a binario (por defecto)
                ftp.voidcmd('TYPE I')

                # Cerrar la conexión FTP
                ftp.quit()

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Eliminamos los registros de F000000001
            retorno = False;

            while not retorno:
                file = 'F000000001'    
                clrpfm = f'CLRPFM FILE({schema}/{file})'    
                retorno = iprod.GetCmdMsg(clrpfm)

            print(f'Se ha eliminado los registros de F000000001 {retorno}')

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Copiamos el archivo de texto en la tabla F000000001
            retorno = False;

            while not retorno:
                cmdStr = f"CPYFRMIMPF FROMSTMF('{target}') TOFILE({schema}/{file}) MBROPT(*REPLACE) RCDDLM(*ALL)"
                retorno = iprod.GetCmdMsg(cmdStr)

            print(f'Copiamos el archivo de texto en la tabla F000000001 {retorno}')

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Ejecutamos la incorporacion del archivo recibido
            retorno = False;

            while not retorno:
                pgm = 'F000000001'
                execpgm = f"CALL PGM({schema}/{pgm}) PARM(('{fuente}')) "    
                retorno = iprod.GetCmdMsg(execpgm)

            print(f'Ejecutamos la incorporacion del archivo recibido {retorno}')

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Eliminamos el archvivo del IFS
            retorno = False;

            while not retorno:
                cmdDelFile = f"DEL OBJLNK('{target}')"
                retorno = iprod.GetCmdMsg(cmdDelFile)

            print(f'Eliminamos el archvivo del IFS {retorno}')


            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Rutas de los archivos y carpetas
            ruta_origen = f'{ruta_completa}'

            # Mover el archivo
            try:
                os.rename(ruta_origen, os.path.join(ruta_destino, fuente))
                print(f"Archivo movido de {ruta_origen} a {ruta_destino}")

            except FileNotFoundError:
                print(f"El archivo {ruta_origen} no existe.")

            except Exception as e:
                print(f"Error al mover el archivo: {e}")


except Exception as e:
    print(f'Error en el procesamiento  {e}')

