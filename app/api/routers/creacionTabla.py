# Load las bibliotecas necesarias
# http://localhost:8000/dgtic/crearestructuraSucerp
try:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart    
    import html
    import os
    import platform

    import os
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    from app_Conexion_Iseries_JtOpen.pythonJTOpen import JT400Helper
    from fastapi import BackgroundTasks, APIRouter
    from fastapi.responses import HTMLResponse


except Exception as e:
    print(f'Falta algun modulo {e}')


# Definimos la clase para manejar los recursos del contexto del proceso
class ConfigurarAplicacionSubmit:

    # definimos la funcion de inicializacion
    def __enter__(self):

        try:

            # Lista de tablas a crear
            self.lista_tablas = ConfigurarAplicacion.TABLAS_CREACION

            # Obtengo el conector a la base de datos
            self.data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

            # obtenemos el string de conexion
            self.con = self.data_Input.__getattribute__('instancia_Host_Input_Dict')

            # Definimos la conexion con el sistema os400 para ejecutar comandos
            self.iprod = JT400Helper(self.con['ip'], self.con['usuario'], self.con['password'])

            # obtenemos del schema donde estan las tablas
            self.lib = self.con['schema']

            # definimos el diccionario para que el contenido lo enviar por mail
            self.logdict = dict()

        except Exception as e:
            print(f"Error al inicializar recursos en ConfigurarAplicacionSubmit: {e}")

        return self

    # definimos la funcion de la finalizacion de la clase
    def __exit__(self, exc_type, exc_value, traceback):
      
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
async def creacion_tablas():

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Procesamiento General
    try:

        print(f"Proceso iniciado..........")

        # Iniciar la aplicación
        with ConfigurarAplicacionSubmit() as api:

            # definimos el contador para los ciclos de la transferencia
            ciclo = 0


            # recorremos la lista de las tablas
            for elemento in api.lista_tablas:

                # activamos para la creacion de la tabla
                ConfigurarAplicacion.LISTA_TABLAS[elemento]['migrate'] = True

                # generamos la estructura de la tabla en la base de datos
                valor  = api.data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])

                # desactivamos la creacion de la tabla
                ConfigurarAplicacion.LISTA_TABLAS[elemento]['migrate'] = False

                # eliminamos el archivo que indica la creacion de la tabla
                os.remove(valor._dbt)

                ciclo += 1
                api.logdict[f'paso({ciclo})'] = f"....................."

                ciclo += 1
                api.logdict[f'paso({ciclo})'] = f'Nombre de la Tabla ({valor})'

                # obtenemos el nombre de la tabla
                file = valor._dalname

                # obtenemos el nombre del objeto tabla para journalizar
                parm = list()
                strsql = f"SELECT SYSTEM_TABLE_NAME FROM QSYS2.SYSTABLES WHERE TABLE_SCHEMA = '{api.lib.upper()}' AND TABLE_NAME = '{file}'"
                ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname'] = api.data_Input.run_comando(strsql, *parm)[0][0]

                # averiguamos si tiene shortname
                if not ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname'] == None:
                    file = ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname']

                ciclo += 1
                api.logdict[f'paso({ciclo})'] = f'Registramos por Journal la tabla {api.lib}/{file} ...................... '

                str = f'STRJRNPF FILE({api.lib}/{file}) JRN({api.lib}/QSQJRN) IMAGES(*BOTH)'

                # Registramos en el Journal
                msg = api.iprod.GetCmdMsg(str)

                # si no hay error
                if msg[0]:

                    ciclo += 1
                    api.logdict[f'paso({ciclo})'] = f'Tabla {file} Journalizada...'

                else:
                    ciclo += 1
                    api.logdict[f'paso({ciclo})'] = f'Tabla {file} {msg[1]} '



                # verificamos si el ambiente esta dentro de la lista para cambiar los
                # textos de los campos de la tabla    
                if ConfigurarAplicacion.ENV_GX in ConfigurarAplicacion.ENV_LABEL_ON:

                    texto = ''

                    # we iterate through the fields of the table record
                    for x in range(0, len(valor._fields)):

                        # we build the text variable
                        texto += f'\"{valor._fields[x].lower()}\" text is \'{valor.__getattribute__(valor._fields[x]).comment}\''

                        if x != (len(valor._fields) - 1):
                            texto += ' ,'

                    # we build the sentencia variable
                    sentencia = f'LABEL ON COLUMN {valor._dalname} ({texto})'

                    # execute the sql statement
                    api.data_Input.db.executesql(sentencia)

                    # realizamos el commit para la sentencia SQL
                    api.data_Input.db.commit()

        # Llama a la función para enviar el correo
        ciclo += 1
        api.logdict[f'paso({ciclo})'] = 'El proceso ha finalizado ...............................'

        print('El proceso ha finalizado ...............................')

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Funcion de envio de correo
        # link para activar el gmail https://myaccount.google.com/security?hl=es
        # ir a la opcion Verificación en 2 pasos
        # ir a la opcion Contraseñas de aplicaciones
        # ir a crear una nueva contraseña de la aplicacion                

        html_content = '<html><head><!-- Puedes agregar meta información aquí si es necesario -->'
        html_content += 'INFORME LOG DEL PROCESO DE CREACION DE LAS ESTRUCTURAS DE LAS TABLAS PARA RECIBIR INFORMACION DE SUCERP</head><body>'
        html_content += '<ul>'
        for key, value in api.logdict.items():
            key_html = html.escape(key)
            value_html = html.escape(value)
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
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    except Exception as e:
        print(f'Error en el procesamiento  {e}')

# enlace para realizar el procesamiento de archivos
@router.get("/crearestructuraSucerp")
async def endpoint_procesar_archivos(background_tasks: BackgroundTasks):

    # Obtengo la Url para redirigir
    urlRedirigir = ConfigurarAplicacion.URL_REDIRIGIR

    # Agrega la tarea al fondo para ser ejecutada asincrónicamente
    background_tasks.add_task(creacion_tablas)

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
            <label>El proceso de PROCESO DE CREACION DE LAS ESTRUCTURAS DE LAS TABLAS PARA RECIBIR INFORMACION DE SUCERP se ha iniciado en segundo plano</label>
            <input type="submit" value="Continuar">
        </form>
    </body>
    </html>
        """
    return HTMLResponse(content=html_content)
