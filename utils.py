import cv2
import numpy as np
import time
from datetime import datetime

#displays image until a key is pressed
def show_image(np_array, sleep_time=5) -> None:
	cv2.imshow("test", np_array)
	time.sleep(sleep_time)
	cv2.destroyAllWindows()

def take_image(camera) -> np.array:
	ret, img = camera.read()
	img = img.mean(axis=2) #convert b&w
	img = img.astype('float64') / 255 #scale 0 - 1
	return img

def img_compare_last(last_img: np.array, new_img: np.array) -> np.array:
	return np.abs(last_img - new_img)

def save_img(img: np.array, folder=''):
	img_name = datetime.now().strftime("date_%Y_%m_%d_time_%H_%M_%S_%f") + '.jpg'
	cv2.imwrite(folder + img_name, img * 255)
	
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
