# -------Lista de lisbrerias y Modulos
try:

    # ---------------LIBRERIAS DE FECHA Y HORA
    import datetime
    import copy

    # Tipo de dato decimal
    import decimal
    from app_Abstract.atributosAbstract import AtributosSucerp, AtributosGx

    from app_Config.config import ConfigurarAplicacion
    import pyodbc
    from pydal.adapters.db2 import DB2Pyodbc


    # --------------LIBRERIA PYDAL
    # --- PARA LA DEFINICION DE TABLAS Y LOS CAMPOS DE ELLAS
    from pydal import DAL, Field
    from pydal.objects import Table

except Exception as e:
    print(f'Falta algun modulo {e}')

"""
Son los Tipos de datos  y referencias para capa abstracta

types = {
    'boolean': 'CHAR(1)',
    'string': 'VARCHAR(%(length)s)',
    'text': 'CLOB',
    'json': 'CLOB',
    'password': 'VARCHAR(%(length)s)',
    'blob': 'BLOB',
    'upload': 'VARCHAR(%(length)s)',
    'integer': 'INT',
    'bigint': 'BIGINT',
    'float': 'REAL',
    'double': 'DOUBLE',
    'decimal': 'NUMERIC(%(precision)s,%(scale)s)',
    'date': 'DATE',
    'time': 'TIME',
    'datetime': 'TIMESTAMP',
    'id': 'INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL',
    'reference': 'INT, FOREIGN KEY (%(field_name)s) REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'list:integer': 'CLOB',
    'list:string': 'CLOB',
    'list:reference': 'CLOB',
    'big-id': 'BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL',
    'big-reference': 
        'BIGINT, FOREIGN KEY (%(field_name)s) REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'reference FK': 
        ', CONSTRAINT FK_%(constraint_name)s 
            FOREIGN KEY (%(field_name)s) 
            REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'reference TFK': 
        ' CONSTRAINT FK_%(foreign_table)s_PK 
            FOREIGN KEY (%(field_name)s) 
            REFERENCES %(foreign_table)s (%(foreign_key)s) ON DELETE %(on_delete_action)s',
    }
"""


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# El objetivo de esta clase es poder obtener el diccionario de un Objeto Tabla
class ToolsAbatract():
    """
    El objetivo de esta clase es poder recuperar los elmentos para poder gestionar las bases de datos:\n
        La key  de una tabla\n
        El registro a actualizar\n
        Los campos de la estructura de la Tabla\n
        Almacenado en gestion_Tablas_dict\n
    """

    def __init__(self):

        # Tabla
        self.__tabla = None

        # Campos del Mensaje
        self.__key = dict()
        self.__registro = dict()
        self.__campos = dict()

        # Gestion de las Tablas
        self.__gestion_Tablas_dict = dict()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Encapsulacion de los atributos

    # ----------DETERMINA EL CAMPOS ID DE LA TABLA--------------------------------
    @property
    def tabla(self):
        return self.__tabla

    @tabla.setter
    def tabla(self, valor):
        self.__tabla = valor
        self.__id_Tabla = self.__tabla._id.longname
        self.__id_Tabla = self.__id_Tabla[(self.__id_Tabla.find('.') + 1):]

    # ----------CAMPOS DE LA TABLAS--------------------------------
    @property
    def campos(self):
        return self.__campos

    @campos.setter
    def campos(self, valor):
        campos = valor
        for c in campos:
            if c != self.__id_Tabla:
                self.__campos[c] = None

    # ----KEY DE LAS TABLAS------------------------
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, valor):
        self.__key = valor

    # ----REGISTRO DE LAS TABLAS------------------------
    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, valor):
        self.__registro = valor

    # ----MENSAJE INSERT------------------------
    @property
    def mensaje_insert(self):
        self.__mensaje_insert = {'datos': self.registro}
        return self.__mensaje_insert

    # ----GESTION TABLAS------------------------
    @property
    def gestion_Tablas_dict(self):
        return self.__gestion_Tablas_dict

    @gestion_Tablas_dict.setter
    def gestion_Tablas_dict(self, valor):
        self.__gestion_Tablas_dict = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Obtiene el diccionario de manejo de la tabla
    def getTableTools(self, tabla):

        if type(tabla) is Table:
            self.tabla = tabla
            self.campos = tabla.fields()
            self.key, self.registro = {self.__id_Tabla: None}, self.campos
            self.gestion_Tablas_dict[tabla._id.tablename] = dict()
            self.gestion_Tablas_dict[tabla._id.tablename]['table'] = tabla
            self.gestion_Tablas_dict[tabla._id.tablename]['campos'] = self.campos
            self.gestion_Tablas_dict[tabla._id.tablename]['insert'] = self.mensaje_insert
            self.gestion_Tablas_dict[tabla._id.tablename]['update'] = {'clave': self.key, 'registro': self.registro}
            self.gestion_Tablas_dict[tabla._id.tablename]['update'] = {'clave': self.key}
            return self.gestion_Tablas_dict


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# El objetivo de esta clase es poder describir los campos de cada tabla que estan en motor SQLITE
class SqliteAbstractDb():

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA GXPROD.USERPATHFILE  
    #     TABLA GXPROD.MSGNIVELGRAVEDAD
    #     TABLA GXPROD.MENSAJESERROR
    #     TABLA GXPROD.MENSAJESERRORMSGDINAMICOS
    #     TABLA GXPROD.IMPRESIONPDF


    def __init__(self, db):

        # Conexion
        self.db = db

        # ------------------------------------------------------
        # Tablas del Validator
        self.__mensajesError = None
        self.__mensajesErrorMsgdDinamicos = None
        self.__msgNivelGravedad = None
        self.__userPathFile = None
        self.__usuario = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TABLA USERPATHFILE
    #     FOR SYSTEM NAME USERP00001------------------------
    @property
    def sq_userPathFile_Dal(self):
        if self.__userPathFile is None:
            try:
                self.__userPathFile = self.db.define_table(
                    'USERPATHFILE',
                    Field('USERPATHFILEID', type='id', label='Id'),
                    Field('USERNAME', type='string', length=10, required=True, label='Nombre Usuario'),
                    Field('USERPATHFILEMODULO', type='string', length=50, required=True, label='Modulo del Usuario'),
                    Field('USERPATHFILEPATH', type='string', length=50, required=True, label='Path de Files'),
                    Field('USEROUTPUT', type='string', length=1, required=True, label='OutPut'),
                    Field('USERLINKPROD', type='string', length=512, required=True, label='User Link Prod'),
                    Field('USERLINKTEST', type='string', length=512, required=True, label='User Link Test'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__userPathFile

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TABLA GXPROD.MSGNIVELGRAVEDAD
    #     FOR SYSTEM NAME MSGNI00001------------------------
    @property
    def sq_msgNivelGravedad_Dal(self):
        if self.__msgNivelGravedad is None:
            try:
                self.__msgNivelGravedad = self.db.define_table(
                    'MSGNIVELGRAVEDAD',
                    Field('NIVELGRAVEDADID', type='id', label='Id'),
                    Field('NIVELGRAVEDADDESCRIPCION', type='string', length=50, required=True, label='Descripcion'),
                    Field('MSGNIVELGRAVEDADALERTA', type='string', length=50, required=True, label='Ayuda Mensaje'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__msgNivelGravedad

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TABLA GXPROD.MENSAJESERROR
    #     FOR SYSTEM NAME MENSA00001------------------------
    @property
    def sq_mensajeError_Dal(self):
        if self.__mensajesError is None:
            try:
                self.__mensajesError = self.db.define_table(
                    'MENSAJESERROR',
                    Field('MSGCODE', type='string', length=7, required=True, label='Mensaje Codigo'),
                    Field('MSGDESCRIPCION', type='string', length=150, required=True, label='Descripcion'),
                    Field('MSGHELP', type='string', length=1024, required=True, label='Ayuda Mensaje'),
                    Field('NIVELGRAVEDADID', 'reference MSGNIVELGRAVEDAD', label='Id', ondelete='CASCADE'),
                    primarykey=['MSGCODE'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesError

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TABLA GXPROD.MENSAJESERRORMSGDINAMICOS
    #     FOR SYSTEM NAME MENSA00002------------------------
    @property
    def sq_mensajesErrorMsgdDinamicos_Dal(self):
        if self.__mensajesErrorMsgdDinamicos is None:
            try:
                self.__mensajesErrorMsgdDinamicos = self.db.define_table(
                    'MENSAJESERRORMSGDINAMICOS',
                    Field('MSGCODE', type='integer', required=True, label='Codigo del Mensaje'),
                    Field('MSGDINAMICOID', type='integer', required=True, label='Mensaje Dinamico Id'),
                    Field('MSGDINAMICOLEN', type='integer', required=True, label='Ayuda Mensaje'),
                    primarykey=['MSGCODE', 'MSGDINAMICOID'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesErrorMsgdDinamicos


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class GxAbstractDb():
    """
    EL OBJTIVO DE ESTA CLASE ES PODER DESCRIBIR LOS CAMPOS DE LAS TABLAS QUE ESTAN EN EL MOTOR ISERIES O MYSQL \n
    EN EL CASO DEL ISERIES LAS TABLAS ESTAN EN LA BIBLIOTECA GXPROD O GXTST DE ACUERDO A LA CONFIGURACION \n
    CUANDO TRABAJAMOS SIN CONEXION A LA ISERIES SE TRABAJA CON MYSQL \n

    """
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA PROCESOIMPORTACIONEXPORTACION
    #     TABLA TIPOMOVIMIENTO
    #     TABLA ENCABEZADO
    #     TABLA TIPOREGISTRO
    #     TABLA TIPORSUBEGISTRO
    #     TABLA TIPOCUERPO
    #     TABLA TIPOTITULAR
    #     TABLA TIPOORIGEN
    #     TABLA TIPOCUOTA
    #     TABLA TIPOPAGO
    #     TABLA TIPOMONEDA
    #     TABLA TIPODOCUMENTO
    #     TABLA PROVINCIAS
    #     TABLA ESTADO
    #     TABLA RELACIONARBASUCERPMARCA
    #     TABLA ALTAIMPOSITIVA
    #     TABLA ALTAIMPOSITIVATITULAR
    #     TABLA ANULACIONTRAMITESSELLOS
    #     TABLA ANULACIONTRAMITESSELLOSDETALLE
    #     TABLA APIESTADOS
    #     TABLA APITAREAS
    #     TABLA APIESTADOSTAREAS
    #     TABLA APIREGISTROS
    #     TABLA APITOKENUSER
    #     TABLA APILOG
    #     TABLA APITOKEN
    #     TABLA BAJAIMPOSITIVA
    #     TABLA BAJAIMPOSITIVATITULAR
    #     TABLA CAMBIOTITULARIDAD
    #     TABLA CAMBIOTITULARIDADTITULAR
    #     TABLA IMPUESTOAUTOMOTOR
    #     TABLA IMPUESTOSELLOS
    #     TABLA IMPUESTOSELLOSPARTES
    #     TABLA IMPUESTOSELLOSPARTESTIPOTRAMITE
    #     TABLA INFORMACIONVEHICULO
    #     TABLA TMPINFORMACIONVEHICULO
    #     TABLA INFORMACIONVEHICULOTITULAR
    #     TABLA TMPINFORMACIONVEHICULOTITULAR
    #     TABLA INFORMACIORADICACION
    #     TABLA TRAMITESGENERALES
    #     TABLA TRAMITESGENERALESTITULARES
    #     TABLA PIE
    #     TABLA APIAUMOSO
    #     TABLA GXPROD.MSGNIVELGRAVEDAD
    #     TABLA GXPROD.MENSAJESERROR
    #     TABLA GXPROD.MENSAJESERRORMSGDINAMICOS
    #     TABLA GXPROD.IMPRESIONPDF
    #     TABLA RECEPLOG
    #     TABLA RECEPCIONTEXTO
    #     TABLA RECEPCIONARCHIVOS  

    def __init__(self, db):

        # Conexion
        self.db = db

        # Formatos
        self.formatosSucerp = AtributosSucerp()

        # diccionario de objetos tablas
        self.__GxdictObjetosTablas = dict()

        # ------------------------------------------------------
        # Tablas de GxProd

        self.__tipoRegistro = None
        self.__tipoSubRegistro = None
        self.__tipoCuerpo = None
        self.__tipoTitular = None
        self.__tipoOrigen = None
        self.__tipoMovimiento = None
        self.__tipoCuota = None
        self.__tipoPago = None
        self.__tipoMoneda = None
        self.__tipoDocumento = None
        self.__provincias = None
        self.__estado = None
        self.__encabezado = None

        self.__altaImpositiva = None
        self.__altaImpositivaTitular = None
        self.__bajaImpositiva = None
        self.__bajaImpositivaTitular = None
        self.__impuestoSellos = None
        self.__impuestoSellosPartes = None
        self.__impuestoSellosPartesTipoTramite = None
        self.__impuestoAutomotor = None

        self.__informacionVehiculo = None
        self.__informacionVehiculoTitular = None
        self.__cambioTitularidad = None
        self.__cambioTitularidadTitular = None
        self.__informacionRadicacion = None
        self.__anulacionTramitesSellos = None
        self.__anulacionTramitesSellosDetalle = None
        self.__tramitesGenerales = None
        self.__tramitesGeneralesTitular = None
        self.__pie = None

        self.__apiAumoso = None
        self.__apiToken = None
        self.__apiTokenUser = None
        self.__apiTokenUserRef = list()
        self.__apiRegistros = None
        self.__apiEstados = None
        self.__apiTareas = None
        self.__apiEstadosTareas = None
        self.__relArbaSucerpMarca = None
        self.__procesoImportacionExportacion = None
        self.__apiLog = None

        self.__tmpInformacionVehiculo = None
        self.__tmpInformacionVehiculoTitular = None

        self.__recepLog = None
        self.__recepcionTexto = None
        self.__recepcionArchivos = None


    # ----Atributos------------------------
    @property
    def recepcionTexto(self):
        return self.__recepcionTexto

    @recepcionTexto.setter
    def recepcionTexto(self, valor):
        self.__recepcionTexto = valor

    @property
    def recepLog(self):
        return self.__recepLog

    @recepLog.setter
    def recepLog(self, valor):
        self.__recepLog = valor

    @property
    def recepcionArchivos(self):
        return self.__recepcionArchivos

    @recepcionArchivos.setter
    def recepcionArchivos(self, valor):
        self.__recepcionArchivos = valor

    @property
    def encabezado(self):
        return self.__encabezado

    @encabezado.setter
    def encabezado(self, valor):
        self.__encabezado = valor

    @property
    def tipoRegistro(self):
        return self.__tipoRegistro

    @tipoRegistro.setter
    def tipoRegistro(self, valor):
        self.__tipoRegistro = valor

    @property
    def tipoSubRegistro(self):
        return self.__tipoSubRegistro

    @tipoSubRegistro.setter
    def tipoSubRegistro(self, valor):
        self.__tipoSubRegistro = valor

    @property
    def tipoCuerpo(self):
        return self.__tipoCuerpo

    @tipoCuerpo.setter
    def tipoCuerpo(self, valor):
        self.__tipoCuerpo = valor

    @property
    def tipoTitular(self):
        return self.__tipoTitular

    @tipoTitular.setter
    def tipoTitular(self, valor):
        self.__tipoTitular = valor

    @property
    def tipoOrigen(self):
        return self.__tipoOrigen

    @tipoOrigen.setter
    def tipoOrigen(self, valor):
        self.__tipoOrigen = valor

    @property
    def tipoMovimiento(self):
        return self.__tipoMovimiento

    @tipoMovimiento.setter
    def tipoMovimiento(self, valor):
        self.__tipoMovimiento = valor

    @property
    def tipoCuota(self):
        return self.__tipoCuota

    @tipoCuota.setter
    def tipoCuota(self, valor):
        self.__tipoCuota = valor

    @property
    def tipoPago(self):
        return self.__tipoPago

    @tipoPago.setter
    def tipoPago(self, valor):
        self.__tipoPago = valor

    @property
    def tipoMoneda(self):
        return self.__tipoMoneda

    @tipoMoneda.setter
    def tipoMoneda(self, valor):
        self.__tipoMoneda = valor

    @property
    def tipoDocumento(self):
        return self.__tipoDocumento

    @tipoDocumento.setter
    def tipoDocumento(self, valor):
        self.__tipoDocumento = valor

    @property
    def provincias(self):
        return self.__provincias

    @provincias.setter
    def provincias(self, valor):
        self.__provincias = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def altaImpositiva(self):
        return self.__altaImpositiva

    @altaImpositiva.setter
    def altaImpositiva(self, valor):
        self.__altaImpositiva = valor

    @property
    def altaImpositivaTitular(self):
        return self.__altaImpositivaTitular

    @altaImpositivaTitular.setter
    def altaImpositivaTitular(self, valor):
        self.__altaImpositivaTitular = valor

    @property
    def bajaImpositiva(self):
        return self.__bajaImpositiva

    @bajaImpositiva.setter
    def bajaImpositiva(self, valor):
        self.__bajaImpositiva = valor

    @property
    def bajaImpositivaTitular(self):
        return self.__bajaImpositivaTitular

    @bajaImpositivaTitular.setter
    def bajaImpositivaTitular(self, valor):
        self.__bajaImpositivaTitular = valor

    @property
    def impuestoSellos(self):
        return self.__impuestoSellos

    @impuestoSellos.setter
    def impuestoSellos(self, valor):
        self.__impuestoSellos = valor

    @property
    def impuestoSellosPartes(self):
        return self.__impuestoSellosPartes

    @impuestoSellosPartes.setter
    def impuestoSellosPartes(self, valor):
        self.__impuestoSellosPartes = valor

    @property
    def impuestoSellosPartesTipoTramite(self):
        return self.__impuestoSellosPartesTipoTramite

    @impuestoSellosPartesTipoTramite.setter
    def impuestoSellosPartesTipoTramite(self, valor):
        self.__impuestoSellosPartesTipoTramite = valor

    @property
    def impuestoAutomotor(self):
        return self.__impuestoAutomotor

    @impuestoAutomotor.setter
    def impuestoAutomotor(self, valor):
        self.__impuestoAutomotor = valor

    @property
    def informacionVehiculo(self):
        return self.__informacionVehiculo

    @informacionVehiculo.setter
    def informacionVehiculo(self, valor):
        self.__informacionVehiculo = valor

    @property
    def informacionVehiculoTitular(self):
        return self.__informacionVehiculoTitular

    @informacionVehiculoTitular.setter
    def informacionVehiculoTitular(self, valor):
        self.__informacionVehiculoTitular = valor

    @property
    def tmpInformacionVehiculo(self):
        return self.__tmpInformacionVehiculo

    @tmpInformacionVehiculo.setter
    def tmpInformacionVehiculo(self, valor):
        self.__tmpInformacionVehiculo = valor

    @property
    def tmpInformacionVehiculoTitular(self):
        return self.__tmpInformacionVehiculoTitular

    @tmpInformacionVehiculoTitular.setter
    def tmpInformacionVehiculoTitular(self, valor):
        self.__tmpInformacionVehiculoTitular = valor

    @property
    def cambioTitularidad(self):
        return self.__cambioTitularidad

    @cambioTitularidad.setter
    def cambioTitularidad(self, valor):
        self.__cambioTitularidad = valor

    @property
    def cambioTitularidadTitular(self):
        return self.__cambioTitularidadTitular

    @cambioTitularidadTitular.setter
    def cambioTitularidadTitular(self, valor):
        self.__cambioTitularidadTitular = valor

    @property
    def informacionRadicacion(self):
        return self.__informacionRadicacion

    @informacionRadicacion.setter
    def informacionRadicacion(self, valor):
        self.__informacionRadicacion = valor

    @property
    def anulacionTramitesSellos(self):
        return self.__anulacionTramitesSellos

    @anulacionTramitesSellos.setter
    def anulacionTramitesSellos(self, valor):
        self.__anulacionTramitesSellos = valor

    @property
    def anulacionTramitesSellosDetalle(self):
        return self.__anulacionTramitesSellosDetalle

    @anulacionTramitesSellosDetalle.setter
    def anulacionTramitesSellosDetalle(self, valor):
        self.__anulacionTramitesSellosDetalle = valor

    @property
    def tramitesGenerales(self):
        return self.__tramitesGenerales

    @tramitesGenerales.setter
    def tramitesGenerales(self, valor):
        self.__tramitesGenerales = valor

    @property
    def tramitesGeneralesTitular(self):
        return self.__tramitesGeneralesTitular

    @tramitesGeneralesTitular.setter
    def tramitesGeneralesTitular(self, valor):
        self.__tramitesGeneralesTitular = valor

    @property
    def pie(self):
        return self.__pie

    @pie.setter
    def pie(self, valor):
        self.__pie = valor

    @property
    def apiAumoso(self):
        return self.__apiAumoso

    @apiAumoso.setter
    def apiAumoso(self, valor):
        self.__apiAumoso = valor

    @property
    def apiToken(self):
        return self.__apiToken

    @apiToken.setter
    def apiToken(self, valor):
        self.__apiToken = valor

    @property
    def apiTokenUser(self):
        return self.__apiTokenUser

    @apiTokenUser.setter
    def apiTokenUser(self, valor):
        self.__apiTokenUser = valor

    @property
    def apiTokenUserRef(self):
        return self.__apiTokenUserRef

    @apiTokenUserRef.setter
    def apiTokenUserRef(self, valor):
        self.__apiTokenUserRef = valor

    @property
    def apiRegistros(self):
        return self.__apiRegistros

    @apiRegistros.setter
    def apiRegistros(self, valor):
        self.__apiRegistros = valor

    @property
    def apiEstados(self):
        return self.__apiEstados

    @apiEstados.setter
    def apiEstados(self, valor):
        self.__apiEstados = valor

    @property
    def apiTareas(self):
        return self.__apiTareas

    @apiTareas.setter
    def apiTareas(self, valor):
        self.__apiTareas = valor

    @property
    def apiEstadosTareas(self):
        return self.__apiEstadosTareas

    @apiEstadosTareas.setter
    def apiEstadosTareas(self, valor):
        self.__apiEstadosTareas = valor

    @property
    def relArbaSucerpMarca(self):
        return self.__relArbaSucerpMarca

    @relArbaSucerpMarca.setter
    def relArbaSucerpMarca(self, valor):
        self.__relArbaSucerpMarca = valor

    @property
    def procesoImportacionExportacion(self):
        return self.__procesoImportacionExportacion

    @procesoImportacionExportacion.setter
    def procesoImportacionExportacion(self, valor):
        self.__procesoImportacionExportacion = valor

    @property
    def apiLog(self):
        return self.__apiLog

    @apiLog.setter
    def apiLog(self, valor):
        self.__apiLog = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA PROCESOIMPORTACIONEXPORTACION
    #     FOR SYSTEM NAME ------------------------
    @property
    def procesoImportacionExportacion_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.procesoImportacionExportacion is None:

                # realizamos la construccion de la tabla
                self.procesoImportacionExportacion = self.__buildTable(
                                self.formatosSucerp.tablaProcesoImportacionExportacion())

            return self.procesoImportacionExportacion
        
        except Exception as inst:
            print(f'Error - procesoImportacionExportacion_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOMOVIMIENTO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoMovimiento_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoMovimiento is None:

                # realizamos la construccion de la tabla
                self.tipoMovimiento = self.__buildTable(self.formatosSucerp.tablaTipoMovimiento())

            return self.tipoMovimiento
        
        except Exception as inst:
            print(f'Error - tipoMovimiento_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ENCABEZADO
    #     FOR SYSTEM NAME ------------------------
    @property
    def encabezado_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.encabezado is None:

                # realizamos la construccion de la tabla
                self.encabezado = self.__buildTable(self.formatosSucerp.tablaEncabezado())

            return self.encabezado
        
        except Exception as inst:
            print(f'Error - encabezado_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOREGISTRO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoRegistro_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoRegistro is None:

                # realizamos la construccion de la tabla
                self.tipoRegistro = self.__buildTable(self.formatosSucerp.tablaTipoRegistro())

            return self.tipoRegistro
        
        except Exception as inst:
            print(f'Error - tipoRegistro_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPORSUBEGISTRO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoSubRegistro_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoSubRegistro is None:

                # realizamos la construccion de la tabla
                self.tipoSubRegistro = self.__buildTable(self.formatosSucerp.tablaTipoSubRegistro())

            return self.tipoSubRegistro
        
        except Exception as inst:
            print(f'Error - tipoSubRegistro_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOCUERPO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoCuerpo_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoCuerpo is None:

                # realizamos la construccion de la tabla
                self.tipoCuerpo = self.__buildTable(self.formatosSucerp.tablaTipoCuerpo())

            return self.tipoCuerpo
        
        except Exception as inst:
            print(f'Error - tipoCuerpo_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOTITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoTitular_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoTitular is None:

                # realizamos la construccion de la tabla
                self.tipoTitular = self.__buildTable(self.formatosSucerp.tablaTipoTitular())

            return self.tipoTitular
        
        except Exception as inst:
            print(f'Error - tipoTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOORIGEN
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoOrigen_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoOrigen is None:

                # realizamos la construccion de la tabla
                self.tipoOrigen = self.__buildTable(self.formatosSucerp.tablaTipoOrigen())

            return self.tipoOrigen
        
        except Exception as inst:
            print(f'Error - tipoOrigen_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOCUOTA
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoCuota_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoCuota is None:

                # realizamos la construccion de la tabla
                self.tipoCuota = self.__buildTable(self.formatosSucerp.tablaTipoCuota())

            return self.tipoCuota
        
        except Exception as inst:
            print(f'Error - tipoCuota_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOPAGO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoPago_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoPago is None:

                # realizamos la construccion de la tabla
                self.tipoPago = self.__buildTable(self.formatosSucerp.tablaTipoPago())

            return self.tipoPago
        
        except Exception as inst:
            print(f'Error - tipoPago_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOMONEDA
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoMoneda_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoMoneda is None:

                # realizamos la construccion de la tabla
                self.tipoMoneda = self.__buildTable(self.formatosSucerp.tablaTipoMoneda())

            return self.tipoMoneda
        
        except Exception as inst:
            print(f'Error - tipoMoneda_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPODOCUMENTO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoDocumento_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tipoDocumento is None:

                # realizamos la construccion de la tabla
                self.tipoDocumento = self.__buildTable(self.formatosSucerp.tablaTipoDocumento())

            return self.tipoDocumento

        except Exception as inst:
            print(f'Error - tipoDocumento_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA PROVINCIAS
    #     FOR SYSTEM NAME ------------------------
    @property
    def provincias_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.provincias is None:

                # realizamos la construccion de la tabla
                self.provincias = self.__buildTable(self.formatosSucerp.tablaProvincias())

            return self.provincias

        except Exception as inst:
            print(f'Error - provincias_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ESTADO
    #     FOR SYSTEM NAME ------------------------
    @property
    def estado_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.estado is None:

                # realizamos la construccion de la tabla
                self.estado = self.__buildTable(self.formatosSucerp.tablaEstado())

            return self.estado

        except Exception as inst:
            print(f'Error - estado_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA RELACIONARBASUCERPMARCA
    #     FOR SYSTEM NAME ------------------------
    @property
    def relArbaSucerpMarca_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.relArbaSucepMarca is None:

                # realizamos la construccion de la tabla
                self.relArbaSucepMarca = self.__buildTable(
                            self.formatosSucerp.tablaRelArbaSucerpMarca())

            return self.relArbaSucepMarca

        except Exception as inst:
            print(f'Error - relArbaSucerpMarca_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ALTAIMPOSITIVATITULAR
    #     FOR SYSTEM NAME ALTAI00001
    @property
    def altaImpositivaTitular_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.altaImpositivaTitular is None:

                # Referencias a tipos de cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Referencias a tipos de sub registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # realizamos la construccion de la tabla
                self.altaImpositivaTitular = self.__buildTable(
                              self.formatosSucerp.tablaAltaImpositivaTitular())

                # Tablas de referencias
                self.altaImpositivaTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias
                ]

            return self.altaImpositivaTitular

        except Exception as inst:
            print(f'Error - altaImpositivaTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ALTAIMPOSITIVA
    #     FOR SYSTEM NAME ALTAI00002
    @property
    def altaImpositiva_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.altaImpositiva is None:

                # Referencias a tipos de registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de sub registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Referencias a tipos de documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # Referencias a altasimpositivatitular
                if self.altaImpositivaTitular is None:
                    self.altaImpositivaTitular = self.altaImpositivaTitular_Dal

                # realizamos la construccion de la tabla
                self.altaImpositiva = self.__buildTable(self.formatosSucerp.tablaAltaImpositiva())

                # Tablas de referencias
                self.altaImpositiva._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro,
                    self.tipoOrigen, self.tipoDocumento, self.provincias,
                    self.altaImpositivaTitular
                ]

            return self.altaImpositiva

        except Exception as inst:
            print(f'Error - altaImpositiva_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ANULACIONTRAMITESSELLOS
    #     FOR SYSTEM NAME ANULA00001
    @property
    def anulacionTramitesSellos_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.anulacionTramitesSellos is None:

                # Referencias a tipos de registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de sub registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Referencia a tipos de Pago
                if self.tipoPago is None:
                    self.tipoPago = self.tipoPago_Dal

                # Referencia a tipos de Moneda
                if self.tipoMoneda is None:
                    self.tipoMoneda = self.tipoMoneda_Dal

                # realizamos la construccion de la tabla
                self.anulacionTramitesSellos = self.__buildTable(
                              self.formatosSucerp.tablaAnulacionTramitesSellos())

                # Tablas de referencias
                self.anulacionTramitesSellos._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.tipoPago, 
                    self.tipoMoneda
                ]

            return self.anulacionTramitesSellos

        except Exception as inst:
            print(f'Error - anulacionTramitesSellos_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ANULACIONTRAMITESSELLOSDETALLE
    #     FOR SYSTEM NAME ANULA00002
    @property
    def anulacionTramitesSellosDetalle_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.anulacionTramitesSellosDetalle is None:

                # Referencias a tipos de registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de sub registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencia a tipos de Moneda
                if self.tipoCuota is None:
                    self.tipoCuota = self.tipoCuota_Dal

                # Referencia a anulaciontramitesellos
                if self.anulacionTramitesSellos is None:
                    self.anulacionTramitesSellos = self.anulacionTramitesSellos_Dal

                # realizamos la construccion de la tabla
                self.anulacionTramitesSellosDetalle = self.__buildTable(
                                self.formatosSucerp.tablaAnulacionTramitesSellosDetalle())

                # Tablas de referencias
                self.anulacionTramitesSellosDetalle._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoCuota, self.anulacionTramitesSellos
                ]

            return self.anulacionTramitesSellosDetalle

        except Exception as inst:
            print(f'Error - anulacionTramitesSellosDetalle_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APIESTADOS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiEstados_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiEstados is None:

                # realizamos la construccion de la tabla
                self.apiEstados = self.__buildTable(self.formatosSucerp.tablaApiEstados())

            return self.apiEstados

        except Exception as inst:
            print(f'Error - apiEstados_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APITAREAS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiTareas_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiTareas is None:

                # realizamos la construccion de la tabla
                self.apiTareas = self.__buildTable(self.formatosSucerp.tablaApiTareas())

            return self.apiTareas

        except Exception as inst:
            print(f'Error - apiTareas_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APIESTADOSTAREAS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiEstadosTareas_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiEstadosTareas is None:

                # Referencia a api Estados
                if self.apiEstados is None:
                    self.apiEstados = self.apiEstados_Dal

                # Referencia a api Tareas
                if self.apiTareas is None:
                    self.apiTareas = self.apiTareas_Dal

                # realizamos la construccion de la tabla
                self.apiEstadosTareas = self.__buildTable(
                            self.formatosSucerp.tablaApiEstadosTareas())

                # Tablas de referencias
                self.apiEstadosTareas._referenced_by_list = [
                    self.apiEstados, self.apiTareas
                ]

            return self.apiEstadosTareas

        except Exception as inst:
            print(f'Error - apiEstadosTareas_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APIREGISTROS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiRegistros_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiRegistros is None:

                # Referencia a api Estados Tareas
                if self.apiEstadosTareas is None:
                    self.apiEstadosTareas = self.apiEstadosTareas_Dal

                # realizamos la construccion de la tabla
                self.apiRegistros = self.__buildTable(self.formatosSucerp.tablaApiRegistros())

                # Tablas de referencias
                self.apiRegistros._referenced_by_list = [self.apiEstadosTareas]

            return self.apiRegistros

        except Exception as inst:
            print(f'Error - apiRegistros_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APITOKENUSER
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiTokenUser_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiTokenUser is None:

                # Tabla de Tipo de Documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla ref APIREGISTROS
                if self.apiRegistros is None:
                    self.apiRegistros = self.apiRegistros_Dal

                # realizamos la construccion de la tabla
                self.apiTokenUser = self.__buildTable(self.formatosSucerp.tablaApiTokenUser())

                # Tablas de referencias
                self.apiTokenUser._referenced_by_list = [self.tipoDocumento, self.apiRegistros]

            return self.apiTokenUser

        except Exception as inst:
            print(f'Error - apiRegistros_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APILOG
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiLog_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiLog is None:

                # realizamos la construccion de la tabla
                self.apiLog = self.__buildTable(self.formatosSucerp.tablaApiLog())

            return self.apiLog

        except Exception as inst:
            print(f'Error - apiLog_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APITOKEN
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiToken_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiToken is None:

                # Tabla ref api Token User
                if self.apiTokenUser is None:
                    self.apiTokenUser = self.apiTokenUser_Dal

                # Tabla ref api Registros
                if self.__apiRegistros is None:
                    self.__apiRegistros = self.apiRegistros_Dal

                # Referencia a api Estados Tareas
                if self.apiEstadosTareas is None:
                    self.apiEstadosTareas = self.apiEstadosTareas_Dal

                # realizamos la construccion de la tabla
                if self.apiToken is None:
                    self.apiToken = self.__buildTable(self.formatosSucerp.tablaApiToken())

                # Tablas de referencias
                self.apiToken._referenced_by_list = [
                    self.apiTokenUser, self.apiRegistros, 
                    self.apiEstadosTareas
                ]

            return self.apiToken

        except Exception as inst:
            print(f'Error - apiToken_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA BAJAIMPOSITIVA
    #     FOR SYSTEM NAME BAJAI00002
    @property
    def bajaImpositiva_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.bajaImpositiva is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla bajaimpositivatitular
                if self.bajaImpositivaTitular is None:
                    self.bajaImpositivaTitular = self.bajaImpositivaTitular_Dal

                # realizamos la construccion de la tabla
                self.bajaImpositiva = self.__buildTable(
                            self.formatosSucerp.tablaBajaImpositiva())

                # Tablas de referencias
                self.bajaImpositiva._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.bajaImpositivaTitular
                ]

            return self.bajaImpositiva

        except Exception as inst:
            print(f'Error - bajaImpositiva_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA BAJAIMPOSITIVATITULAR
    #     FOR SYSTEM NAME BAJAI00001
    @property
    def bajaImpositivaTitular_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.bajaImpositivaTitular is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # realizamos la construccion de la tabla
                self.bajaImpositivaTitular = self.__buildTable(
                                self.formatosSucerp.tablaBajaImpositivaTitular())

                # Tablas de referencias
                self.bajaImpositivaTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias
                ]
            return self.bajaImpositivaTitular

        except Exception as inst:
            print(f'Error - bajaImpositivaTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA CAMBIOTITULARIDAD
    #     FOR SYSTEM NAME CAMBI00003
    @property
    def cambioTitularidad_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.cambioTitularidad is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Referencias a tipos de documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # Referencias a cambiotitularidadtitular
                if self.cambioTitularidadTitular is None:
                    self.cambioTitularidadTitular = self.cambioTitularidadTitular_Dal


                # realizamos la construccion de la tabla
                self.cambioTitularidad = self.__buildTable(
                                self.formatosSucerp.tablaCambioTitularidad())

                # Tablas de referencias
                self.cambioTitularidad._referenced_by_list = [
                    self.tipoRegistro, self.tipoCuerpo, 
                    self.tipoSubRegistro, self.tipoDocumento, 
                    self.provincias, self.cambioTitularidadTitular
                ]

            return self.cambioTitularidad

        except Exception as inst:
            print(f'Error - cambioTitularidad_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA CAMBIOTITULARIDADTITULAR
    #     FOR SYSTEM NAME CAMBI00002
    @property
    def cambioTitularidadTitular_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.cambioTitularidadTitular is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Titular
                if self.tipoTitular is None:
                    self.tipoTitular = self.tipoTitular_Dal

                # Referencias a tipos de documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # realizamos la construccion de la tabla
                self.cambioTitularidadTitular = self.__buildTable(
                                self.formatosSucerp.tablaCambioTitularidadTitular())

                # Tablas de referencias
                self.cambioTitularidadTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoTitular, self.tipoDocumento, 
                    self.provincias
                ]

            return self.cambioTitularidadTitular

        except Exception as inst:
            print(f'Error - cambioTitularidadTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA IMPUESTOAUTOMOTOR
    #     FOR SYSTEM NAME IMPUE00004
    @property
    def impuestoAutomotor_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.impuestoAutomotor is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Movimeinto
                if self.tipoMovimiento is None:
                    self.tipoMovimiento = self.tipoMovimiento_Dal

                # Tabla tipo de Registro
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de Pago
                if self.tipoPago is None:
                    self.tipoPago = self.tipoPago_Dal

                # Referencias a tipos de Monedas
                if self.tipoMoneda is None:
                    self.tipoMoneda = self.tipoMoneda_Dal

                # realizamos la construccion de la tabla
                self.impuestoAutomotor = self.__buildTable(
                            self.formatosSucerp.tablaImpuestoAutomotor())

                # Tablas de referencias
                self.impuestoAutomotor._referenced_by_list = [
                    self.tipoCuerpo, self.tipoMovimiento, 
                    self.tipoRegistro, self.tipoPago, 
                    self.tipoMoneda
                ]

            return self.impuestoAutomotor

        except Exception as inst:
            print(f'Error - impuestoAutomotor_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA IMPUESTOSELLOS
    #     FOR SYSTEM NAME IMPUE00001
    @property
    def impuestoSellos_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.impuestoSellos is None:

                # Tabla tipo de Registro
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla tipo de Pago
                if self.tipoPago is None:
                    self.tipoPago = self.tipoPago_Dal

                # Tabla tipo de Moneda
                if self.tipoMoneda is None:
                    self.tipoMoneda = self.tipoMoneda_Dal

                # realizamos la construccion de la tabla
                self.impuestoSellos = self.__buildTable(
                            self.formatosSucerp.tablaImpuestosSellos())

                # Tablas de referencias
                self.impuestoSellos._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.tipoPago, 
                    self.tipoMoneda
                ]

            return self.impuestoSellos

        except Exception as inst:
            print(f'Error - impuestoSellos_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA IMPUESTOSELLOSPARTES
    #     FOR SYSTEM NAME IMPUE00002
    @property
    def impuestoSellosPartes_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.impuestoSellosPartes is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de Provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # realizamos la construccion de la tabla
                self.impuestoSellosPartes = self.__buildTable(
                            self.formatosSucerp.tablaImpuestosSellosPartes())

                # Tablas de referencias
                self.impuestoSellosPartes._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias
                ]

            return self.impuestoSellosPartes

        except Exception as inst:
            print(f'Error - impuestoSellosPartes_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA IMPUESTOSELLOSPARTESTIPOTRAMITE
    #     FOR SYSTEM NAME IMPUE00003
    @property
    def impuestoSellosPartesTipoTramite_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.impuestoSellosPartesTipoTramite is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # realizamos la construccion de la tabla
                self.impuestoSellosPartesTipoTramite = self.__buildTable(
                                self.formatosSucerp.tablaImpuestosSellosPartesTipoTramite())

                # Tablas de referencias
                self.impuestoSellosPartesTipoTramite._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro
                ]

            return self.impuestoSellosPartesTipoTramite

        except Exception as inst:
            print(f'Error - impuestoSellosPartesTipoTramite_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA INFORMACIONVEHICULO
    #     FOR SYSTEM NAME INFOR00001
    @property
    def informacionVehiculo_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.informacionVehiculo is None:

                # Tabla tipo de Registro
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # realizamos la construccion de la tabla
                self.informacionVehiculo = self.__buildTable(
                            self.formatosSucerp.tablaInformacionVehiculo())

                # Tablas de referencias
                self.informacionVehiculo._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.provincias
                ]

            return self.informacionVehiculo

        except Exception as inst:
            print(f'Error - informacionVehiculo_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TMPINFORMACIONVEHICULO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tmpInformacionVehiculo_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tmpInformacionVehiculo is None:

                # Tabla tipo de Registro
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # realizamos la construccion de la tabla
                self.tmpInformacionVehiculo = self.__buildTable(
                            self.formatosSucerp.tablaTmpInformacionVehiculo())

            return self.tmpInformacionVehiculo

        except Exception as inst:
            print(f'Error - tmpInformacionVehiculo_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA INFORMACIONVEHICULOTITULAR
    #     FOR SYSTEM NAME INFOR00002
    @property
    def informacionVehiculoTitular_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.informacionVehiculoTitular is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # Tabla de informacion de Vehiculo
                if self.informacionVehiculo is None:
                    self.informacionVehiculo = self.informacionVehiculo_Dal

                # realizamos la construccion de la tabla
                self.informacionVehiculoTitular = self.__buildTable(
                                self.formatosSucerp.tablaInformacionVehiculoTitular())

                # Tablas de referencias
                self.informacionVehiculoTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias,
                    self.informacionVehiculo
                ]

            return self.informacionVehiculoTitular

        except Exception as inst:
            print(f'Error - informacionVehiculoTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TMPINFORMACIONVEHICULOTITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def tmpInformacionVehiculoTitular_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tmpInformacionVehiculoTitular is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # Tabla de informacion de Vehiculo
                if self.tmpInformacionVehiculo is None:
                    self.tmpInformacionVehiculo = self.tmpInformacionVehiculo_Dal

                # realizamos la construccion de la tabla
                self.tmpInformacionVehiculoTitular = self.__buildTable(
                            self.formatosSucerp.tablaTmpInformacionVehiculoTitular())

            return self.tmpInformacionVehiculoTitular

        except Exception as inst:
            print(f'Error - tmpInformacionVehiculoTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA INFORMACIORADICACION
    #     FOR SYSTEM NAME INFOR00003
    @property
    def informacionRadicacion_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.informacionRadicacion is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Esatdos
                if self.estado is None:
                    self.estado = self.estado_Dal

                # realizamos la construccion de la tabla
                self.informacionRadicacion = self.__buildTable(
                            self.formatosSucerp.tablaInformacionRadicacion())

                # Tablas de referencias
                self.informacionRadicacion._referenced_by_list = [
                    self.tipoRegistro, self.estado
                ]

            return self.informacionRadicacion

        except Exception as inst:
            print(f'Error - informacionRadicacion_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TRAMITESGENERALES
    #     FOR SYSTEM NAME TRAMI00002
    @property
    def tramitesGenerales_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tramitesGenerales is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de SubRegistros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla tipo de Documentos
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla tramitesgeneralestitular
                if self.tramitesGeneralesTitular is None:
                    self.tramitesGeneralesTitular = self.tramitesGeneralesTitular_Dal


                # realizamos la construccion de la tabla
                self.tramitesGenerales = self.__buildTable(
                    self.formatosSucerp.tablaTramitesGenerales())

                # Tablas de referencias
                self.tramitesGenerales._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.tipoDocumento,
                    self.tramitesGeneralesTitular
                ]

            return self.tramitesGenerales

        except Exception as inst:
            print(f'Error - tramitesGenerales_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TRAMITESGENERALESTITULARES
    #     FOR SYSTEM NAME TRAMI00001
    @property
    def tramitesGeneralesTitular_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.tramitesGeneralesTitular is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de SubRegistros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Titular
                if self.tipoTitular is None:
                    self.tipoTitular = self.tipoTitular_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # realizamos la construccion de la tabla
                self.tramitesGeneralesTitular = self.__buildTable(
                    self.formatosSucerp.tablaTramitesGeneralesTitulares())

                # Tablas de referencias
                self.tramitesGeneralesTitular._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoTitular, self.tipoDocumento,
                    self.provincias
                ]

            return self.tramitesGeneralesTitular

        except Exception as inst:
            print(f'Error - tramitesGeneralesTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA PIE
    #     FOR SYSTEM NAME PIE
    @property
    def pie_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.pie is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # realizamos la construccion de la tabla
                self.pie = self.__buildTable(self.formatosSucerp.tablaPie())

                # Tablas de referencias
                self.pie._referenced_by_list = [
                    self.tipoRegistro
                ]

            return self.pie

        except Exception as inst:
            print(f'Error - pie_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA APIAUMOSO
    #     FOR SYSTEM NAME APIAUMOSO
    @property
    def apiAumoso_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.apiAumoso is None:

                # Tabla api Token
                if self.apiToken is None:
                    self.apiToken = self.apiToken_Dal

                # realizamos la construccion de la tabla
                self.apiAumoso = self.__buildTable(self.formatosSucerp.tablaApiAumoso())

                # Tablas de referencias
                self.apiToken._referenced_by_list = [ self.apiToken ]

            return self.apiAumoso

        except Exception as inst:
            print(f'Error - apiAumoso_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA GXPROD.MSGNIVELGRAVEDAD
    #     FOR SYSTEM NAME MSGNI00001------------------------
    @property
    def msgNivelGravedad_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__msgNivelGravedad is None:

                # realizamos la construccion de la tabla
                self.__msgNivelGravedad = self.__buildTable(
                                    self.formatosSucerp.tablaMensajeNivelGravedad())

            return self.__msgNivelGravedad

        except Exception as inst:
            print(f'Error - msgNivelGravedad_Dal {e}')
            print(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA GXPROD.MENSAJESERROR
    #     FOR SYSTEM NAME MENSA00001------------------------
    @property
    def mensajeError_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__mensajesError is None:
    
                # realizamos la construccion de la tabla
                self.__mensajesError = self.__buildTable(self.formatosSucerp.tablaMensajeError())

            return self.__mensajesError
        
        except Exception as inst:
            print(f'Error - mensajeError_Dal {e}')
            print(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA GXPROD.MENSAJESERRORMSGDINAMICOS
    #     FOR SYSTEM NAME MENSA00002------------------------
    @property
    def mensajesErrorMsgdDinamicos_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__mensajesErrorMsgdDinamicos is None:

                    # realizamos la construccion de la tabla
                    self.__mensajesErrorMsgdDinamicos = self.__buildTable(
                                self.formatosSucerp.tablaMensajesErrorMsgdDinamicos())

            return self.__mensajesErrorMsgdDinamicos
        
        except Exception as inst:
            print(f'Error - mensajesErrorMsgdDinamicos_Dal {e}')
            print(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA GXPROD.IMPRESIONPDF
    #     FOR SYSTEM NAME IMPRE00001------------------------
    @property
    def impresionPdf_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__impresionPdf is None:

                # realizamos la construccion de la tabla
                self.__mensajesErrorMsgdDinamicos = self.__buildTable(
                                    self.formatosSucerp.tablaImpresionPdf())
                                           
            return self.__impresionPdf
        
        except Exception as inst:
            print(f'Error - impresionPdf_Dal {e}')
            print(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA RECEPLOG
    #     FOR SYSTEM NAME IMPRE00001------------------------
    @property
    def recepLog_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__recepLog is None:

                # realizamos la construccion de la tabla
                self.__recepLog = self.__buildTable(
                                    self.formatosSucerp.tablaRecepLog())
                                           
            return self.__recepLog
        
        except Exception as inst:
            print(f'Error - recepLog_Dal {e}')
            print(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA RECEPCIONTEXTO
    #     FOR SYSTEM NAME IMPRE00001------------------------
    @property
    def recepcionTexto_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__recepcionTexto is None:

                # realizamos la construccion de la tabla
                self.__recepcionTexto = self.__buildTable(
                                    self.formatosSucerp.tablaRecepcionTexto())
                                           
            return self.__recepcionTexto
        
        except Exception as inst:
            print(f'Error - recepcionTexto_Dal {e}')
            print(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA RECEPCIONARCHIVOS
    #     FOR SYSTEM NAME IMPRE00001------------------------
    @property
    def recepcionArchivos_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__recepcionArchivos is None:

                # realizamos la construccion de la tabla
                self.__recepcionArchivos = self.__buildTable(
                                    self.formatosSucerp.tablaRecepcionArchivos())
                                           
            return self.__recepcionArchivos
        
        except Exception as inst:
            print(f'Error - recepcionArchivos_Dal {e}')
            print(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def __buildTable(self, parm):

        try:

            # create  table
            valor = self.db.define_table(parm['name'], *parm['fields'], **parm['arg'])

            # if the environment allows to generate LABEL ON
            if parm['arg']['migrate']:

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
                    self.db.executesql(sentencia)

            self.db.commit()
            return valor

        except Exception as inst:
            print(inst)
            return inst

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ----CLASE DE DEFINICION DE TABLAS DE LA BIBLIOTECA MATANZA
class MatanzaAbstractDb():
    """
     EL OBJETIVO DE ESTA CLASE ES PODER DESCRIBIR LOS CAMPOS DE CADA TABLA QUE ESTAMN EL MOTOR ISERIES O MYSQL \n
     CUANDO TRABAJAMOS SIN CONEXION A LAS TABLAS DE ISERIES SE TRABAJA CON MYSQL \n

    """

    # Constructor
    def __init__(self, db):

        # Conexion
        self.db = db

        # ------------------------------------------------------
        # Tablas de Matanza
        self.__tmAut = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA MATANZA.TMAUT
    #     FOR SYSTEM NAME TMAUT
    @property
    def tmAut_Dal(self):

        try:

            # valida si la tabla ha sido inicializado
            if self.__tmAut is None:

                # realizamos la construccion de la tabla
                self.__tmAut = self.__buildTable(
                                    self.formatosSucerp.tablaMaut())
                                           
            return self.__tmAut
        
        except Exception as inst:
            print(f'Error - tmAut_Dal {e}')
            print(inst)


