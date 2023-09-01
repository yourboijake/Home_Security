#trying to get a video stream working, since that would be cool

'''
resources: https://pyshine.com/How-to-send-audio-video-of-MP4-using-sockets-in-Python/
https://medium.com/nerd-for-tech/developing-a-live-video-streaming-application-using-socket-programming-with-python-6bc24e522f19
https://sourcenet.hashnode.dev/video-streaming-using-socket-programming-in-python


'''

import cv2
import imutils
import socket
import struct
import pickle
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('host ip: ', host_ip)
port = 9999
#socket_address = (host_ip, port)
socket_address = ('', port)

#bind socket, listening to incoming requests on that IP and port
server_socket.bind(socket_address)
server_socket.listen(2)
print('listening at:', socket_address)


encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
#struct_pack_method = "Q"
struct_pack_method=">L"
while True:
    client_socket, addr = server_socket.accept()
    print("got connection from:", addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while vid.isOpened():
            ret, frame = vid.read()
            result, frame = cv2.imencode('.jpg', frame, encode_param)

            #resize image, maintianing aspect ratio
            #frame = imutils.resize(frame, width=200)
            
            #don't use pickle, just try to send raw bytes
            #could try something like this: https://github.com/sabjorn/NumpySocket/blob/main/numpysocket/numpysocket.py
            #or using pickle: https://gist.github.com/kittinan/e7ecefddda5616eab2765fdb2affed1b
            #more examples: https://codereview.stackexchange.com/questions/156732/protocol-implementation-tcp-sending-images-through-sockets-follow-up
            
            data = pickle.dumps(frame, protocol=0)
            print(len(data))
            message = struct.pack(struct_pack_method, len(data)) + data
            try:
                client_socket.sendall(message)
            except:
                pass

            cv2.imshow("TRANSMITTING VIDEO", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
                break

cv2.destroyAllWindows()

