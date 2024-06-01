import sys
import socket

#usage: $ python3 test.py ip.addr.of.ec2
#test that I can send and recieve TCP packets

IP = sys.argv[1]
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'attempting to connect on ', (IP, 5097))
clientsocket.connect((IP, 5097))

msg = bytes('hello world', 'utf-8')
clientsocket.send(msg)






