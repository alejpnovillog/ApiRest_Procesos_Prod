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
lista_tablas = ConfigurarAplicacion.TABLAS_CREACION


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# eliminar las tablas en forma ordenada
def eliminarTablas():

    try:

        global lib

        for elemento in reversed(lista_tablas):

            # generamos la estructura de la tabla en la base de datos
            valor  = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])

            # obtenemos el nombre de la tabla
            file = valor._dalname
            
            # obtenemos el nombre del objeto tabla para journalizar
            parm = list()
            strsql = f"SELECT SYSTEM_TABLE_NAME FROM QSYS2.SYSTABLES WHERE TABLE_SCHEMA = '{lib.upper()}' AND TABLE_NAME = '{file}'"
            ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname'] = data_Input.run_comando(strsql, *parm)[0][0]


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

            # obtenemos el nombre del objeto tabla para journalizar
            file = valor._dalname
            parm = list()
            strsql = f"SELECT SYSTEM_TABLE_NAME FROM QSYS2.SYSTABLES WHERE TABLE_SCHEMA = '{lib.upper()}' AND TABLE_NAME = '{file}'"
            ConfigurarAplicacion.LISTA_TABLAS[elemento]['shortname'] = data_Input.run_comando(strsql, *parm)[0][0]
            #file = file[0][0]

            print('-------------------------------------------------------------------- ')
            print(f'Nombre de la Tabla ({valor})')



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
#creacionTablas()

# realizamos la eliminacion de las tablas
eliminarTablas()

