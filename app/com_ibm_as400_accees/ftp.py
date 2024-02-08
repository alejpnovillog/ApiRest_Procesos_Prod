# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion
        from typing import List

except Exception as e:
    print(f'Falta algun modulo {e}')


# Definimos la clase para manejar la iseries
class FTP():

    ACTIVE_MODE = 10
    ASCII = 0
    BINARY = 1
    PASSIVE_MODE = 11

    def __init__( self, server: str, user: str, pasw: str):

        """
        server          - Es la direccion ip del servidor\n

        documentacion
        https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/FTP.html\n

        """

        # asigno la clase Java
        self.ftpIseries = jpype.JClass('com.ibm.as400.access.FTP')

        # La interfaz ConnectionListener proporciona una interfaz
        # de escucha para recibir eventos de conexión.
        self.FTPListener = jpype.JClass('java.util.EventListener')

        # realiza la conexion con la clase Java
        self.systemFtp = self.ftpIseries(server, user, pasw)



    # ***
    #  Agrega un oyente para ser notificado cuando se dispara un evento FTP.
    def addFtpListener(self, FTPListener):
        """
        """         


    # ***
    # Añade datos a un archivo en el sistema.
    def append(self, sourceFileName: str, targetFileName: str)-> bool:
        """

        Args:
            sourceFileName (str):   El nombre del archivo de origen
            targetFileName (str):   El nombre del archivo de destino

        Returns:
            bool:   Retorna si la operacion fue existosa
        """

        return self.systemFtp.append(sourceFileName,targetFileName)                                        

                 

    # ***
    #  Establece el directorio actual en el sistema para directorio.
    def cd(self, directorio: str)-> bool:
        """

        Args:
            directorio (str):     Ubicacion en donde queremos posicionarse en el sistema

        Returns:
            bool:   Retorna si la operacion fue exitosa
        """
        
        return self.systemFtp.cd(directorio)



    # ***
    # Se conecta al sistema.
    def connect(self)-> bool:
        """

        Returns:
            bool:   Retorna si la operacion fue exitosa
        """

        return self.systemFtp.connect()
    


    # ***
    # Se conecta al sistema.
    def dir(self)-> List[str]:
        """

        Returns:
            List[str]:  Retornamos un a lista de string con el nombre del elemento del directorio
        """

        return self.system.dir()         
    

    # ***
    # Se desconecta al sistema.
    def disconnect(self)-> bool:
        """

        Returns:
            bool:   Retorna si la operacion fue exitosa
        """

        return self.systemFtp.disconnect()


    # ***
    #  Obtiene un archivo del sistema.
    def get(self, sourceFileName: str, targetFileName: str)-> bool:
        """

        Args:
            sourceFileName (str):   El nombre del archivo de origen
            targetFileName (str):   El nombre del archivo de destino

        Returns:
            bool:   Retorna si la operacion fue existosa
        """

        return self.systemFtp.get(sourceFileName,targetFileName)                                        



    # ***
    # Devuelve el directorio actual en el sistema.
    def getCurrentDirectory(self)-> str:
        """

        Returns:
            str:        Es el directorio que esta en este momento
        """
        return self.systemFtp.getCurrentDirectory()
    

    # ***
    # Devuelve el texto de la última respuesta devuelta desde el sistema.
    def getLastMessage(self)-> str:
        """

        Returns:
            str:        Es la descripcion del ultima respuesta del sistema
        """
        return self.systemFtp.getLastMessage()



    # ***
    # Devuelve el modo de transferencia actual.
    def getMode(self)-> int:
        """

        Returns:
            int:        Retorna si el modo esta activo o no esta activo
        """
        return self.systemFtp.getMode()


    # ***
    # Devuelve el puerto utilizado para conectarse al sistema.
    def getPort(self)-> int:
        """

        Returns:
            int:        Retorna el numero de port que utiliza para conectar el sistema
        """
        return self.systemFtp.getPort()



    # ***
    # Devuelve el nombre del sistema.
    def getServer(self)-> str:
        """

        Returns:
            str:        Retorna el nombre del sistema
        """
        return self.systemFtp.getServer()


    # ***
    # Devuelve al usuario.
    def getUser(self)-> str:
        """

        Returns:
            str:        Retorna el usuario del sistema
        """
        return self.systemFtp.getUser()



    # ***
    #  Indica si el socket se reutiliza para múltiples transferencias de archivos, 
    #  cuando está en modo activo.
    def isReuseSocket(self)-> bool:
        """

        Returns:
            bool:   Retorna si es verdadero o falso
        """

        return self.systemFtp.isReuseSocket()                                        



    # ***
    #  Envía un comando al sistema, devolviendo la respuesta del sistema.
    def issueCommand(self, cmd: str)-> str:
        """

        Returns:
            str:        Retorna la respuesta del comando enviado al sistema
        """
        return self.systemFtp.issueCommand(cmd)




    # ***
    # Enumera el contenido del directorio de trabajo actual.
    def ls(self)-> List[str]:
        """

        Returns:
            List[str]:  Retornamos un a lista de string con el nombre del elemento del directorio
        """

        return self.systemFtp.ls()         



    # ***
    # Enumera el contenido del directorio de trabajo actual.
    def ls(self, ubicacion)-> List[str]:
        """

        Returns:
            List[str]:  Retornamos un a lista de string con el nombre del elemento del directorio
        """

        return self.systemFtp.ls(ubicacion)         



    # ***
    #  Coloca un archivo en el sistema.
    def put(self, sourceFileName: str, targetFileName: str)-> bool:
        """

        Args:
            sourceFileName (str):   El nombre del archivo de origen
            targetFileName (str):   El nombre del archivo de destino

        Returns:
            bool:   Retorna si la operacion fue existosa
        """

        return self.systemFtp.put(sourceFileName,targetFileName)                                        



    # ***
    # Devuelve el directorio actual en el sistema.
    def pwd(self)-> str:
        """

        Returns:
            str:  Retornamos el nombre del directorio actual
        """

        return self.systemFtp.pwd()         



    # ***
    # Establecemos el tipo de transferencia que vamos a utilizar en el sistema.
    def setDataTransferType(self, transferencia: int):
        """

        Returns:
            int:  Establecemos el tipo de transferencia con el sistema
        """

        return self.systemFtp.setDataTransferType(transferencia)         
