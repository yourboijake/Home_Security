import utils
from datetime import datetime
import json
import cv2
import time

#read in config details
config = json.load(open('config.json', 'r'))

#initialize empty queue and camera connection
iq = utils.ImageQueue()
cam = cv2.VideoCapture(0)

#define path for folder to store images
img_storage_path = ''

#fill history with IMG_HISTORY_LENGTH imgs
while (iq.queue_size() - 1) < config['IMG_HISTORY_LENGTH']:
    return_value, img = cam.read()
    if return_value: iq.enqueue(img)

while True:
    return_value, new_img = cam.read()
    diff = utils.img_compare_last(iq.imgs[-1], new_img)
    if diff.mean() > config['MOTION_SENSITIVITY_THRESHOLD']:
        #send SMTP notification here
        img_capture_counter = 0
        while img_capture_counter < config['IMG_CAPTURE_NUM_IMGS']:
            utils.save_img(new_img)
            iq.dequeue() #purge oldest image from queue
            iq.enqueue(new_img) #add newest image to queue
            return_value, new_img = cam.read()
            img_capture_counter += 1
            time.sleep(1 / config['IMG_CAPTURE_FPS'])
    else:
        time.sleep(1 / config['MOTION_DETECTION_FPS'])
