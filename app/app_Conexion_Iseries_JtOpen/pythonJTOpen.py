# -------Lista de lisbrerias y Modulos
try:
    import jpype
    import os
    import platform
    from app_Config.config import ConfigurarAplicacion    
    from com_ibm_as400_accees.as400 import AS400
    from com_ibm_as400_accees.as400Ftp import AS400FTP

except Exception as e:
    print(f'Falta algun modulo {e}')

# Definimos la clase para manejar la iseries
class JT400Helper(object):

    """
    CALL  PGM(QCMD) para poder acceder sin restricciones de permisos
    """


    def __init__(self, server, username, pwd):

        """
        server    = Es la Ip del server
        username  = Es el usuario
        pwd       = Es la password  del usuario
        """

        self.registros = list()

        # asignamos los parametros recibidos
        self.server, self.username, self.pwd = server, username, pwd


        # determinamos en que plataforma estamos ejeutando el script
        if platform.system() == 'Linux':

            # definimos el path la java virtual machine
            jvmpath = ConfigurarAplicacion.JVMPATH_LINUX
            # definimos el path del jt400
            jarpath = ConfigurarAplicacion.JARPATH_LINUX

        # para el caso de que sea la plataforma windows
        else:

            # definimos el path la java virtual machine
            jvmpath = ConfigurarAplicacion.JVMPATH_WINDOWS
            # definimos el path del jt400
            jarpath = ConfigurarAplicacion.JARPATH_WINDOWS


        # definimos donde se encuentra jt400
        jvmArg = f'-Djava.class.path={jarpath}'

        try:

            jpype.startJVM(jvmpath, jvmArg)

        except Exception as e:
            print(f"Error al iniciar la JVM: {e}")


        # definimos el objeto CommandCall
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/CommandCall.html
        CommandCall = jpype.JClass('com.ibm.as400.access.CommandCall')

        # definimos el objeto el ProgramCall
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/ProgramCall.html
        ProgramCall = jpype.JClass('com.ibm.as400.access.ProgramCall')

        # definimos el objeto para obtener el listado de spool
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/SpooledFileList.html
        SpooledFileList = jpype.JClass('com.ibm.as400.access.SpooledFileList')

        # definimos el objeto AS400Text
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Text.html
        AS400Text = jpype.JClass('com.ibm.as400.access.AS400Text')

        # definimos el objeto AS400JDBCDriver
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400JDBCDriver.html
        AS400JDBCDriver = jpype.JClass('com.ibm.as400.access.AS400JDBCDriver')

        # definimos el objeto Conection
        Connection = jpype.JClass('java.sql.Connection')

        self.Enumerate = jpype.JClass('java.util.Enumeration')

        # definimos el objeto DatabaseMetaData
        DatabaseMetaData = jpype.JClass('java.sql.DatabaseMetaData')

        # definimos el objeto Statement
        Statement = jpype.JClass('java.sql.Statement')

        # definimos el objeto ResultSet
        self.ResultSet = jpype.JClass('java.sql.ResultSet')

        # definimos el objeto que maneja el RJobLog
        self.RJobLog = jpype.JClass('com.ibm.as400.resource.RJobLog')

        # definimos el pbjeto AS400
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400.html
        AS400 = jpype.JClass('com.ibm.as400.access.AS400')

        # definimos el objeto AS400FTP
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400FTP.html
        self.AS400FTP = jpype.JClass('com.ibm.as400.access.AS400FTP')

        # definimos el objeto IFSFile
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/IFSFile.html
        self.IFSFile = jpype.JClass('com.ibm.as400.access.IFSFile')

        # definimos objetolist
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/ObjectList.html
        self.objetoList = jpype.JClass('com.ibm.as400.access.ObjectList')

        # definimos el objeto ProgramParameter
        self.ProgramParameter = jpype.JClass('com.ibm.as400.access.ProgramParameter')

        # definimos el objeto DriverManager
        self.DriverManager = jpype.JClass('java.sql.DriverManager')

        # asignamos el driver jodbc al DriveManager
        self.DriverManager.registerDriver(AS400JDBCDriver())

        # asignamos al sistema con el valor el server usuario y password
        self.system = AS400(self.server, self.username, self.pwd)

        # asignamos una instancia del AS400FTP
        self.FTP = jpype.JClass('com.ibm.as400.access.FTP') 
        self.ftp = self.AS400FTP(self.system)

        # definimos una instancia de CommandCall
        self.cc = CommandCall(self.system)

        # definimos una instancia de outqueue
        self.outqueue = SpooledFileList(self.system)

        # definimos una instancia de pc
        self.pc = ProgramCall(self.system)

        # Represents information about a CL command (*CMD) object on the system.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/index.html?overview-tree.html
        self.Command = jpype.JClass('com.ibm.as400.access.Command')


        self.String = jpype.JClass('java.lang.String')


        # La clase AS400Array proporciona un tipo de datos compuesto 
        # que representa una matriz de objetos AS400DataType.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Array.html
        self.AS400Array = jpype.JClass('com.ibm.as400.access.AS400Array')

        # La clase AS400ArrayBeanInfo proporciona información de frijol para la clase AS400Array.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400ArrayBeanInfo.html
        self.AS400ArrayBeanInfo = jpype.JClass('com.ibm.as400.access.AS400ArrayBeanInfo')

        # La clase AS400BeanInfo proporciona información de frijol para la clase AS400.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400BeanInfo.html
        self.AS400BeanInfo = jpype.JClass('com.ibm.as400.access.AS400BeanInfo')
        
        # La clase AS400BidiTransform proporciona transformaciones de diseño que permiten la conversión de texto Bidi 
        # en formato IBM i (después de su conversión a Unicode) a texto Bidi en formato Java, o viceversa.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400BidiTransform.html
        self.AS400BidiTransform = jpype.JClass('com.ibm.as400.access.AS400BidiTransform')

        # La clase AS400Bin2 proporciona un convertidor entre un objeto corto y un número binario firmado de dos bytes.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Bin2.html
        self.AS400Bin2 = jpype.JClass('com.ibm.as400.access.AS400Bin2')

        # La clase AS400Bin4 proporciona un convertidor entre un objeto entero y un número binario firmado de cuatro bytes.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Bin4.html
        self.AS400Bin4 = jpype.JClass('com.ibm.as400.access.AS400Bin4')

        # La clase AS400Bin8 proporciona un convertidor entre un objeto largo y un número binario firmado de ocho bytes.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Bin8.html
        self.AS400Bin8 = jpype.JClass('com.ibm.as400.access.AS400Bin8')

        # La clase AS400ByteArray proporciona un convertidor entre una matriz de bytes y una matriz de bytes de longitud 
        # fija que representa datos de IBM i que no son convertibles.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400ByteArray.html
        self.AS400ByteArray = jpype.JClass('com.ibm.as400.access.AS400ByteArray')

        # La clase AS400Certificate representa un certificado codificado X.509 ASN.1.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Certificate.html
        self.AS400Certificado = jpype.JClass('com.ibm.as400.access.AS400Certificate')

        # La clase AS400CertificateAttribute representa un certificado atributo. Este atributo se utiliza para identificar certificados durante una operación de lista. 
        # Esta clase contiene un solo atributo que puede ser un valor de matriz de cadenas o de bytes.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateAttribute.html
        self.AS400CertificadoAtributo = jpype.JClass('com.ibm.as400.access.AS400CertificateAttribute')

        # La clase AS400CertificateEvent representa un evento AS400Certificate.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateEvent.html
        self.AS400CertificadoEvento = jpype.JClass('com.ibm.as400.access.AS400CertificateEvent')

        # La clase AS400CertificateUserProfileUtil accede a certificados en un objeto de perfil de usuario de IBM i.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateUserProfileUtil.html
        self.AS400CertificadoUserProfileUtil = jpype.JClass('com.ibm.as400.access.AS400CertificateUserProfileUtil')

        # La clase AS400CertificateUserProfileUtilBeanInfo proporciona información 
        # de frijoles para la clase AS400CertificateUserProfileUtil.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateUserProfileUtilBeanInfo.html
        self.AS400CertificadoUserProfileUtilBeanInfo = jpype.JClass('com.ibm.as400.access.AS400CertificateUserProfileUtilBeanInfo')
 
        # La clase AS400CertificateUtil proporciona los métodos comunes a AS400CertificateVldlUtil y AS400CertificateUserProfileUtil. 
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateUtil.html
        self.AS400CertificadoUtil = jpype.JClass('com.ibm.as400.access.AS400CertificateUtil')

        # La clase AS400CertificateUtilBeanInfo proporciona información de frijoles para la clase AS400CertificateUtil.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateUtilBeanInfo.html
        self.AS400CertificadoUtilBeanInfo = jpype.JClass('com.ibm.as400.access.AS400CertificateUtilBeanInfo')

        # La clase AS400CertificateVldlUtil proporciona la implementación de los métodos para acceder a 
        # certificados en un objeto de lista de validación IBM i.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateVldlUtil.html
        self.AS400CertificadoVldlUtil = jpype.JClass('com.ibm.as400.access.AS400CertificateVldlUtil')

        # La clase AS400CertificateVldlUtilBeanInfo proporciona información de frijoles para la clase AS400CertificateVldlUtil.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400CertificateVldlUtilBeanInfo.html
        self.AS400CertificadoVldlUtilBeanInfo = jpype.JClass('com.ibm.as400.access.AS400CertificateVldlUtilBeanInfo')

        # La clase AS400ConnectionPool gestiona un grupo de objetos AS400. Se utiliza un grupo de conexiones para comparta conexiones 
        # y administre el número de conexiones que un usuario puede tener con el sistema.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400ConnectionPool.html
        self.AS400ConnectionPool = jpype.JClass('com.ibm.as400.access.AS400ConnectionPool')

        # La clase AS400ConnectionPoolBeanInfo proporciona la información del frijol para la clase AS400ConnectionPool.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400ConnectionPoolBeanInfo.html
        self.AS400ConexiónPoolBeanInfo = jpype.JClass('com.ibm.as400.access.AS400ConnectionPoolBeanInfo')

        # La clase AS400DateTimeConverter representa una fecha y hora convertidas. 
        # El AS/400 System API QWCCVTDT se utiliza para convertir un valor de fecha y hora de un formato a otro formato.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400DateTimeConverter.html
        self.AS400DateTimeConverter = jpype.JClass('com.ibm.as400.access.AS400DateTimeConverter')

        # La clase AS400DecFloat proporciona un convertidor entre un objeto BigDecimal y un tipo DecimalFloat.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400DecFloat.html
        self.AS400DecFloat = jpype.JClass('com.ibm.as400.access.AS400DecFloat')

        # La clase AS400File representa un archivo físico o lógico en el sistema. Permite al usuario hacer lo siguiente:
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400File.html
        self.AS400File = jpype.JClass('com.ibm.as400.access.AS400File')

        # La clase AS400FileBeanInfo proporciona frijol información para la clase AS400File.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400FileBeanInfo.html
        self.AS400FileBeanInfo = jpype.JClass('com.ibm.as400.access.AS400FileBeanInfo')

        # La clase AS400FileRecordDescription representa las descripciones de registro de un físico o archivo lógico en el sistema. 
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400FileRecordDescription.html
        self.AS400FileRecordDescripción = jpype.JClass('com.ibm.as400.access.AS400FileRecordDescription')

        # La clase AS400FileRecordDescriptionBeanInfo proporciona información de frijoles para la clase AS400FileRecordDescription.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400FileRecordDescriptionBeanInfo.html
        self.AS400FileRecordDescripciónBeanInfo = jpype.JClass('com.ibm.as400.access.AS400FileRecordDescriptionBeanInfo')

        # La clase AS400FileRecordDescriptionEvent representa un RecordDescriptionEvent. 
        # Esta clase está acostumbrada a eventos de incendio de las clases de descripción de registros, RecordFormat y Grabar.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400FileRecordDescriptionEvent.html
        self.AS400FileRecordDescripciónEvento = jpype.JClass('com.ibm.as400.access.AS400FileRecordDescriptionEvent')

        # La clase AS400Float4 proporciona un convertidor entre un objeto Float y un número de punto flotante de cuatro bytes.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Float4.html
        self.AS400Float4 = jpype.JClass('com.ibm.as400.access.AS400Float4')

        # La clase AS400Float8 proporciona un convertidor entre un objeto doble y un número de punto flotante de ocho bytes.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400Float8.html
        self.AS400Float8 = jpype.JClass('com.ibm.as400.access.AS400Float8')

        # La clase AS400FTPBeanInfo proporciona información sobre frijoles para la clase FTP.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400FTPBeanInfo.html
        self.AS400FTPBeanInfo = jpype.JClass('com.ibm.as400.access.AS400FTPBeanInfo')

        # AS400JDBCArray es una implementación de java.sql.Array y contiene una matriz de datos JDBC.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400JDBCArray.html
        self.AS400JDBCArray = jpype.JClass('com.ibm.as400.access.AS400JDBCArray')

        # AS400JDBCArrayResultSet es un JDBC ResultSet que contiene datos de Array
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400JDBCArrayResultSet.html
        self.AS400JDBCArrayResultSet = jpype.JClass('com.ibm.as400.access.AS400JDBCArrayResultSet')

        # La clase AS400JDBCBlob proporciona acceso a grandes binarios objetos. Los datos son válidos solo dentro de la corriente transacción.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400JDBCBlob.html
        self.AS400JDBCBlob = jpype.JClass('com.ibm.as400.access.AS400JDBCBlob')

        # La clase AS400JDBCBlobLocator proporciona acceso a grandes binarios objetos. Los datos son válidos solo dentro de la corriente transacción.
        # https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/AS400JDBCBlobLocator.html
        self.AS400JDBCBlobLocator = jpype.JClass('com.ibm.as400.access.AS400JDBCBlobLocator')
 




    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Este metodo muestra una lista de Objetos
    def getObjectsList(self, objectLibrary, objectName, objectType):

        """
        Se obtiene una lista de objetos

        objectLibrary - Es la biblioteca que deseamos recuperar la lista
            ALL - Todas las bibliotecas
            ALL_USER - de Todos los usuario
            CURRENT_LIBRARY - La current_library
            LIBRARY_LIST - La lista de bibliotecas del sistema
            USER_LIBRARY_LIST - La lista de bibliotecas del usuario

        objectName - El nombre del objeto.
            ALL - Todos los ejemplos
            ALL_USER - Todos los objetos de la biblioteca QSYS.
            IBM - tODOS LOS OBJETOS

        objectType - Tipos de objetos. Ejemplo (*LIB, *FILE, *OUTQ, etc) or ALL.

        """
        

        return self.objetoList(self.system, objectLibrary, objectName, objectType)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Este metodo muestra el valor ifspath
    def ShowIfs(self, ifspath):

        # asigno una instancia del IFSFile de un sistema y el ifspath
        ifs = self.IFSFile(self.system,ifspath)
        # visauliza que es el ifspath
        print(f'Verifica si exists : {ifs.exists()}')
        print(f'Verifica si es un Directory : {ifs.isDirectory()}')
        print(f'Verifica si es un File : {ifs.isFile()}')

        # busca la lista de los archivos
        fs = ifs.listFiles()

        # si hay elementos
        if len(fs) > 0:
            for f in fs:
                print(f.name)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # visualizamos la fecha del ultimo cambio de un objeto de tipo FILE
    def ShowObj2(self, lib, obj):

        # definimos la instancia de la clase ObjectDescription
        od = self.ObjectDescription(self.system, lib, obj, "FILE")

        # visualiza la fecha del cambio
        print(od.CHANGE_DATE_AND_TIME)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ejecutamos la sentencia del sql
    def GetSQLResult(self, cmdstr, ofile=''):
        """
        cmdstr = Es la sentencia SQL
        ofile  = Es el archivo de salida que es opcional
        """
        self.registros = list()

        # asignamos la conexion
        connection = self.DriverManager.getConnection("jdbc:as400://" + self.server, self.username, self.pwd)

        # obtenemos la metada de la base de datos
        dmd = connection.getMetaData()

        # creamos la conexion al motor pasandole como parametros
        # self.ResultSet.TYPE_SCROLL_SENSITIVE = es sensitivo al scroll
        # self.ResultSet.CONCUR_UPDATABLE = con cursor habilitado para actualizar
        select = connection.createStatement(self.ResultSet.TYPE_SCROLL_SENSITIVE, self.ResultSet.CONCUR_UPDATABLE)

        # Ejecutamos la sentencia sql y esperamos el cursor
        rs = select.executeQuery(cmdstr)

        # inicializamos
        strs = ''

        # averiguamos la cantidad de columnas tiene el cursor
        cols = rs.getMetaData().getColumnCount()

        # mientras haya registros se realiza el loop
        while (rs.next()):

            # inicializamos una lista
            rowstrs = []

            # recorremos la cantidad de columnas obtenidas del cursor
            for i in range(1, cols+1):
                value = rs.getString(i)
                if ' ' in value:
                    value = f'{value}'

                # agregamos elementos a la lista
                rowstrs.append(rs.getString(i))

            # genero el resulta del cursor delimitado por comas
            #strs += ','.join(rowstrs)+'\n'


            # si hay algun nombre de archivo de salida grabamos
            if ofile != '':

                with open(ofile,'w') as f:
                    f.write(strs)
            else:

                self.registros.append(rowstrs)

        # cierro la conexion
        connection.close()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos el mensaje de respuesta al ejecutar el comando
    def GetCmdMsg(self, cmdstr):
        """
        cmdstr = Es el comando a ejecutar
        """
        msg = list()

        # ejecutamos el comando
        successfully = self.cc.run(cmdstr)

        # si el mensaje de respuesta es erroneo
        if successfully:
            msg.append(True)
        else:

            msg.append(False)
            # obtenemos la lista de mensajes de la cola de mensajes
            ml = self.cc.getMessageList()

            # navegamos por la lista de los mensajes
            for m in ml:
                msg.append(m.getText())

        return msg

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # visualizamos la descripcion del objeto
    def ShowObj(self, lib, obj, tmplib):
        """
        lib    = Es la biblioteca donde esta el objeto
        obj    = Es el nombre del objeto
        tmplib = Es la bibloteca donde colocamos el resultado del comando
        """
        # construimos el comando
        cmdstr = f'DSPOBJD OBJ({lib}/{obj}) OBJTYPE(*PGM) OUTPUT(*OUTFILE) OUTFILE({tmplib}/OBJD)'

        # ejecuta el comando y espera un mensaje de respuesta
        msg = self.GetCmdMsg(cmdstr)

        # si no hay error
        if msg[0]:
            cmdstr = 'SELECT ODLBNM, ODOBNM, ODOBTP, ODOBAT,ODOBSZ , ODOBTX, ODLDAT, ODLTIM,'
            cmdstr += ' ODOBSY, ODCRTU, ODJRST, ODJRNM, ODJRLB, ODJRIM, ODJREN, ODJRCN,'
            cmdstr += f' ODJRDT, ODJRTI FROM {tmplib}'

            # obtenemos el resultado de la sentencia sql
            self.GetSQLResult(cmdstr)


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # visualizamos los campos de una base de datos
    def SaveFieldDef(self, flib, file, tmplib, ofile):
        """
        flib   = Es la biblioteca de la base de datos
        file   = Es el nombre de la base de datos
        tmplib = Es la bibloteca donde colocamos el resultado del comando
        ofile  = Es el archivo de salida que es opcional
        """
        # construimos el comando
        cmdstr = f'DSPFFD FILE({flib}/{file}) OUTPUT(*OUTFILE) OUTFILE({tmplib}/FIELDDEF)'

        # ejecuta el comando y espera un mensaje de respuesta
        msg = self.GetCmdMsg(cmdstr)

        # si no hay error
        if msg[0]:
            cmdstr = 'SELECT WHFLDI, WHFTXT, WHFLDT, WHFLDD, WHFLDP,WHFLDB, WHFOBO'
            cmdstr += f' FROM {tmplib}.FIELDDEF WHERE WHFLDI <> ' ' ORDER BY WHFOBO'

            # obtenemos el resultado de la sentencia sql
            self.GetSQLResult(cmdstr,ofile)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos un job log por numero
    def GetJobLogByNum(self, jobnum, jobuser, jobname):
        """
        jobnum  = Es el numero del Job
        jobuser = Es el nombre del usuario del Job
        jobname = Es el nombre del Job
        """

        # genera una instancia del objeto que maneja el retorno de los datos de un Job
        joblog = self.RJobLog(self.system,jobname,jobuser,jobnum)

        # realiza la apertura de un Job
        joblog.open()

        # Espera hasta que el Job finalice
        joblog.waitForComplete()

        # obtenemos la longitud de la lista del joblog
        num = joblog.getListLength()

        # recuperamos el contenido del joblog
        msgs = []
        for i in range(0,num):
            qmsg = joblog.resourceAt(i)
            msgs.append(qmsg.getAttributeValue("MESSAGE_TEXT"))
            msg = '\n'.join(msgs)
            return msg


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos la informacion de un joblog pasandole los datos del job
    def GetJobLog(self, jobstr):
        """
        jobstr  = Es la identificacion del job
        """

        # sacamos las / del string con la identificacion del job
        jobarr = jobstr.split('/')

        # asignamos los parametros para llamar GetJobLogByNum
        jobnum, jobuser, jobname = jobarr[0], jobarr[1], jobarr[2]

        # obtenemos un job log por numero
        return self.GetJobLogByNum( jobnum, jobuser, jobname)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # grabamos los datos del joblog en un archivo
    def SaveJobLog(self, jobstr, ofile):
        """
        jobstr  = Es la identificacion del job
        ofile   = Es el archivo de salida es opcional
        """

        msg = self.GetJobLog(jobstr)
        with open(ofile,'w') as f:
            f.write(msg)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # llamamos a un programa de la iseries
    def CallProgram(self, plib, pgm, paras):
        """
        plib  = Es la biblioteca donde esta el programa
        pgm   = Es el nombre del programa
        paras = Es la lista de parametros del programa

        retorna una lista con el resultado del comando
        """

        #WRKACTJOB SBS(QUSRWRK) JOB(QZRCSRVS) - dump not work
        #paras=["Y","12345"," "]
        pgmparas=[]
        # navegamos por la lista de parametros
        for para in paras:
            pgmparas.append(self.ProgramParameter(para))
            print(str(pgmparas.getInputData()))

        # cargamos los datos del programa a ejecutar
        self.pc.setProgram(f'/QSYS.LIB/{plib}.LIB/{pgm}.PGM',pgmparas)

        # ejecutamos el programa y esperamos su respuesta
        successfully = self.pc.run()

        msg = list()

        # obtenemos los datos del Job del programa
        job = self.pc.getJob()
        print(self.pc.toString())
        print(job.toString())

        # si no fue exitosa la ejecucion del programa
        if successfully != True:

            msg.append(False)

            # obtenemos la cola de mensaje
            ml = self.pc.getMessageList()

            # navegamos por la lista de los mensajes
            for m in ml:
                msg.appen(m.getText())

            # desconectamos los servicios
            self.system.disconnectAllServices()
        else:
            msg.append(True)
        return msg

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # verificamos si el objeto FILE existe
    def CheckObjExists(self, lib, file, type="*FILE"):
        """
        lib   = Es la biblioteca donde esta el objeto
        file  = Es el nombre del objeto
        type  = Es el tipo del objeto

        retornamos una lista con el resultado del comando
        """
        str = f'CHKOBJ OBJ({lib}/{file}) OBJTYPE({type})'
        return self.GetCmdMsg(str)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # eliminamos el objeto
    def DeleteObj(self, lib, file):
        """
        lib   = Es la biblioteca donde esta el objeto
        file  = Es el nombre del objeto

        retornamos una lista con el resultado del comando
        """
        str = f'DLTF FILE({lib}/{file})'
        return self.GetCmdMsg(str)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # copiamos desde una objeto tipo file al IFS
    def FileToIfs(self, lib, file, mem, ifspath):

        """
        lib     = Es la biblioteca donde esta el objeto
        file    = Es el nombre del objeto
        mem     = Es el nombre del miembro del file
        ifspath = Es el archivo IFS

        retorna una lista con el resultado del comando

        don't use RMVBLANK(*TRAILING) ,will cause numeric field contains
        blank characters error when put ifs to file

        """

        str = f'CPYTOIMPF FROMFILE({lib}/{file} {mem}) TOSTMF({ifspath}) MBROPT(*REPLACE) STMFCCSID(*STMF)'
        str += f'RCDDLM(*CRLF) DTAFMT(*DLM) STRDLM(*NONE)'
        print(lib, file, mem, "->", ifspath)
        return self.GetCmdMsg(str)


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # copiamos un objeto desde IFS a un objeto FILE
    def IfsToFile(self, ifspath, lib, file, mem):
        """
        lib     = Es la biblioteca donde esta el objeto
        file    = Es el nombre del objeto
        mem     = Es el nombre del miembro del file
        ifspath = Es el archivo IFS

        retorna una lista con el resultado del comando

        """
        str = f'CPYFRMIMPF FROMSTMF({ifspath}) TOFILE({lib}/{file} {mem}) MBROPT(*REPLACE) RCDDLM(*CRLF)'
        str += f' STRDLM(*NONE) FLDDLM(',') ERRRCDOPT(*REPLACE) RPLNULLVAL(*FLDDFT)'
        print(ifspath,"->",lib,file,mem)

        # retornamos la respuesta de la ejecucion del comando en la iserie
        return self.GetCmdMsg(str)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos un objeto desde el IFS a un archivo de la PC
    def FtpGetIfsFile(self, ifspath, ofile):
        """
        ofile   = Es el archivo de la PC
        ifspath = Es el archivo IFS

        retornamos el resultado del FTP
        """
        ftp = self.AS400FTP(self.system)
        successfully = ftp.get(ifspath,ofile)
        print(ifspath,"->",ofile)
        return successfully


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos un objeto de tipo FILE desde la IFS
    def FtpGetIfsFile(self,ifspath,ofile):
        """
        ifspath = Es el archivo IFS
        ofile   = Es el archivo de la PC

        retornamos el resultado del FTP
        """

        ftp=self.AS400FTP(self.system)
        successfully = ftp.get(ifspath,ofile)
        print(ifspath,"->",ofile)
        return successfully


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos un objeto de tipo FILE a un archivo de la PC
    def FileToPc(self,  lib, file, mem, ofile):
        """
        lib     = Es la biblioteca donde esta el objeto
        file    = Es el nombre del objeto
        mem     = Es el nombre del miembro del file
        ifspath = Es el archivo IFS
        ofile   = Es el archivo de la PC
        """

        # definimos un archivo de recepcion en la temp
        tmpifs = f'QDLS/TEMP/{mem}.CSV'

        # copiamos el objeto tipo FILE al archivo de recepcion
        msg = self.FileToIfs(lib,file,mem,tmpifs)

        # verificamos el resultado de la copia
        if msg[0]:

            # obtenemos desde el archivo de recepcion y lo copiamos a la PC
            respuesta =  self.FtpGetIfsFile(tmpifs,ofile)
        else:
            msg

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # transferimos un archivo desde la PC hacia la IFS
    def FtpPutIfsFile(self, ifile, ifspath):
        """
        ifile    = Es el nombre del archivo PC
        ifspath  = Es el archivo IFS

        retornamos el resultado del FTP
        """
        try:

            # ejecutamos en PUT del FTP
            successfully = self.ftp.connect()
            self.ftp.setDataTransferType(self.ftp.ASCII)
            successfully = self.ftp.put(ifile, ifspath)

            print(ifile,"->",ifspath)

            return successfully
        
        except Exception as e:
            print(f'Error Ftp {e}')


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # transferimos un archivo desde la PC hacia un objto tipo FILE
    def PcToFile(self, ifile, lib, file, mem):
        """
        lib     = Es la biblioteca donde esta el objeto
        file    = Es el nombre del objeto
        mem     = Es el nombre del miembro del file
        ifile   = Es el nombre del archivo PC
        """

        tmpifs = f'QDLS/TEMP/{mem}.CSV'

        # transferimos el archivo PC al IFS
        self.FtpPutIfsFile(ifile, tmpifs)

        # copiamos del IFS al objto tipo FILE
        self.IfsToFile(tmpifs,lib,file,mem)


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # transferimos desde un archivo fuente a la PC
    def FtpGetText(self, lib, srcf, mem, dest=r"d:\temp"):
        """
        lib     = Es la biblioteca donde esta el objeto
        srcf    = Es el nombre del objeto SRC
        mem     = Es el nombre del miembro del file SRC
        dest    = Es el directorio destino para generar el archivo de texto de la PC

        retornamos el resultado del FTP
        """
        msg = list()
        # generamos una instancia del FTP del sistema
        ftp = self.AS400FTP(self.system)

        # es el archivo fuente desde donde se toma los datos
        target = f'/QSYS.LIB/{lib}.LIB/{srcf}.FILE/{mem}.MBR'

        # verificamos si es un directorio
        if os.path.isdir(dest):

            # armamos el nombre del archivo PC
            dest = os.path.join(dest, mem+".txt")
            print(target,"->",dest)

            # ejecutamos el comando FTP
            successfully = ftp.get(target, dest)
            return successfully


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # transferimos desde un archivo de salvar  a la PC
    def FtpGetSavf(self, lib, savf, dest=r"d:\temp"):
        """
        lib     = Es la biblioteca donde esta el objeto
        savf    = Es el nombre del objeto SAV
        dest    = Es el directorio destino para generar el archivo de texto de la PC

        QUOTE SITE NAMEFMT 0 QGPL/QCLSRC.TEST
        QUOTE SITE NAMEFMT 1 /QSYS.lib/Libname.lib/Fname.file/Mname.mbr

        retornamos el resultado del FTP
        """

        # generamos una instancia del FTP del sistema
        ftp = self.AS400FTP(self.system)

        # es el archivo fuente desde donde se toma los datos
        target = f'/QSYS.LIB/{lib}.LIB/{savf}.SAVF'

        # le decimos al ftp qu e usamos la nomenclatura de tipo 1
        ftp.issueCommand("quote site namefmt 1")

        # verificamos si es un directorio
        if os.path.isdir(dest):

            # armamos el nombre del archivo PC
            dest=os.path.join(dest,savf+".SAVF")

            # asignamos al ftp el tipo de transferencia
            ftp.setDataTransferType(1)

            # ejecutamos el comando FTP
            successfully = ftp.get(target, dest)
            return successfully

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # transferimos de un archivo PC a un miembro SRC de la Iseries
    def FtpPutText(self, ifile, lib, srcf, mem):
        """
        ifile   = Es el nombre del archivo PC
        lib     = Es la biblioteca donde esta el objeto
        srcf    = Es el nombre del objeto SRC
        mem     = Es el nombre del miembro del file SRC

        retornamos el resultado del FTP

        """

        # generamos una instancia del FTP del sistema
        ftp = self.AS400FTP(self.system)

        # definimos el destino del archivo ifile
        dest = f'/QSYS.LIB/{lib}.LIB/{srcf}.FILE/{mem}.MBR'

        # ejecutamos el comando FTP
        successfully = ftp.put(ifile, dest)

        print(ifile,"->",lib,srcf,mem)
        return successfully


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos una lista de los objetos de uan cola de salida
    def GetOutQList(self, outqlib, outq):
        """
        outqlib = Es el nombre de la biblioteca de la cola de salida
        outq    = Es el nombre de la cola de salida

        """

        # definimos cual es la cola de salida
        self.outqueue.setQueueFilter(f'/QSYS.LIB/{outqlib}.LIB/{outq}.OUTQ')

        # definimos el filtro del usario de la cola de salida
        self.outqueue.setUserFilter("*ALL")

        # sincronizamos
        self.outqueue.openSynchronously()

        # obtenemos los objetos de la cola de salida
        enums = self.outqueue.getObjects()

        i = 1
        info = ""

        # se ejecuta mientras haya elementos
        while (enums.hasMoreElements()):

            # obtenemos los datos del elemento de la cola de salida
            splf = enums.nextElement()

            # si hay informacion
            if(splf != None):

                strs=[]
                splSystem = splf.getStringAttribute(271)
                splfFile = splf.getStringAttribute(104)
                splFilNum = splf.getIntegerAttribute(105).toString()
                splProgram = splf.getStringAttribute(272)
                splDate = splf.getStringAttribute(34)
                jobNumber = splf.getStringAttribute(60)
                jobUser = splf.getStringAttribute(62)
                jobNam = splf.getStringAttribute(59)
                FilePages = splf.getIntegerAttribute(111).toString()
                PrintQ = splf.getStringAttribute(48)
                PrintDevice = splf.getStringAttribute(90)
                PageSize = splf.getFloatAttribute(78).intValue()

                strs.append(f'System :{splSystem}, File : {splfFile}, File Number : {splFilNum}, Progarm :{splProgram}, Date : {splDate}')
                strs.append(f'Number/User/Job : {jobNumber}/{jobUser}/{jobNam}')
                strs.append(f'File Pages: {FilePages}, Print quality : {PrintQ}, Printer device type : {PrintDevice}, Page size length : {PageSize}')

                info += '\n'.join(strs)+'\n'

                i+=1
        # desconexion de todos loa servicios
        self.system.disconnectAllServices()
        print('total spool files : ', i)
        print(info)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # obtenemos un archivo de spool
    def GetSpoolFile(self, sflib, sffile, sfname, sfjobnum, fnum, dest):
        """
        sflib    = Es el nombre de la biblioteca del spool
        sffile   = Es el nombre de el archivo del spool
        sfname   = Es el nombre del el spool
        sfjobnum = Es el numeo de Job
        fnum     = Es el numero
        dest     = Es la ubicacion de destino a grabar el spool
        """

        # verificacmos si el objeto existe
        msg = self.CheckObjExists(sflib, sffile)

        # verificamos si el comando fue exitoso
        if msg[0]:

            #IGCDTA parameter is for DBCS file
            # ejecutamos el comando
            msg = self.GetCmdMsg(f'CRTPF FILE({sflib}/{sffile}) RCDLEN(160) IGCDTA(*YES)')

            # verificamos si el comando fue exitoso
            if msg[0]:

                # armamos el comando
                str = f'CPYSPLF FILE({sfname}) TOFILE({sflib}/{sffile}) JOB({sfjobnum}) SPLNBR({fnum})'

                # ejecutamos el comando
                msg = self.GetCmdMsg(str)

                # verificamos si el comando fue exitoso
                if msg[0]:

                    # obtenemos el archivo de texto del spool
                    self.FtpGetText(sflib, sffile, sffile, dest)
                    print('download successfully!')
        return msg
    
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # grabamos un mensaje en la cola de datos
    def PutMsg(self, qlib, qname, msg):
        """
        qlib    = Es el nombre de la biblioteca de la dataq
        qname   = Es el nombre de la dataq
        msg   = Es el mensaje que gramaos en la dataq
        """
        qstr = f'/QSYS.LIB/{qlib}.LIB/{qname}.DTAQ'
        dataqueue = self.DataQueue(self.system, qstr)
        dataqueue.write(msg)


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # leemos un mensaje de la cola de datos
    def GetMsg(self,qlib,qname):
        """
        qlib    = Es el nombre de la biblioteca de la dataq
        qname   = Es el nombre de la dataq
        """
        qstr = f'/QSYS.LIB/{qlib}.LIB/{qname}.DTAQ'
        dataqueue = self.DataQueue(self.system, qstr)

        # Leemos la dataq
        dqdata = dataqueue.read()
        dqdatastr = 'No data'
        if dqdata != None:
            dqdatastr = dqdata.getString()
            print(dqdatastr)
            return dqdatastr

    #if __name__ == '__main__':
    #    pass


