import socket

HOST = 'localhost'
PORT = 8002

arquivo = open('thumb.png', 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Envia o nome do arquivo
sock.send(input('Digite o nome do arquivo: ').encode())

# Envia o conteúdo do arquivo
sock.send(arquivo.read())

# Aguarda confirmação do servidor
confirmacao = sock.recv(1024)
if confirmacao == b"ok":
    print('Arquivo enviado com sucesso')

# Fecha o socket depois de terminar a comunicação
sock.close()
