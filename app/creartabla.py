# Load las bibliotecas necesarias
try:

    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    
except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lista de tablas a crear
lista_tablas = [
    'TABLA_ESTADO',                             # True Tabla de referencia
    #'TABLA_PROVINCIA',                          # True Tabla de referencia
    #'TABLA_TIPO_CUERPO',                        # True Tabla de referencia
    #'TABLA_TIPO_CUOTA',                         # True Tabla de referencia
    #'TABLA_TIPO_DOCUMENTO',                     # True Tabla de referencia
    #'TABLA_TIPO_MONEDA',                        # True Tabla de referencia
    #'TABLA_TIPO_MOVIMIENTO',                    # True Tabla de referencia
    #'TABLA_TIPO_ORIGEN',                        # True Tabla de referencia
    #'TABLA_TIPO_PAGO',                          # True Tabla de referencia
    #'TABLA_TIPO_REGISTRO',                      # True Tabla de referencia
    #'TABLA_TIPO_SUB_REGISTRO',                  # True Tabla de referencia
    #'TABLA_TIPO_TITULAR',                       # True Tabla de referencia
    #'TABLA_API_ESTADOS',                        # False Tabla de referencia
    #'TABLA_API_TAREAS',                         # False Tabla de referencia
    #'TABLA_API_LOG',                            # False Tabla de referencia
    #'TABLA_PROCESOIMPORTACIONEXPORTACION',      # True Tabla de referencia

    #'TABLA_TIPO_VEHICULO',                      # False Tabla de referencia
    #'TABLA_TIPO_TRAMITE',                       # False Tabla de referencia

    #'TABLA_CATEGORIA',                          # True
    #'TABLA_DETALLE_TIPO_TRAMITE',               # False
    #'TABLA_API_ESTADOS_TAREAS',                 # False
    #'TABLA_API_REGISTROS',                      # False
    #'TABLA_API_TOKEN_USER',                     # False
    #'TABLA_API_TOKEN',                          # False

    #'TABLA_ALTAIMPOSITIVATITULAR',              # True
    #'TABLA_ALTAIMPOSITIVA',                     # True
    #'TABLA_API_AUMOSO',                         # False
    #'TABLA_ANULACIONTRAMITESSELLOS',            # True
    #'TABLA_ANULACIONTRAMITESSELLOSDETALLE',     # True
    #'TABLA_BAJAIMPOSITIVATITULAR',              # True
    #'TABLA_BAJAIMPOSITIVA',                     # True
    #'TABLA_CAMBIOTITULARIDADTITULAR',           # True
    #'TABLA_CAMBIOTITULARIDAD',                  # True
    #'TABLA_ENCABEZADO',                         # True
    #'TABLA_IMPUESTOAUTOMOTOR',                  # True
    #'TABLA_IMPUESTOSELLOS',                     # True
    #'TABLA_IMPUESTOSELLOSPARTES',               # True
    #'TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE',    # True
    #'TABLA_INFORMACIORADICACION',               # True
    #'TABLA_INFORMACIONVEHICULO',                # True
    #'TABLA_INFORMACIONVEHICULOTITULAR',         # True
    #'TABLA_PIE',                                # True
    #'TABLA_RELACION_ARBA_SUCERP_MARCA',         # False
    #'TABLA_TRAMITESGENERALES',                  # True
    #'TABLA_TRAMITESGENERALESTITULARES',         # True
]


# Obtengo el conector a la base de datos
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

# inspeccionamos la lista

try:
        for elemento in lista_tablas:

            #data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])
            valor  = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])


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

                data_Input.db.commit()


            print(f'Nombre de la Tabla ({valor})')


except Exception as inst:
    print(inst)







