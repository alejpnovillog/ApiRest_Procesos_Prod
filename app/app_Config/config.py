

class ConfigurarAplicacion(object):

    # Conectores del MOTOR SQLITE
    VALIDATOR       = "Validator"

    # Conectores del MOTOR postgresql
    POSTGRESQL_MATANZA = "IseriesMatanza_postgres"
    POSTGRESQL_GXPROD = "IseriesGxProd_postgres"

    # Conectores del MOTOR MYSQL
    MYSQL_MATANZA   = "IseriesMatanza_mysql"
    MYSQL_GXPROD    = "IseriesGxProd_mysql"

    # Conectores del MOTOR ISERIES
    TEST_MATANZA    = "Matanza_tst"
    PROD_MATANZA    = "Matanza_prd"

    TEST_ISERIES    = "Iseries_tst"
    PROD_ISERIES    = "Iseries_prd"

    PUB400_LIB = "Pub400"

    # Ambientes
    ENV_SOURCE  = POSTGRESQL_GXPROD
    ENV_TARGET  = PROD_ISERIES
    ENV_MATANZA = None
    ENV_GX      = PROD_ISERIES
    ENV_GX_TEST = TEST_ISERIES
    ENV_DDS     = 'IseriesDDSEpagos_Prd'
    ENV_SQ      = None


    # Ambientes con LABEL ON
    ENV_LABEL_ON = [TEST_ISERIES, PROD_ISERIES]

    # Cantidad de registros para un trabajar con
    WRK_RECORDS = 100

    SERVER_HTTP_DEVELOPMENT = 'http://localhost:8000'
    SERVER_HTTP_PRODUCTION  = 'http://MLMSRV:8000'

    JVMPATH_WINDOWS = 'C:\\Program Files\\Java\\jre-1.8\\bin\\server\\jvm.dll'
    JVMPATH_LINUX = '/usr/lib/jvm/java-11-openjdk-amd64/lib/server/libjvm.so'

    ADDCLASSPATH_WINDOWS  = 'C:\Software\JtOpen\lib\*'
    ADDCLASSPATH_LINUX  = '/home/anovillo/Escritorio/Jtopen/JtOpen/lib/*'

    JARPATH_WINDOWS = 'C:\\Users\\anovillo\\Desktop\\Software\\JtOpen\\lib\jt400.jar'
    JARPATH_LINUX = '/home/anovillo/Escritorio/Jtopen/JtOpen/lib/jt400.jar'

    RECEPCIONPATH_WINDOWS = 'C:\\Users\\anovillo\\Desktop\\Rendiciones'
    PROCESADOPATH_WINDOWS = 'C:\\Users\\anovillo\\Desktop\\Rendiciones_Procesadas'

    RECEPCIONPATH_LINUX = '/home/anovillo/Escritorio/Rendiciones'
    PROCESADOPATH_LINUX = '/home/anovillo/Escritorio/Rendiciones_Procesadas'
    
    FTPDIR = '/home/anovillo/'

    # Tablas Id
    TABLA_ESTADO                          = 1
    TABLA_PROVINCIA                       = 2
    TABLA_TIPO_CUERPO                     = 3
    TABLA_TIPO_CUOTA                      = 4
    TABLA_TIPO_DOCUMENTO                  = 5
    TABLA_TIPO_MONEDA                     = 6
    TABLA_TIPO_MOVIMIENTO                 = 7
    TABLA_TIPO_ORIGEN                     = 8
    TABLA_TIPO_PAGO                       = 9
    TABLA_TIPO_REGISTRO                   = 10
    TABLA_TIPO_SUB_REGISTRO               = 11
    TABLA_TIPO_TITULAR                    = 12
    TABLA_API_TOKEN_USER                  = 14
    TABLA_API_ESTADOS                     = 15
    TABLA_API_TAREAS                      = 16
    TABLA_API_ESTADOS_TAREAS              = 17
    TABLA_API_TOKEN                       = 18
    TABLA_API_AUMOSO                      = 19
    TABLA_API_REGISTROS                   = 20
    TABLA_ALTAIMPOSITIVA                  = 21
    TABLA_ALTAIMPOSITIVATITULAR           = 22
    TABLA_ANULACIONTRAMITESSELLOS         = 23
    TABLA_ANULACIONTRAMITESSELLOSDETALLE  = 24
    TABLA_BAJAIMPOSITIVA                  = 25
    TABLA_BAJAIMPOSITIVATITULAR           = 26
    TABLA_CAMBIOTITULARIDAD               = 27
    TABLA_CAMBIOTITULARIDADTITULAR        = 28
    TABLA_ENCABEZADO                      = 29
    TABLA_IMPUESTOAUTOMOTOR               = 34
    TABLA_IMPUESTOSELLOS                  = 35
    TABLA_IMPUESTOSELLOSPARTES            = 36
    TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE = 37
    TABLA_INFORMACIONVEHICULO             = 38
    TABLA_INFORMACIONVEHICULOTITULAR      = 39
    TABLA_INFORMACIORADICACION            = 40
    TABLA_PIE                             = 41
    TABLA_RECEPCIONARCHIVOS               = 44  
    TABLA_TMPINFORMACIONVEHICULO          = 45
    TABLA_TMPINFORMACIONVEHICULOTITULAR   = 46
    TABLA_RELACION_ARBA_SUCERP_MARCA      = 47
    TABLA_PROCESOIMPORTACIONEXPORTACION   = 48
    TABLA_API_LOG                         = 49
    TABLA_RECEPCION_TEXTO                 = 50
    TABLA_RECEPLOG                        = 51
    TABLA_MENSAJESERROR                   = 52  
    TABLA_MSGNIVELGRAVEDAD                = 53
    TABLA_MENSAJESERRORMSGDINAMICOS       = 54
    TABLA_IMPRESIONPDF                    = 55


    TABLAS_CREACION = [
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
    ##'TABLA_API_ESTADOS',                        # Tabla de referencia
    ##'TABLA_API_TAREAS',                         # Tabla de referencia
    ##'TABLA_API_LOG',                            # Tabla de referencia
    'TABLA_PROCESOIMPORTACIONEXPORTACION',      # --------------------
    'TABLA_RECEPCIONARCHIVOS',                  # ---------------------
    'TABLA_RECEPLOG',                           # ---------------------
    ##'TABLA_API_ESTADOS_TAREAS',                 # --------------------- 
    ##'TABLA_API_REGISTROS',                      # --------------------- 
    ##'TABLA_API_TOKEN_USER',                     # --------------------- 
    ##'TABLA_API_TOKEN',                          # --------------------- 
    'TABLA_ENCABEZADO',                         # --------------------- 
    'TABLA_INFORMACIONVEHICULO',                # --------------------- 
    'TABLA_INFORMACIONVEHICULOTITULAR',         # ---------------------     
    'TABLA_PIE',                                # ---------------------
    'TABLA_TRAMITESGENERALES',                  # --------------------- 
    'TABLA_TRAMITESGENERALESTITULARES',         # --------------------- 
    'TABLA_ALTAIMPOSITIVA',                     # ---------------------
    'TABLA_ALTAIMPOSITIVATITULAR',              # ---------------------
    'TABLA_BAJAIMPOSITIVATITULAR',              # --------------------- 
    'TABLA_BAJAIMPOSITIVA',                     # --------------------- 
    'TABLA_ANULACIONTRAMITESSELLOS',            # --------------------- 
    'TABLA_ANULACIONTRAMITESSELLOSDETALLE',     # --------------------- 
    'TABLA_CAMBIOTITULARIDADTITULAR',           # --------------------- 
    'TABLA_CAMBIOTITULARIDAD',                  # --------------------- 
    'TABLA_IMPUESTOAUTOMOTOR',                  # --------------------- 
    'TABLA_INFORMACIORADICACION',               # --------------------- 
    'TABLA_IMPUESTOSELLOS',                     # --------------------- 
    'TABLA_IMPUESTOSELLOSPARTES',               # --------------------- 
    'TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE',    # --------------------- 
    ##'TABLA_API_AUMOSO',                         # --------------------- 
    'TABLA_RELACION_ARBA_SUCERP_MARCA',         # --------------------- 
    ]


    # Lista de Tablas
    LISTA_TABLAS = {
        # Tabla de Estados
        'TABLA_ESTADO': {
            'numero': 1, 'objeto': 'estado_Dal', 'migrate' : False, 'shortname': 'TIPOESTADO',
            'html_wrk': 'estadowrk.html',
            'query_list': ['_all', '_description', '_estado', '_estado_R'],
            'default_query': '_all',
            # query todos los registros
            '_all': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [0],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros por descripcion
            '_description': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [2],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros por estado
            '_estado': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [1],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros con estado = R
            '_estado_R': {
                'fieldnumber': [1, ],
                'field': [ ('R', ), ],
                'struct_query': ['fld',],
                'op': ['EQ', ],
                'order': False,
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
        },
        # TABLA_PROVINCIA
        'TABLA_PROVINCIA' : {
            'numero': 2, 'objeto': 'provincias_Dal', 'migrate' : False, 'shortname': 'PROVINCIAS',
            'html_wrk': 'provinciawrk.html',
            # query todos los registros
            'query_all': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [0],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros por descripcion
            'query_enabled': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [1],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
        },
        # TABLA_TIPO_CUERPO
        'TABLA_TIPO_CUERPO': {
            'numero': 3, 'objeto': 'tipoCuerpo_Dal', 'migrate' : False, 'shortname': 'TIPOCUERPO',
            'html_wrk': 'tipocuerpowrk.html',
            # query todos los registros
            'query_all': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [0],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros por descripcion
            'query_description': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [2],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros por Codigo
            'query_code': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [1],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
        },
        # TABLA_TIPO_CUOTA
        'TABLA_TIPO_CUOTA': {
            'numero': 4, 'objeto': 'tipoCuota_Dal', 'migrate' : False, 'shortname': 'TIPOCUOTA',
            'html_wrk': 'tipocuotawrk.html',
            # query todos los registros
            'query_all': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [0],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros por descripcion
            'query_description': {
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [2],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False
            },
            # query todos los registros por Codigo
            'query_code': {
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [1],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
        },
        'TABLA_TIPO_DOCUMENTO': {
            'numero': 5, 'objeto': 'tipoDocumento_Dal', 'migrate' : False, 'shortname': 'TIPOD00001',
            'html_wrk': 'tipodocumentowrk.html',
            'query_list': ['_all', '_description', '_code'],
            'default_query': '_all',
            # query todos los registros
            '_all': {
                'alias': 'Todos',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [0],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None,
                'executesql': False
            },
            # query todos los registros por descripcion
            '_description': {
                'alias': 'por Descripcion',
                'fieldnumber': False,
                'field': False,
                'struct_query': False,
                'op': False,
                'order': [2],
                'pageno': False,
                'indexpageno': False,
                'seleccion': False,
                'wrkrecords': False,
                'executesql': False
            },
            # query todos los registros por Codigo
            '_code': {
                'alias': 'por Codigo',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [1],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
        },
        'TABLA_TIPO_MONEDA': {
            'numero': 6, 'objeto': 'tipoMoneda_Dal', 'migrate' : False, 'shortname': 'TIPOMONEDA',
            'html_wrk': 'tipomonedawrk.html',
            'query_list': ['_all', '_description', '_code'],
            'default_query': '_all',
            # query todos los registros
            '_all': {
                'alias': 'Todos',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
            # query todos los registros por descripcion
            '_description': {
                'alias': 'por Descripcion',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [2],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
            # query todos los registros por Codigo
            '_code': {
                'alias': 'por Codigo',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [1],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
        },
        'TABLA_TIPO_MOVIMIENTO': {
            'numero': 7, 'objeto': 'tipoMovimiento_Dal', 'migrate' : False, 'shortname': 'TIPOM00001',
            'html_wrk': 'tipomovimientowrk.html',
            'query_list': ['_all', '_description', '_code'],
            'default_query': '_all',
            # query todos los registros
            '_all': {
                'alias': 'todos',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
            # query todos los registros por descripcion
            '_description': {
                'alias': 'por Descripcion',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [2],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
            # query todos los registros por Codigo
            '_code': {
                'alias': 'Por Codigo',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [1],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
        },
        'TABLA_TIPO_ORIGEN': {
            'numero': 8, 'objeto': 'tipoOrigen_Dal', 'migrate' : False, 'shortname': 'TIPOORIGEN',
            'html_wrk': 'tipoorigenwrk.html',
            'query_list': ['_all', '_description', '_code'],
            'default_query': '_all',
            # query todos los registros
            '_all': {
                'alias': 'todos',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
            # query todos los registros por descripcion
            '_description': {
                'alias': 'por Descripcion',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [2],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
            # query todos los registros por Tipo
            '_code': {
                'alias': 'por Tipo',
                'fieldnumber': [],
                'field': [],
                'struct_query': [],
                'op': [],
                'order': [1],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            },
        },
        'TABLA_TIPO_PAGO': {'numero': 9, 'objeto': 'tipoPago_Dal', 'migrate' : False, 'shortname': None},
        'TABLA_TIPO_REGISTRO': {'numero': 10, 'objeto': 'tipoRegistro_Dal', 'migrate' : False, 'shortname': 'TIPOR00001',},
        'TABLA_TIPO_SUB_REGISTRO': {'numero': 11, 'objeto': 'tipoSubRegistro_Dal', 'migrate' : False, 'shortname': 'TIPOS00001',},
        'TABLA_TIPO_TITULAR': {'numero': 12, 'objeto': 'tipoTitular_Dal', 'migrate' : False, 'shortname': 'TIPOT00001',},
        'TABLA_API_TOKEN_USER': {'numero': 14, 'objeto': 'apiTokenUser_Dal', 'migrate' : False, 'shortname': 'APITO00001',},
        'TABLA_API_ESTADOS': {'numero': 15, 'objeto': 'apiEstados_Dal', 'migrate' : False, 'shortname': None,},
        'TABLA_API_TAREAS': {'numero': 16, 'objeto': 'apiTareas_Dal', 'migrate' : False, 'shortname': None,},
        'TABLA_API_ESTADOS_TAREAS': {'numero': 17, 'objeto': 'apiEstadosTareas_Dal', 'migrate' : False, 'shortname': 'APIES00001',},
        'TABLA_API_TOKEN': {'numero': 18, 'objeto': 'apiToken_Dal', 'migrate' : False, 'shortname': None,},
        'TABLA_API_AUMOSO': {'numero': 19, 'objeto': 'apiAumoso_Dal', 'migrate' : False, 'shortname': None,},
        'TABLA_API_REGISTROS': {'numero': 20, 'objeto': 'apiRegistros_Dal', 'migrate' : False, 'shortname': 'APIRE00001',},
        'TABLA_ALTAIMPOSITIVA': {'numero': 21, 'objeto': 'altaImpositiva_Dal', 'migrate' : False, 'shortname': 'ALTAI00002',},
        'TABLA_ALTAIMPOSITIVATITULAR': {'numero': 22, 'objeto': 'altaImpositivaTitular_Dal', 'migrate' : False, 'shortname': 'ALTAI00001',},
        'TABLA_ANULACIONTRAMITESSELLOS': {'numero': 23, 'objeto': 'anulacionTramitesSellos_Dal', 'migrate' : False, 'shortname': 'ANULA00001',},
        'TABLA_ANULACIONTRAMITESSELLOSDETALLE': {'numero': 24, 'objeto': 'anulacionTramitesSellosDetalle_Dal', 'migrate' : False, 'shortname': 'ANULA00002',},
        'TABLA_BAJAIMPOSITIVA': {'numero': 25, 'objeto': 'bajaImpositiva_Dal', 'migrate' : False, 'shortname': 'BAJAI00002',},
        'TABLA_BAJAIMPOSITIVATITULAR': {'numero': 26, 'objeto': 'bajaImpositivaTitular_Dal', 'migrate' : False, 'shortname': 'BAJAI00001',},
        'TABLA_CAMBIOTITULARIDAD': {'numero': 27, 'objeto': 'cambioTitularidad_Dal', 'migrate' : False, 'shortname': 'CAMBI00002',},
        'TABLA_CAMBIOTITULARIDADTITULAR': {'numero': 28, 'objeto': 'cambioTitularidadTitular_Dal', 'migrate' : False, 'shortname': 'CAMBI00001',},
        'TABLA_ENCABEZADO': {'numero': 29, 'objeto': 'encabezado_Dal', 'migrate' : False, 'shortname': None,},
        'TABLA_IMPUESTOAUTOMOTOR': {'numero': 34, 'objeto': 'impuestoAutomotor_Dal', 'migrate' : False, 'shortname': 'IMPUE00001',},
        'TABLA_IMPUESTOSELLOS': {'numero': 35, 'objeto': 'impuestoSellos_Dal', 'migrate' : False, 'shortname': 'IMPUE00002',},
        'TABLA_IMPUESTOSELLOSPARTES': {'numero': 36, 'objeto': 'impuestoSellosPartes_Dal', 'migrate' : False, 'shortname': 'IMPUE00003',},
        'TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE': {'numero': 37, 'objeto': 'impuestoSellosPartesTipoTramite_Dal', 'migrate' : False, 'shortname': 'IMPUE00004',},
        'TABLA_INFORMACIONVEHICULO': {
            'numero': 38, 'objeto': 'informacionVehiculo_Dal', 'migrate' : False, 'shortname': 'INFOR00001',
            'html_wrk':'informacionvehiculo.html',
            'query_list': ['_query', ],
            'default_query': '_query',
            '_query':{
                'fieldnumber': [8, 12, 10],
                'field': [ (48, ), (1956, 1992), ('MOTOCICLETA', 'CUATRICICLO')],
                'struct_query': ['fld',  '&', '&',],
                'op': ['EQ', 'IN', 'LK'],
                'pageno': None,
                'indexpageno': None,
                'seleccion': None,
                'wrkrecords': None
            }
        },
        'TABLA_INFORMACIONVEHICULOTITULAR': {'numero': 39, 'objeto': 'informacionVehiculoTitular_Dal', 'migrate' : False, 'shortname': 'INFOR00002',},
        'TABLA_INFORMACIORADICACION': {'numero': 40, 'objeto': 'informacionRadicacion_Dal', 'migrate' : False, 'shortname': 'INFOR00003',},
        'TABLA_PIE': {'numero': 41, 'objeto': 'pie_Dal', 'migrate' : False, 'shortname': None,},
        'TABLA_TRAMITESGENERALES': {'numero': 42, 'objeto': 'tramitesGenerales_Dal', 'migrate' : False, 'shortname': 'TRAMI00002',},
        'TABLA_TRAMITESGENERALESTITULARES': {'numero': 43, 'objeto': 'tramitesGeneralesTitular_Dal', 'migrate' : False, 'shortname': 'TRAMI00001',},
        'TABLA_RECEPCIONARCHIVOS': {'numero': 44, 'objeto': 'recepcionArchivos_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_TMPINFORMACIONVEHICULO': {'numero': 45, 'objeto': 'tmpInformacionVehiculo_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_TMPINFORMACIONVEHICULOTITULAR': {'numero': 46, 'objeto': 'tmpInformacionVehiculoTitular_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_RELACION_ARBA_SUCERP_MARCA': {'numero': 47, 'objeto': 'relArbaSucerpMarca_Dal', 'migrate': False, 'shortname': 'RELAC00001',},
        'TABLA_PROCESOIMPORTACIONEXPORTACION': {'numero': 48, 'objeto': 'procesoImportacionExportacion_Dal', 'migrate': False, 'shortname': 'PROCE00001',},
        'TABLA_API_LOG': {'numero': 49, 'objeto': 'apiLog_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_RECEPCION_TEXTO': {'numero': 50, 'objeto': 'recepcionTexto_Dal', 'migrate': False, 'shortname': 'RECEP00001',},
        'TABLA_RECEPLOG': {'numero': 51, 'objeto': 'recepLog_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_MENSAJESERROR': {'numero': 52, 'objeto': 'mensajeError_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_MSGNIVELGRAVEDAD': {'numero': 53, 'objeto': 'msgNivelGravedad_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_MENSAJESERRORMSGDINAMICOS': {'numero': 54, 'objeto': 'mensajesErrorMsgdDinamicos_Dal', 'migrate': False, 'shortname': None,},
        'TABLA_IMPRESIONPDF': {'numero': 55, 'objeto': 'impresionPdf_Dal', 'migrate': False, 'shortname': None,},

    }

    # Tablas Objeto Nombre
    APITOKENUSER                = 'apiTokenUser'

    # Switch Render Template
    SWITCH_RENDER_TEMPLATE = True


    # Render Pagina de error
    HTML_ERRNOEXISTE = 'errnoexiste.html'


    # Render Paginas WRK
    HTML_WRKESTADOS             = 'estadowrk.html'
    HTML_WRKPROVINCIAS          = 'provinciawrk.html'
    HTML_WRKTIPOCUERPO          = 'tipocuerpowrk.html'
    HTML_WRKTIPOCUOTA           = 'tipocuotawrk.html'
    HTML_WRKTIPODOCUMENTO       = 'tipodocumentowrk.html'
    HTML_WRKTIPOMONEDA          = 'tipomonedawrk.html'
    HTML_WRKTIPOMOVIMIENTO      = 'tipomovimientowrk.html'
    HTML_WRKTIPOORIGEN          = 'tipoorigenwrk.html'
    HTML_WRKTIPOPAGO            = 'tipopagowrk.html'
    HTML_WRKTIPOREGISTRO        = 'tiporegistrowrk.html'
    HTML_WRKTIPOSUBREGISTRO     = 'tiposubregistrowrk.html'
    HTML_WRKTIPOTITULAR         = 'tipotitularwrk.html'
    HTML_WRKAPITOKENUSER        = 'apitokenuserwrk.html'
    HTML_WRKAPIESTADOS          = 'apiestadoswrk.html'
    HTML_WRKAPITAREAS           = 'apitareaswrk.html'
    HTML_WRKAPITOKEN            = 'apitokenwrk.html'
    HTML_WRKAPIAUMOSO           = 'apiaumosowrk.html'

    # Render Paginas ADD, UPD
    HTML_ADDPROVINCIAS          = 'provinciaadd.html'
    HTML_ADDTIPOCUERPO          = 'tipocuerpoadd.html'
    HTML_ADDTIPOCUOTA           = 'tipocuotaadd.html'
    HTML_ADDTIPODOCUMENTO       = 'tipodocumentoadd.html'
    HTML_ADDTIPOESTADO          = 'tipoestadoadd.html'
    HTML_ADDTIPOMONEDA          = 'tipomonedaadd.html'
    HTML_ADDTIPOMOVIMIENTO      = 'tipomovimientoadd.html'
    HTML_ADDTIPOORIGEN          = 'tipoorigenadd.html'
    HTML_ADDTIPOPAGO            = 'tipopagoadd.html'
    HTML_ADDTIPOREGISTRO        = 'tiporegistroadd.html'
    HTML_ADDTIPOSUBREGISTRO     = 'tiposubregistroadd.html'
    HTML_ADDTIPOTITULAR         = 'tipotitularadd.html'
    HTML_ADDAPIESTADOS          = 'apiestadosadd.html'
    HTML_ADDAPITAREAS           = 'apitareasadd.html'
    HTML_ADDAPIREGISTROS        = 'apiregistrosadd.html'
    HTML_ADDAPITOKENUSER        = 'tokenuseradd.html'
    HTML_ADDAPITOKEN            = 'apitokenadd.html'

    HTML_UPDPROVINCIAS          = 'provinciaupd.html'



    PATH_EPAGOS_IMAGENES = "C:\\Epagos\\archivos_Estaticos\\Imagenes\\"
    URL_EPAGOS_MOSTRADOR = "http://172.16.5.105:5000/epagos/mostrador"
    HEADER_CONTENT_JSON = "!'Content-type',!'application/json'"

    JSON_AS_ASCII = False

    # Perfil de sucerp pepe1234
    SUCERP_USER = '1'
    SUCERP_PASS = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwc3ciOiJwZXBlMTIzNCIsImV4cCI6MTY1ODAwMDA4OX0.273VBib9P20wJ-zPMhN3MOu1znV4NCoyVGt7tVTkD5o'
    SUCERP_PASS_VALIDADO = {'psw': 'pepe1234', 'exp': 1658000089}

    # Errores sucerp
    ERROR_000 = { "code" : '*000',  "descripcion" : 'No hay error '}
    ERROR_401 = { "code" : '*401',  "descripcion" : 'El Usuario o Registro no Autorizado (id Registro) '}
    ERROR_402 = { "code" : '*402',  "descripcion" : 'El Usuario o Registro no Autorizado (id Usuario) '}
    ERROR_403 = { "code" : '*403',  "descripcion" : 'El Usuario o Registro no Autorizado (usuario) '}
    ERROR_404 = { "code" : '*404',  "descripcion" : 'El Usuario o Registro no Autorizado (password) '}
    ERROR_405 = {"code": '*405', "descripcion": 'El Contribuyente no Existe - transaccion finalizada'}
    ERROR_406 = {"code": '*406', "descripcion": 'La operacion no fue satisfactoria '}
    ERROR_407 = {"code": '*407', "descripcion": 'La operacion fue parcialmente satisfactoria '}
    ERROR_408 = {"code": '*408', "descripcion": 'El Contribuyente no tiene Deuda - transaccion finalizada '}
    ERROR_409 = {"code": '*409', "descripcion": 'Error de seguridad - Comuniquese con el area responsable - transaccion finalizada '}
    ERROR_410 = {"code": '*410', "descripcion": 'Error de seguridad - (pakey) - Comuniquese con el area responsable - transaccion finalizada '}
    ERROR_411 = {"code": '*411', "descripcion": 'Error de seguridad - Comuniquese con el area responsable - transaccion finalizada  '}
    ERROR_412 = {"code": '*412', "descripcion": 'La operacion de Pago o Cancelacion de Deuda fue Satisfactoria - Transaccion finalizada'}
    ERROR_413 = {"code": '*413', "descripcion": 'Error de seguridad - La operacion token ya ha sido utilizado'}
    ERROR_414 = {"code": '*414', "descripcion": 'Error el Registro no coinciden con el pedido solicitado'}
    ERROR_415 = {"code": '*415', "descripcion": 'Error en la Estructura Json'}
    # Atributos de la Tabla
    APITOKENUSER = 'APITOKENUSER'

    # Atributo unnitest
    TESTER_LCL = 'LCL'
    TESTER_RMT = 'RMT'

    # Directorio del Proyecto
    DIR_PROYECTO_LINUX = '/home/anovillo/Escritorio/ApiRest_Procesos_Prod/ApiRest_Procesos_Prod/app'
    DIR_PROYECTO_WINDOWS = 'C:\\Users\\anovillo\\Desktop\\ApiRest_Procesos_Prod\\app'

    DIR_PATH_IMAGENES_WINDOWS = f'{DIR_PROYECTO_WINDOWS}\\archivos_Estaticos\\Imagenes\\'
    DIR_PATH_ERRORES_WINDOWS = f'{DIR_PROYECTO_WINDOWS}\\archivos_Estaticos\\Errores\\'
    DIR_PATH_HOST_WINDOWS = f'{DIR_PROYECTO_WINDOWS}\\archivos_Estaticos\\Host\\'
    DIR_PATH_METODOS_WINDOWS = f'{DIR_PROYECTO_WINDOWS}\\archivos_Estaticos\\Metodos\\'
    DIR_PATH_TEMPLATES_WINDOWS = f'{DIR_PROYECTO_WINDOWS}\\templates\\'

    DIR_PATH_IMAGENES_LINUX = f'{DIR_PROYECTO_LINUX}/archivos_Estaticos/Imagenes/'
    DIR_PATH_ERRORES_LINUX = f'{DIR_PROYECTO_LINUX}/archivos_Estaticos/Errores/'
    DIR_PATH_HOST_LINUX = f'{DIR_PROYECTO_LINUX}/archivos_Estaticos/Host/'
    DIR_PATH_METODOS_LINUX = f'{DIR_PROYECTO_LINUX}/archivos_Estaticos/Metodos/'
    DIR_PATH_TEMPLATES_LINUX = f'{DIR_PROYECTO_LINUX}/templates/'

    URL_REDIRIGIR = 'https://www.google.com'