# prod = JT400Helper('172.16.5.19', 'gxusr', 'genexus')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# obtenemos un cursor de un sql
#cmdstr = 'select * from gxprod.tiporegistro'
#prod.GetSQLResult(cmdstr=cmdstr)
#print('funciono')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# verificamos si existe un objeto tipo file
#lib, file = 'epagos', 'INFOR00003'
#respuesta = prod.CheckObjExists( lib, file, type="*FILE")
#print(respuesta)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# generamos un archivo fisico la respuesta es una lista
# donde la posicion 0 tiene valor True, False
# La posicion 1 en adelante son el detalle de los mensajes

"""

crtpfparam = dict()
tablas = list()

crtpfparam['lib'] = 'epagos'
crtpfparam['file'] = 'INFOR00001'
crtpfparam['src'] = 'QDDSSRC'
tablas.append(crtpfparam)

crtpfparam['lib'] = 'epagos'
crtpfparam['file'] = 'INFOR00002'
crtpfparam['src'] = 'QDDSSRC'
tablas.append(crtpfparam)


for elemento in tablas:
    str = f'CRTPF FILE({elemento["lib"]}/{elemento["file"]}) SRCFILE({elemento["lib"]}/{elemento["src"]})'
    respuesta = prod.GetCmdMsg(str)

"""










