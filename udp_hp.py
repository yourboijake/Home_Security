'''
import socket

ip = '172.17.0.1'
#local ip 10.0.5.70
port = 9927

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = bytes('hello world', 'utf-8')

import pdb; pdb.set_trace()

sock.sendto(message, (ip, port))
'''


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#udp_host = '172.17.0.1'
udp_host = '10.0.5.76'
udp_port = 41009

msg = bytes('hello world', 'utf-8')

sock.sendto(msg, (udp_host, udp_port))

