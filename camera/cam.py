from utils import capture_image, send_image, toggle_scp
import os
import time
from datetime import datetime
import json
import cv2
import logging

'''
main function that captures images and sends to remote server

the main loop is as follows:
- every X seconds, send API request to server to identify whether or not to stream images
- if true, capture image and scp
- if false, continue iterating until next API call

'''

#load in credentials
api_cred = json.load(open('api_cred.json'))
scp_cred = json.load(open('scp_cred.json'))

#camera setup and settings
cv2_camera = cv2.VideoCapture(0)
FRAMERATE = 0.5  #frames per second
STREAM_TOGGLE = False #send frames or not, boolean

start_ts = datetime.now()
while True:
    #define API call logic here

    if STREAM_TOGGLE == True:
        img_fname = capture_image(cv2_camera=cv2_camera)
        process = send_image(img_fname=img_fname, scp_cred=scp_cred)
        if process.returncode != 0:
            open('err.log', 'a').write(process.stderr)
            logging.warning('Failed to scp file to remote server')

        time.sleep(1.0 / FRAMERATE)
    else:
        time.sleep(1)