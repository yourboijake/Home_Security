from flask import Flask, Response, render_template, request
import cv2
import time
from datetime import datetime, timedelta
import threading
import os
import json

MAX_QUEUE_SIZE = 100
FRAMERATE = 2  #frames per second
app = Flask(__name__)

#define image capture thread
cam = cv2.VideoCapture(0)
def img_snap():
    while True:
        time.sleep(1.0 / FRAMERATE)
        #capture and save new frame
        success, frame = cam.read()
        ts = datetime.now().strftime('%m-%d-%Y_%H-%M-%S-%f')
        #fname = 'static/' + ts + '.jpg'
        fname = 'static/display_img.jpg'
        cv2.imwrite(fname, frame)


@app.route('/', methods= ["GET", "POST"])
def home():
    if request.method == "POST":
        email_switch = request.form.get("email_switch")
        print(type(email_switch))

        #set values in settings.json and emails.txt
        with open('settings.json', 'w') as f:
            data = {}
            data['email_switch'] = request.form.get("email_switch")
            data['capture_switch'] = request.form.get("capture_switch")
            new_json = json.dumps(data, indent=4)
            f.write(new_json)

        with open('emails.txt', 'a') as f:
            f.write(request.form.get("email"))
    
    #if signin is a success, render the main page with video stream and settings
    #retrieve settings values
    with open('settings.json', 'r') as f:
        data = json.load(f)
        email_switch = data['email_switch']
        capture_switch = data['capture_switch']

    return render_template('index.html', email_switch=email_switch, capture_switch=capture_switch)


if __name__ == '__main__':
    #clear out any existing images
    #os.system('rm static/05-*.jpg')

    #initialize queue, and thread to take snapshots and populate queue
    t = threading.Thread(target=img_snap, args=())
    t.start()
    time.sleep(1)

    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)