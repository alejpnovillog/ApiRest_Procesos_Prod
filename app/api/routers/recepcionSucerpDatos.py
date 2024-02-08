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



# Definimos la clase para manejar los recursos del contexto del proceso
class ConfigurarAplicacionSubmit:

    # definimos la funcion de inicializacion
    def __enter__(self):

        try:

            # asignamos una instancia de FTP    
            self.ftp = FTP()

            # asignamos una instancia de ConfigurarAplicacion
            self.api = ConfigurarAplicacion()
            
            # asignamos una instancia de GestionRegistros
            self.db = GestionRegistros(ambiente = self.api.ENV_GX)        

            # -- Recuperamos la lista de a procesar en Windows
            if platform.system() == "Windows":

                # - Obtenemos la carpeta de recepcion en Linux    
                self.directorio = self.api.RECEPCIONPATH_WINDOWS
                self.ruta_destino = f'{self.api.PROCESADOPATH_WINDOWS}'


            # -- Recuperamos la lista de a procesar en Linux
            if platform.system() == "Linux":

                # - Obtenemos la carpeta de recepcion en Linux    
                self.directorio = self.api.RECEPCIONPATH_LINUX
                self.ruta_destino = f'{self.api.PROCESADOPATH_LINUX}'



            # --------------- Recuperamos el schema del ambiente -----------------------
            self.schema = self.db.__getattribute__('instancia_Host_Input_Dict')['schema']

            # --------------- Recuperamos el server del ambiente -----------------------
            self.server = self.db.__getattribute__('instancia_Host_Input_Dict')['ip']

            # --------------- Recuperamos el usuario del ambiente ----------------------
            self.username = self.db.__getattribute__('instancia_Host_Input_Dict')['usuario']

            # --------------- Recuperar la password del ambiente -----------------------
            self.pwd = self.db.__getattribute__('instancia_Host_Input_Dict')['password']

            self.iprod = JT400Helper(self.server, self.username, self.pwd)        

            self.target = ''

            self.fuente = ''

            # --------------- Comando de CLRPFM 
            self.file = 'F000000001'    
            self.clrpfm = f'CLRPFM FILE({self.schema}/{self.file})'    



            print("Inicializando recursos de ConfigurarAplicacionSubmit")

        except Exception as e:
            print(f"Error al inicializar recursos en ConfigurarAplicacionSubmit: {e}")

        return self

    # definimos la funcion de la finalizacion de la clase
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

        # definimos el ambiente de ejecucion
        with ConfigurarAplicacionSubmit() as api:

            # nos ubicamos en el directorio
            os.chdir(api.directorio)            

            # Obtenemos los objetos de la carpeta de recepcion
            lista_archivos_directorios = os.listdir()

            # Iterar sobre la lista
            for elemento in lista_archivos_directorios:
            
                # - Obtenemos la ruta completa del objeto
                ruta_completa = os.path.join(api.directorio, elemento)

                # Verificar si es un directorio
                if os.path.isdir(ruta_completa):
                    print(f"Error {elemento} es un directorio.")

                # Verificar si es un archivo
                elif os.path.isfile(ruta_completa):
                    
                    # definimos el destino dentro de la iseries    
                    api.target = f'{api.api.FTPDIR}{elemento}'
                    
                    # definimos el nombre del archivo de la carpeta local
                    api.fuente = elemento

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # definimos la instancia del FTP 2023-06-23_1698427164.txt

                    try:
                        # Conectar al servidor FTP
                        api.ftp.connect(api.server)
                        
                        # realizamos el login
                        api.ftp.login(api.username, api.pwd)

                        # Establecer el tipo de transferencia 
                        # en ASCII (para archivos de texto)
                        api.ftp.voidcmd('TYPE A')

                        # Abrir el archivo local en modo de 
                        # lectura binaria y especificar la codificación
                        with open(api.fuente, 'rb') as file:
                        
                            # Subir el archivo al servidor en modo ASCII
                            api.ftp.storlines(f'STOR {api.target}', file)

                        print(f"Archivo {api.fuente} subido con éxito a {api.target}")

                    except Exception as e:
                        print(f"Error: {e}")

                    finally:
                        # Restablecer el tipo de 
                        # transferencia a binario (por defecto)
                        api.ftp.voidcmd('TYPE I')

                        # Cerrar la conexión FTP
                        api.ftp.quit()

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Eliminamos los registros de F000000001
                    retorno = False;

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(api.clrpfm)

                    print(f'Se ha eliminado los registros de F000000001 {retorno}')

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Copiamos el archivo de texto en la tabla F000000001
                    retorno = False;
                    cpyfrmimpf = f"CPYFRMIMPF FROMSTMF('{api.target}') TOFILE({api.schema}/{api.file}) MBROPT(*REPLACE) RCDDLM(*ALL)"

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(cpyfrmimpf)

                    print(f'Copiamos el archivo de texto en la tabla F000000001 {retorno}')

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Ejecutamos la incorporacion del archivo recibido
                    retorno = False;
                    execpgm = f"CALL PGM({api.schema}/{api.pgm}) PARM(('{api.fuente}')) "    

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(execpgm)

                    print(f'Ejecutamos la incorporacion del archivo recibido {retorno}')

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Eliminamos el archvivo del IFS
                    retorno = False;
                    cmdDelFile = f"DEL OBJLNK('{api.target}')"

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(cmdDelFile)

                    print(f'Eliminamos el archvivo del IFS {retorno}')

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Rutas de los archivos y carpetas
                    ruta_origen = f'{ruta_completa}'

                    # Mover el archivo a la carpeta de archivos procesados
                    try:
                        os.rename(ruta_origen, os.path.join(api.ruta_destino, api.fuente))
                        print(f"Archivo movido de {ruta_origen} a {api.ruta_destino}")

                    # si no encuentra el archivo    
                    except FileNotFoundError:
                        print(f"El archivo {ruta_origen} no existe.")

                    # si hay otro error
                    except Exception as e:
                        print(f"Error al mover el archivo: {e}")


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
