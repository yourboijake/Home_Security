import cv2, imutils, socket
import numpy as np
import time, base64
import queue

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
socket_address = ('', 9999)
server_socket.bind(socket_address)
print('listening at', socket_address)

cam = cv2.VideoCapture(0)

def send_img(client_socket, img: np.array):
    encoded, buffer = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY,80])
    message = base64.b64encode(buffer)
    server_socket.sendto(message, client_addr)

#main loop
for i in range(50):
    ret, img = cam.read()
    if ret:
        send_img(client_socket, img)
    else:
        print('failed in frame', i)
    time.sleep(1)