import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 5097))
serversocket.listen(5) # become a server socket, maximum 5 connections
print('server listening')

while True:
    connection, address = serversocket.accept()
    print('recieved connection from', connection, address)
    buf = connection.recv(1024)
    if len(buf) > 0:
        print(buf)
    
