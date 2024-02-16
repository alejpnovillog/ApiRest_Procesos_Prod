import subprocess
import pexpect


# Datos de conexión SSH
usuario = 'anovillo'
host = 'PUB400.com'
puerto = 2222
contrasena = 'macs6259'

# Construir el comando SSH
comando_ssh = f'ssh {usuario}@{host} -p {puerto}'

# Crear una instancia de pexpect.spawn
ssh_process = pexpect.spawn(comando_ssh)

# Esperar a que aparezca la contraseña y enviarla
ssh_process.expect("anovillo@pub400.com's password:", timeout=120)
ssh_process.sendline(contrasena)

# Imprimir la salida del comando SSH
print("Salida del comando SSH:")
print(ssh_process.read())

# Cerrar la conexión SSHmacs6259

ssh_process.close()
