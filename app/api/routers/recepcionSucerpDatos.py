# http://localhost:8000/dgtic/procesarSucerp
# CALL PGM(ANOVILLO1/F000000001) PARM(('2023-06-08_1698427125.txt' (*CHAR 120)) (2 (*INT 4)))
# CALL PGM(ANOVILLO1/F000000001) PARM(('2023-06-08_1698427125.txt') (2))
                                                               
try:

    import psutil
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart    
    import html
    import os
    import platform
    import jpype
    import datetime

    from ftplib import FTP
    from app_Conexion_Iseries_JtOpen.pythonJTOpen import JT400Helper    

    # Clase de configuracion
    from app_Config.config import ConfigurarAplicacion

    # Gestion Registros
    from app_Abstract.gestionRegistros import GestionRegistros

    from fastapi import BackgroundTasks, APIRouter
    from fastapi.responses import HTMLResponse



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

            # -- Recuperamos la lista de a procesar en Windows
            if platform.system() == "Windows":
                # nos ubicamos en el directorio del proyecto para usar la gestion db
                os.chdir(self.api.DIR_PROYECTO_WINDOWS)            

            # -- Recuperamos la lista de a procesar en Linux
            if platform.system() == "Linux":
                # nos ubicamos en el directorio del proyecto para usar la gestion db
                os.chdir(self.api.DIR_PROYECTO_LINUX)            

            # asignamos una instancia de GestionRegistros
            self.db = GestionRegistros(ambiente = self.api.ENV_GX)        

            # --------------- Recuperamos el schema del ambiente -----------------------
            self.schema = self.db.__getattribute__('instancia_Host_Input_Dict')['schema']

            # --------------- Recuperamos el server del ambiente -----------------------
            self.server = self.db.__getattribute__('instancia_Host_Input_Dict')['ip']

            # --------------- Recuperamos el usuario del ambiente ----------------------
            self.username = self.db.__getattribute__('instancia_Host_Input_Dict')['usuario']

            # --------------- Recuperar la password del ambiente -----------------------
            self.pwd = self.db.__getattribute__('instancia_Host_Input_Dict')['password']

            # --------------- Tablas de control de los archivos recibidos desde sucerp
            self.objetoRecepcionArchivos = self.db.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_RECEPCIONARCHIVOS']['objeto'])            
            self.objetoProcesoImportacionExportacion = self.db.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROCESOIMPORTACIONEXPORTACION']['objeto'])            

            # --------------- asignamos una instancia de la clase JT400Helper para usar el Os400
            self.iprod = JT400Helper(self.server, self.username, self.pwd)        

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

            # definimos el nombre del archivo target
            self.target = ''

            # definimos el nombre del archivo fuente
            self.fuente = ''

            # --------------- Comando de CLRPFM 
            self.file = 'F000000001'
            self.pgm  = self.file    
            self.clrpfm = f'CLRPFM FILE({self.schema}/{self.file})'    

            self.logdict = dict()

            #print("Inicializando recursos de ConfigurarAplicacionSubmit")

        except Exception as e:
            print(f"Error al inicializar recursos en ConfigurarAplicacionSubmit: {e}")

        return self

    # definimos la funcion de la finalizacion de la clase
    def __exit__(self, exc_type, exc_value, traceback):
      
        del self.db
        #print("Liberando recursos de ConfigurarAplicacionSubmit")

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

        # Iniciar la aplicación
        with ConfigurarAplicacionSubmit() as api:

            # nos ubicamos en el directorio
            os.chdir(api.directorio)            

            # Obtenemos los objetos de la carpeta de recepcion
            lista_archivos_directorios = os.listdir()

            # definimos el contador para los ciclos de la transferencia
            ciclo = 0

            elemento = 'Recepcion SUCERP'

            ciclo += 1
            api.logdict[f'{elemento} - paso({ciclo})'] = f"Proceso iniciado.........."

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

                        ciclo += 1
                        api.logdict[f'{elemento} - paso({ciclo})'] = f"Archivo {api.fuente} subido con éxito a {api.target}"


                    except Exception as e:
                        print(f"Error: {e}")

                    finally:
                        # Restablecer el tipo de 
                        # transferencia a binario (por defecto)
                        api.ftp.voidcmd('TYPE I')

                        # Cerrar la conexión FTP
                        api.ftp.quit()

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Generamos el registro para RECEPCIONARCHIVOS
                    registro = {}
                    registro['archivonombre']    = api.fuente
                    registro['archivousercrt']   = api.username
                    registro['archivoprocesado'] = datetime.datetime.now()
                    retorno = False

                    while not retorno:
                        api.db.campos.clear()
                        retorno = api.db.add_Dal(api.objetoRecepcionArchivos, **registro)

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Eliminamos los registros de F000000001
                    retorno = False;

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(api.clrpfm)

                    ciclo += 1
                    api.logdict[f'{elemento} - paso({ciclo})'] = f'Se ha eliminado los registros de F000000001 {retorno}'

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Copiamos el archivo de texto en la tabla F000000001
                    retorno = False;
                    cpyfrmimpf = f"CPYFRMIMPF FROMSTMF('{api.target}') TOFILE({api.schema}/{api.file}) MBROPT(*REPLACE) RCDDLM(*ALL)"

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(cpyfrmimpf)

                    ciclo += 1
                    api.logdict[f'{elemento} - paso({ciclo})'] = f'Copiamos el archivo de texto en la tabla F000000001 {retorno}'

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Generamos el registro para PROCESOIMPORTACIONEXPORTACION
                    registro = {}
                    registro['procesocodigotabla']        = 1
                    registro['procesonombretabla']        = api.fuente
                    registro['procesotransferencia']      = 'S'
                    registro['procesofechatransferencia'] = datetime.datetime.now()
                    registro['procesobasedatos']          = 'S'
                    registro['procesofechabasedatos']     = datetime.datetime.now()
                    registro['procesoaccion']             = None
                    retorno = False

                    while not retorno:
                        api.db.campos.clear()
                        retorno = api.db.add_Dal(api.objetoProcesoImportacionExportacion, **registro)

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Ejecutamos la incorporacion del archivo recibido
                    retorno = False;
                    execpgm = f"CALL PGM({api.schema}/{api.pgm}) PARM(('{api.fuente}' (*CHAR 120)) ('{api.db.ultimoid}'))"    

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(execpgm)

                    ciclo += 1
                    api.logdict[f'{elemento} - paso({ciclo})'] = f'Ejecutamos la incorporacion del archivo recibido {retorno}'

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Eliminamos el archvivo del IFS
                    retorno = False;
                    cmdDelFile = f"DEL OBJLNK('{api.target}')"

                    while not retorno:
                        retorno = api.iprod.GetCmdMsg(cmdDelFile)

                    ciclo += 1
                    api.logdict[f'{elemento} - paso({ciclo})'] = f'Eliminamos el archvivo del IFS {retorno}'

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Rutas de los archivos y carpetas
                    ruta_origen = f'{ruta_completa}'

                    # Mover el archivo a la carpeta de archivos procesados
                    try:
                        os.rename(ruta_origen, os.path.join(api.ruta_destino, api.fuente))

                        ciclo += 1
                        api.logdict[f'{elemento} - paso({ciclo})'] = f"Archivo movido de {ruta_origen} a {api.ruta_destino}"

                    # si no encuentra el archivo    
                    except FileNotFoundError:
                        ciclo += 1
                        api.logdict[f'{elemento} - paso({ciclo})'] = f"El archivo {ruta_origen} no existe."

                    # si hay otro error
                    except Exception as e:
                        ciclo += 1
                        api.logdict[f'{elemento} - paso({ciclo})'] = f"Error al mover el archivo: {e}"


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Actualizamos la vinculacion de ALTAIMPOSITIVATITULAR y ALTAIMPOSITIVA
        #try:
        #    parm = list()
        #    strsql = (
        #        f'UPDATE ALTAIMPOSITIVATITULAR x '
        #        f'SET ALTAT00002 = ( '
        #        f'SELECT b."altataxid" ' 
        #        f'FROM ALTAIMPOSITIVA b '
        #        f'WHERE (b."archivorecibidoid" = X."archivorecibidoid" ) AND '
        #        f'((b."tipodocumentoid" = x."tipodocumentoid") and (b."numerodocumento" = x."numerodocumento") OR '
        #        f'(b."cuitcuil" = x."cuitcuil")) '
        #        f') '
        #        f'WHERE ALTAT00002 IS NULL '
        #    )
        #    retorno = api.db.run_comando(strsql, *parm)
        #except Exception as e:
        #    print(f'Error en el SQL ALTAIMPOSITIVATITULAR  {e}')

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Actualizamos la vinculacion de ALTAIMPOSITIVATITULAR y ALTAIMPOSITIVA
        #try:
        #    parm = list()
        #    strsql = (
        #        f'UPDATE BAJAIMPOSITIVATITULAR x '
        #        f'SET ALTAT00002 = ( '
        #        f'SELECT b."altataxid" ' 
        #        f'FROM BAJAIMPOSITIVA b '
        #        f'WHERE (b."archivorecibidoid" = X."archivorecibidoid" ) AND '
        #        f'((b."tipodocumentoid" = x."tipodocumentoid") and (b."numerodocumento" = x."numerodocumento") OR '
        #        f'(b."cuitcuil" = x."cuitcuil")) '
        #        f') '
        #        f'WHERE ALTAT00002 IS NULL '
        #    )
        #    retorno = api.db.run_comando(strsql, *parm)
        #except Exception as e:
        #    print(f'Error en el SQL  {e}')



        # Llama a la función para enviar el correo
        elemento = 'Recepcion SUCERP'                
        ciclo += 1
        api.logdict[f'{elemento} - paso({ciclo})'] = 'El proceso ha finalizado ...............................'

        print('El proceso ha finalizado ...............................')

        # Funcion de envio de correo
        # link para activar el gmail https://myaccount.google.com/security?hl=es
        # ir a la opcion Verificación en 2 pasos
        # ir a la opcion Contraseñas de aplicaciones
        # ir a crear una nueva contraseña de la aplicacion                

        html_content = '<html><head><!-- Puedes agregar meta información aquí si es necesario -->'
        html_content += 'INFORME LOG DEL PROCESO DE RECEPCION DE ARCHIVOS DE SUCERP</head><body>'
        html_content += '<ul>'
        for key, value in api.logdict.items():
            key_html = html.escape(str(key))
            value_html = html.escape(str(value))
            html_content += f'<li><strong>{key_html}:</strong> {value_html}</li>'
        html_content += '</ul></body></html>'


        # ------------------------------------------------------------------------
        # Configuración del remitente y destinatario
        remitente_email = 'alejpnovillog@gmail.com'
        destinatario_email = 'kuvasz102@gmail.com'

        # Configuración del servidor SMTP de Gmail
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_usuario = 'alejpnovillog@gmail.com'
        smtp_contrasena = 'ugmz diik xvys qhzt'

        # Configuración del mensaje
        asunto = 'Finalizacion del proceso de recepcion de archivos de Sucerp'
        cuerpo = html_content

        mensaje = MIMEMultipart()
        mensaje['From'] = remitente_email
        mensaje['To'] = destinatario_email
        mensaje['Subject'] = asunto

        # Agrega el cuerpo del mensaje
        #mensaje.attach(MIMEText(cuerpo, 'plain'))
        # Adjuntar el archivo HTML al mensaje
        mensaje.attach(MIMEText(html_content, "html"))

        # Inicia la conexión SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as servidor_smtp:
        
            # Establece la conexión segura
            servidor_smtp.starttls()

            # Inicia sesión en la cuenta de Gmail
            servidor_smtp.login(smtp_usuario, smtp_contrasena)

            # Envía el correo electrónico
            servidor_smtp.send_message(mensaje)

        print('Correo electrónico enviado con éxito.')

    except Exception as e:
        print(f'Error en el procesamiento  {e}')


# enlace para realizar el procesamiento de archivos
@router.get("/procesarSucerp")
async def endpoint_procesar_archivos(background_tasks: BackgroundTasks):
    
    # Obtengo la Url para redirigir
    urlRedirigir = ConfigurarAplicacion.URL_REDIRIGIR

    # Agrega la tarea al fondo para ser ejecutada asincrónicamente
    background_tasks.add_task(procesar_archivos)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulario POST</title>
    </head>
    <body>
        <form action="{urlRedirigir}" method="GET">
            <label>El proceso de recepcion de archivos de SUCERP se ha iniciado en segundo plano</label>
            <input type="submit" value="Continuar">
        </form>
    </body>
    </html>
        """
    return HTMLResponse(content=html_content)

