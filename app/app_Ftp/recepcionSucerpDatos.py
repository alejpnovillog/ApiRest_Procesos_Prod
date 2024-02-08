try:
    import gc
    import os
    import platform
    from ftplib import FTP
    from app_Conexion_Iseries_JtOpen.pythonJTOpen import JT400Helper    

    # Clase de configuracion
    from app_Config.config import ConfigurarAplicacion

    # Gestion Registros
    from app_Abstract.gestionRegistros import GestionRegistros

    from fastapi import BackgroundTasks, APIRouter

except Exception as e:
    print(f'Falta algun modulo {e}')


class ConfigurarAplicacionSubmit:

    def __enter__(self):

        api = ConfigurarAplicacion()

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

        print("Inicializando recursos de ConfigurarAplicacionSubmit")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
      
        print("Liberando recursos de ConfigurarAplicacionSubmit")

        if exc_type is not None:
            # Se produjo una excepción dentro del bloque with
            print(f"Se produjo una excepción del tipo {exc_type}: {exc_value}")

            # Puedes hacer algo específico basado en el tipo de excepción
            if issubclass(exc_type, ValueError):
                print("Manejando una excepción de ValueError")

            # También puedes acceder al traceback si es necesario
            if traceback is not None:
                print("Traceback:")
                traceback.print_tb(traceback)

        # Puedes decidir si quieres propagar o suprimir la excepción
        # Si quieres propagar la excepción, devuelve False
        # Si quieres suprimir la excepción, devuelve True
        return True  


class GestionRegistrosSubmit:

    def __enter__(self):

        with ConfigurarAplicacionSubmit as api:

            db = GestionRegistros(ambiente=api.ENV_GX)

            # --------------- Recuperamos el schema del ambiente -----------------------
            schema = db.__getattribute__('instancia_Host_Input_Dict')['schema']

            # --------------- Recuperamos el server del ambiente -----------------------
            server = db.__getattribute__('instancia_Host_Input_Dict')['ip']

            # --------------- Recuperamos el usuario del ambiente ----------------------
            username = db.__getattribute__('instancia_Host_Input_Dict')['usuario']

            # --------------- Recuperar la password del ambiente -----------------------
            pwd = db.__getattribute__('instancia_Host_Input_Dict')['password']


        print("Inicializando recursos de GestionRegistrosSubmit")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
      
        print("Liberando recursos de GestionRegistrosSubmit")

        if exc_type is not None:
            # Se produjo una excepción dentro del bloque with
            print(f"Se produjo una excepción del tipo {exc_type}: {exc_value}")

            # Puedes hacer algo específico basado en el tipo de excepción
            if issubclass(exc_type, ValueError):
                print("Manejando una excepción de ValueError")

            # También puedes acceder al traceback si es necesario
            if traceback is not None:
                print("Traceback:")
                traceback.print_tb(traceback)

        # Puedes decidir si quieres propagar o suprimir la excepción
        # Si quieres propagar la excepción, devuelve False
        # Si quieres suprimir la excepción, devuelve True
        return True  


class FtpSubmit:

    def __enter__(self):

        ftp = FTP()

        print("Inicializando recursos de FtpSubmit")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
      
        print("Liberando recursos de FtpSubmit")

        if exc_type is not None:
            # Se produjo una excepción dentro del bloque with
            print(f"Se produjo una excepción del tipo {exc_type}: {exc_value}")

            # Puedes hacer algo específico basado en el tipo de excepción
            if issubclass(exc_type, ValueError):
                print("Manejando una excepción de ValueError")

            # También puedes acceder al traceback si es necesario
            if traceback is not None:
                print("Traceback:")
                traceback.print_tb(traceback)

        # Puedes decidir si quieres propagar o suprimir la excepción
        # Si quieres propagar la excepción, devuelve False
        # Si quieres suprimir la excepción, devuelve True
        return True  

