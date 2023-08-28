import cv2
import numpy as np
import skimage
import time

#displays image until a key is pressed
def show_image(np_array, sleep_time=5):
    cv2.imshow("test", np_array)
    time.sleep(sleep_time)
    cv2.destroyAllWindows()

def img_compare_history_blend(history: list, new_img: np.array):
    hist_blur = map(lambda img1, img2: skimage.util.compare_images(img1, img2, method='blur'), history)
    diff = skimage.util.compare_images(hist_blur, new_img, method='diff')
    return diff

def img_compare_last(last_img: np.array, new_img: np.array):
    comp = skimage.util.compare_images(last_img, new_img, method='diff')
    return comp

def save_img(img: np.array, img_name: str):
    cv2.imwrite(img_name, img * 255)