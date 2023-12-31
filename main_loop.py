import utils
from datetime import datetime
import json
import cv2
import time
import os

#read in config details
config = json.load(open('config.json', 'r'))

#initialize empty queue and camera connection
cam = cv2.VideoCapture(0)

#define path for folder to store images
img_storage_path = ''

old_img = utils.take_image(cam)
print('recording...')
while True:
	new_img = utils.take_image(cam)
	diff = utils.img_compare_last(old_img, new_img)
	old_img = new_img
	if diff.mean() > config['MOTION_SENSITIVITY_THRESHOLD']:
		#send SMTP notification here
		os.system('clear')
		print('motion detected:', diff.mean())
		img_capture_counter = config['IMG_CAPTURE_NUM_IMGS']
	if img_capture_counter > 0:
		utils.save_img(new_img)
		img_capture_counter -= 1

	time.sleep(1 / config['MOTION_DETECTION_FPS'])
