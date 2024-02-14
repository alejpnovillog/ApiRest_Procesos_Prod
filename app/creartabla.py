# Load las bibliotecas necesarias
try:
    import os
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    from app_Conexion_Iseries_JtOpen.pythonJTOpen import JT400Helper
    
except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lista de tablas a crear
lista_tablas = [
    'TABLA_ESTADO',                             # Tabla de referencia
    'TABLA_PROVINCIA',                          # Tabla de referencia
    'TABLA_TIPO_CUERPO',                        # Tabla de referencia
    'TABLA_TIPO_CUOTA',                         # Tabla de referencia
    'TABLA_TIPO_DOCUMENTO',                     # Tabla de referencia
    'TABLA_TIPO_MONEDA',                        # Tabla de referencia
    'TABLA_TIPO_MOVIMIENTO',                    # Tabla de referencia
    'TABLA_TIPO_ORIGEN',                        # Tabla de referencia
    'TABLA_TIPO_PAGO',                          # Tabla de referencia
    'TABLA_TIPO_REGISTRO',                      # Tabla de referencia
    'TABLA_TIPO_SUB_REGISTRO',                  # Tabla de referencia
    'TABLA_TIPO_TITULAR',                       # Tabla de referencia
    'TABLA_API_ESTADOS',                        # Tabla de referencia
    'TABLA_API_TAREAS',                         # Tabla de referencia
    'TABLA_API_LOG',                            # Tabla de referencia
    'TABLA_PROCESOIMPORTACIONEXPORTACION',      # --------------------
    'TABLA_RECEPCION_TEXTO',                    # ---------------------
    'TABLA_RECEPLOG',                           # ---------------------
    'TABLA_API_ESTADOS_TAREAS',                 # --------------------- 
    'TABLA_API_REGISTROS',                      # --------------------- 
    'TABLA_API_TOKEN_USER',                     # --------------------- 
    'TABLA_API_TOKEN',                          # --------------------- 
    'TABLA_ENCABEZADO',                         # --------------------- 
    'TABLA_PIE',                                # ---------------------
    'TABLA_ALTAIMPOSITIVATITULAR',              # ---------------------
    'TABLA_ALTAIMPOSITIVA',                     # ---------------------
    'TABLA_BAJAIMPOSITIVATITULAR',              # --------------------- 
    'TABLA_BAJAIMPOSITIVA',                     # --------------------- 
    'TABLA_ANULACIONTRAMITESSELLOS',            # --------------------- 
    'TABLA_ANULACIONTRAMITESSELLOSDETALLE',     # --------------------- 
    'TABLA_CAMBIOTITULARIDADTITULAR',           # --------------------- 
    'TABLA_CAMBIOTITULARIDAD',                  # --------------------- 
    'TABLA_INFORMACIONVEHICULO',                # --------------------- 
    'TABLA_INFORMACIONVEHICULOTITULAR',         # --------------------- 
    'TABLA_IMPUESTOAUTOMOTOR',                  # --------------------- 
    'TABLA_INFORMACIORADICACION',               # --------------------- 
    'TABLA_IMPUESTOSELLOS',                     # --------------------- 
    'TABLA_IMPUESTOSELLOSPARTES',               # --------------------- 
    'TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE',    # --------------------- 
    'TABLA_TRAMITESGENERALESTITULARES',         # --------------------- 
    'TABLA_TRAMITESGENERALES',                  # --------------------- 
    'TABLA_API_AUMOSO',                         # --------------------- 
    'TABLA_RELACION_ARBA_SUCERP_MARCA',         # --------------------- 
]


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# eliminar las tablas en forma ordenada
def eliminarTablas():

    try:

        for elemento in reversed(lista_tablas):

            # generamos la estructura de la tabla en la base de datos
            valor  = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])

            # obtenemos el nombre de la tabla
            file = valor._dalname

            # averiguamos si tiene shortname
            if not ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname'] == None:
                file = ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname']

            # obtenemos del schema donde estan las tablas
            lib = con['schema']

            print('-------------------------------------------------------------------- ')
            print(f'Eliminamos la tabla del Journal {lib}/{file} ...................... ')

            # Elininamos la tabla del Journal
            str = f'ENDJRNPF FILE({lib}/{file})'

            # Ejecutamos el comando
            msg = iprod.GetCmdMsg(str)

            # si no hay error
            if msg[0]:
                print(f'Tabla {file} Journalizada...')
            else:
                print(f'Tabla {file} {msg[1]} ')    


            print(f'Nombre de la Tabla ({lib}/{file})')

            # Eliminamos el objeto de la biblioteca
            str =f'DLTOBJ OBJ({lib}/{file}) OBJTYPE(*FILE)'

            # Ejecutamos el comando
            msg = iprod.GetCmdMsg(str)

            # si no hay error
            if msg[0]:
                print(f'Tabla {file} Eliminamos de la biblioteca...')
            else:
                print(f'Tabla {file} {msg[1]} ')    


    except Exception as inst:
        print(inst)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Creamos las tablas en la bibliotecas
def creacionTablas():

    # inspeccionamos la lista
    try:

        # recorremos la lista de las tablas
        for elemento in lista_tablas:

            # activamos para la creacion de la tabla
            ConfigurarAplicacion.LISTA_TABLAS[elemento]['migrate'] = True

            # generamos la estructura de la tabla en la base de datos
            valor  = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])

            # desactivamos la creacion de la tabla
            ConfigurarAplicacion.LISTA_TABLAS[elemento]['migrate'] = False

            # eliminamos el archivo que indica la creacion de la tabla
            os.remove(valor._dbt)
            print('-------------------------------------------------------------------- ')
            print(f'Nombre de la Tabla ({valor})')

            # obtenemos el nombre de la tabla
            file = valor._dalname

            # averiguamos si tiene shortname
            if not ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname'] == None:
                file = ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname']


            print(f'Registramos por Journal la tabla {lib}/{file} ...................... ')
            str = f'STRJRNPF FILE({lib}/{file}) JRN({lib}/QSQJRN) IMAGES(*BOTH)'

            # Registramos en el Journal
            msg = iprod.GetCmdMsg(str)

            # si no hay error
            if msg[0]:
                print(f'Tabla {file} Journalizada...')
            else:
                print(f'Tabla {file} {msg[1]} ')    


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
                data_Input.db.executesql(sentencia)

                # realizamos el commit para la sentencia SQL
                data_Input.db.commit()


    except Exception as inst:
        print(inst)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Obtengo el conector a la base de datos
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

# obtenemos el string de conexion
con = data_Input.__getattribute__('instancia_Host_Input_Dict')

# Definimos la conexion con el sistema os400 para ejecutar comandos
iprod = JT400Helper(con['ip'], con['usuario'], con['password'])

# obtenemos del schema donde estan las tablas
lib = con['schema']

# realizamos la creacion de las tablas
creacionTablas()

# realizamos la eliminacion de las tablas
eliminarTablas()

