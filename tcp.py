import socket


#TCP_IP = '127.0.0.1'
TCP_IP = '18.221.231.46'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = bytes("Hello, World!", 'utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    msg = input('>')
    s.send(bytes(msg, 'utf-8'))

s.close()
