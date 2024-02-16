try:

    import os

    from pydal.objects import Table

    # Clase de configuracion
    from app_Config.config import ConfigurarAplicacion

    # Gestion Registros
    from app_Abstract.gestionRegistros import GestionRegistros

    # Libreria para usar ssh
    import paramiko


except Exception as e:
    print(f'Falta algun modulo {e}')


try:

    # Datos de conexión SSH
    host = 'PUB400.COM'
    usuario = 'anovillo'
    contrasena = 'macs6259'
    puerto = 2222  # Reemplaza con el puerto que estás utilizando

    # Crear una instancia de la clase SSHClient
    cliente_ssh = paramiko.SSHClient()

    # Cargar las claves del sistema local
    cliente_ssh.load_system_host_keys()

    # Configurar una política para gestionar claves de 
    # host desconocidas (puedes ajustar esto según tus necesidades)
    cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Conectar al host remoto con nombre de usuario, contraseña y puerto
    cliente_ssh.connect(host, port=puerto, username=usuario, password=contrasena)

    # Verificar el estado de la conexión
    if cliente_ssh.get_transport().is_active():
        print("Conexión SSH exitosa.")
    else:
        print("La conexión SSH no está activa.")


    # Ejecutar comandos remotos
    stdin, stdout, stderr = cliente_ssh.exec_command('cd ..')


    # Imprimir la salida del comando remoto
    print(stdout.read())

    # Ejecutar comandos remotos
    stdin, stdout, stderr = cliente_ssh.exec_command('ls')

    #salida_del_comando = stdout.read().decode('utf-8')
    salida_del_comando = stdout.read()
    print("Salida del comando 'ls':")
    print(salida_del_comando)

    # Imprimir la salida del comando remoto
    #print(stdout.read().decode('utf-8'))

    # Cerrar la conexión SSH
    cliente_ssh.close()

except Exception as e:
    print(f"Error al conectar: {e}")
finally:
    # Cerrar la conexión SSH en caso de éxito o fallo
    cliente_ssh.close()







