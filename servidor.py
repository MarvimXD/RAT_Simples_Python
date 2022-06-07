import socket

host = socket.gethostbyname(socket.gethostname())
porta = 8081

servidor = socket.socket()
servidor.bind((host, porta))

print('Servidor Iniciado')
print('Aguardando conexão...')
servidor.listen(1)
client, clienteAdd = servidor.accept()

print(f'{clienteAdd} Conexão estabelecida!')

while True:
    comando = input('Digite o comando ')
    comando = comando.encode()
    client.send(comando)
    resposta = client.recv(1024)
    print(resposta)