class JT400HelperSubmit:

    def __enter__(self):


        with GestionRegistrosSubmit as db:

            iprod = JT400Helper(db.server, db.username, db.pwd)

        print("Inicializando recursos de FtpSubmit")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
      
        print("Liberando recursos de FtpSubmit")

        if exc_type is not None:
            # Se produjo una excepción dentro del bloque with
            print(f"Se produjo una excepción del tipo {exc_type}: {exc_value}")

            # Puedes hacer algo específico basado en el tipo de excepción
            if issubclass(exc_type, ValueError):
                print("Manejando una excepción de ValueError")

            # También puedes acceder al traceback si es necesario
            if traceback is not None:
                print("Traceback:")
                traceback.print_tb(traceback)

        # Puedes decidir si quieres propagar o suprimir la excepción
        # Si quieres propagar la excepción, devuelve False
        # Si quieres suprimir la excepción, devuelve True
        return True  



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ASIGNAMOS EL ROUTER PARA OBTENER LA INFORMACION NECESARIA
router = APIRouter()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos el proceso ascincronico en background
async def procesar_archivos():

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Procesamiento General
    try:

        print(f"Proceso iniciado..........")

        with ConfigurarAplicacionSubmit as api:

            with GestionRegistrosSubmit as db:

                with JT400HelperSubmit as iprod:        

                    with FtpSubmit as ftp:        


        # ------------------- recuperamos el ambiente ------------------------------
        # api = ConfigurarAplicacion()
        #db = GestionRegistros(ambiente=api.ENV_GX)

        # --------------- Recuperamos el schema del ambiente -----------------------
        #schema = db.__getattribute__('instancia_Host_Input_Dict')['schema']

        # --------------- Recuperamos el server del ambiente -----------------------
        #server = db.__getattribute__('instancia_Host_Input_Dict')['ip']

        # --------------- Recuperamos el usuario del ambiente ----------------------
        #username = db.__getattribute__('instancia_Host_Input_Dict')['usuario']

        # --------------- Recuperar la password del ambiente -----------------------
        #pwd = db.__getattribute__('instancia_Host_Input_Dict')['password']

        # --------------- Asignamos una instancia del JT400  -----------------------
        #iprod = JT400Helper(server, username, pwd)

        # --------------- Asignamos una instancia del objeto system ----------------
                        #system = iprod.system
            
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # -- Recuperamos la lista de a procesar en Windows
        #if platform.system() == "Windows":

            # - Obtenemos la carpeta de recepcion en Linux    
        #    directorio = api.RECEPCIONPATH_WINDOWS
        #    ruta_destino = f'{api.PROCESADOPATH_WINDOWS}'

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # -- Recuperamos la lista de a procesar en Linux
        #if platform.system() == "Linux":

            # - Obtenemos la carpeta de recepcion en Linux    
        #    directorio = api.RECEPCIONPATH_LINUX
        #    ruta_destino = f'{api.PROCESADOPATH_LINUX}'


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #               nos ubicamos en el directorio
                        os.chdir(api.directorio)            

        # -             Obtenemos los objetos de la carpeta de recepcion
                        lista_archivos_directorios = os.listdir()

                        # Iterar sobre la lista
                        for elemento in lista_archivos_directorios:
                        
                            # - Obtenemos la ruta completa del objeto
                            ruta_completa = os.path.join(api.directorio, elemento)

                            # Verificar si es un directorio
                            if os.path.isdir(api.ruta_completa):
                                print(f"Error {elemento} es un directorio.")

                            # Verificar si es un archivo
                            elif os.path.isfile(api.ruta_completa):
                            
                                # definimos el destino dentro de la iseries    
                                target = f'{api.FTPDIR}{elemento}'

                                # definimos el nombre del archivo de la carpeta local
                                fuente = elemento

                                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
                                # definimos la instancia del FTP 2023-06-23_1698427164.txt
                                #ftp = FTP()

                                try:
                                    # Conectar al servidor FTP
                                    ftp.connect(db.server)

                                    # realizamos el login
                                    ftp.login(db.username, db.pwd)

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
                                    clrpfm = f'CLRPFM FILE({db.schema}/{file})'    
                                    retorno = iprod.GetCmdMsg(clrpfm)

                                print(f'Se ha eliminado los registros de F000000001 {retorno}')

                                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                # Copiamos el archivo de texto en la tabla F000000001
                                retorno = False;

                                while not retorno:
                                    cmdStr = f"CPYFRMIMPF FROMSTMF('{target}') TOFILE({db.schema}/{file}) MBROPT(*REPLACE) RCDDLM(*ALL)"
                                    retorno = iprod.GetCmdMsg(cmdStr)

                                print(f'Copiamos el archivo de texto en la tabla F000000001 {retorno}')

                                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                # Ejecutamos la incorporacion del archivo recibido
                                retorno = False;

                                while not retorno:
                                    pgm = 'F000000001'
                                    execpgm = f"CALL PGM({db.schema}/{pgm}) PARM(('{fuente}')) "    
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
                                    os.rename(ruta_origen, os.path.join(api.ruta_destino, fuente))
                                    print(f"Archivo movido de {ruta_origen} a {api.ruta_destino}")

                                except FileNotFoundError:
                                    print(f"El archivo {ruta_origen} no existe.")

                                except Exception as e:
                                    print(f"Error al mover el archivo: {e}")


        # eliminamos las instancias de los objetos
        #referencias = gc.get_referrers(api)
        #print(f'campo referencia {referencias}')
        #print(f'Hay referencias al objeto api {gc.get_referrers(api)}')

        #del api
        #del db
        #del iprod
        #del system


                            print('El proceso ha finalizado ...............................')

    except Exception as e:
        print(f'Error en el procesamiento  {e}')


# enlace para realizar el procesamiento de archivos
@router.post("/procesar_archivos")
async def endpoint_procesar_archivos(ubicacion_carpeta: str, background_tasks: BackgroundTasks):
    # Agrega la tarea al fondo para ser ejecutada asincrónicamente
    background_tasks.add_task(procesar_archivos)

    # Responde inmediatamente sin esperar a que termine el proceso
    return {"mensaje": "Proceso de archivos iniciado en segundo plano"}
