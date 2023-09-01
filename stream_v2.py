#https://www.youtube.com/watch?v=Kg-sxVmCt5Q
#streaming: https://www.youtube.com/watch?v=UHc24_EhdZk 
#https://pyshine.com/How-to-send-audio-video-of-MP4-using-sockets-in-Python/

import socket
from io import BytesIO
import cv2
import numpy as np
import pickle
import time

#set up camera connection
cam = cv2.VideoCapture(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind(('127.0.1.1', 9999))
server.bind(('', 9999))
server.listen(5)
print('server listening')

client_socket, client_address = server.accept()
print('connected to client at', client_address)

def send_img(client_socket, img: np.array, CHUNK_SIZE_BYTES=262144):
    img_binary = pickle.dumps(img)
    client_socket.sendall(img_binary)
    #img_chunks = [img_binary[i:i+CHUNK_SIZE_BYTES] for i in range(0, len(img_binary), CHUNK_SIZE_BYTES)]
    #for chunk in img_chunks:
    #    client_socket.send(chunk)


#main loop
for i in range(50):
    ret, img = cam.read()
    if ret:
        send_img(client_socket, img)
    else:
        print('failed in frame', i)
    time.sleep(1)

#ret, img = cam.read()
#cv2.imwrite("test_stream_frame.jpg", img)
#img = cv2.imread('comp1.jpg', cv2.IMREAD_GRAYSCALE)
#send_img(client_socket, img)

print('stream sent')
client_socket.close()
server.close()