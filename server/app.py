from flask import Flask, Response, render_template, request
import cv2
import time
from datetime import datetime, timedelta
import threading
import os
import queue

MAX_QUEUE_SIZE = 100
FRAMERATE = 2  #frames per second
app = Flask(__name__)

#define image capture thread
cam = cv2.VideoCapture(0)
def img_snap(q):
    while True:
        time.sleep(1.0 / FRAMERATE)
        #capture and save new frame
        success, frame = cam.read()
        ts = datetime.now().strftime('%m-%d-%Y_%H-%M-%S-%f')
        #fname = 'static/' + ts + '.jpg'
        fname = 'static/display_img.jpg'
        cv2.imwrite(fname, frame)

        #append filename to queue
        #q.put(fname)

        #delete images when queue gets to half full, need to modify this logic for motion detection
        #print(q.qsize())
        #while q.qsize() > (MAX_QUEUE_SIZE / 2):
        #    fname = q.get()
        #    os.system(f'rm {fname}')


@app.route('/')
def home():
    return render_template('photoref.html')

if __name__ == '__main__':
    #clear out any existing images
    #os.system('rm static/05-*.jpg')

    #initialize queue, and thread to take snapshots and populate queue
    q = queue.Queue(maxsize=MAX_QUEUE_SIZE)
    t = threading.Thread(target=img_snap, args=(q,))
    t.start()

    time.sleep(1)
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)