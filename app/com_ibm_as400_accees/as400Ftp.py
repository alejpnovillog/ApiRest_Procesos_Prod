# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion
        from typing import List

except Exception as e:
    print(f'Falta algun modulo {e}')


# Definimos la clase para manejar la iseries
class AS400FTP():

    ACTIVE_MODE = 10
    ASCII = 0
    BINARY = 1
    PASSIVE_MODE = 11

    def __init__( self, iSeriesftp):

        """
        server          - Es la direccion ip del servidor\n

        documentacion
        https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_71/rzahh/javadoc/com/ibm/as400/access/FTP.html\n

        """

        # asigno la clase Java
        self.ftpIseries = jpype.JClass('com.ibm.as400.access.AS400FTP')

        # La interfaz ConnectionListener proporciona una interfaz
        # de escucha para recibir eventos de conexión.
        self.FTPListener = jpype.JClass('java.util.EventListener')

        # realiza la conexion con la clase Java
        self.systemFtp = self.ftpIseries     (iSeriesftp)



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
        
        return self.sytemFtp.cd(directorio)



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

        return self.systemFtp.dir()         
    

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

