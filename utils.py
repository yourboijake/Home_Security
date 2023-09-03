import cv2
import numpy as np
import time
from datetime import datetime

#displays image until a key is pressed
def show_image(np_array, sleep_time=5):
	cv2.imshow("test", np_array)
	time.sleep(sleep_time)
	cv2.destroyAllWindows()

def img_compare_last(last_img: np.array, new_img: np.array):
	last_img = last_img.mean(axis=2).astype('float64') / 255
	new_img = new_img.mean(axis=2).astype('float64') / 255
	comp = np.abs(last_img - new_img)
	return comp

def save_img(img: np.array):
	img_name = datetime.now().strftime("date_%Y_%m_%d_time_%H_%M_%S_%f") + '.jpg'
	cv2.imwrite(img_name, img * 255)
	
#implementation of a queue class for images
class ImgQueue:
	def __init__(self):
		self.imgs = []
	
	def queue_size(self):
		return len(self.imgs)
	
	def enqueue(self, img: np.array):
		self.imgs.append(img)
	
	#remove oldest element in the queue
	def dequeue(self):
		try:
			del self.imgs[0]
		except:
			print("cannot dequeue empty queue")
