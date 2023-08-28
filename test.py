'''
thoughts on how to compare images:
- improve normalization by averaging pixel values of whole history
- MSE is pretty primitive -> maybe it will work for stationary camera?

Alternative algorithm for checking for movement:
- compare images using scikit-image diff: diff = diff(img at t, img at t - 1)
- compute movement metric:
    - mean pixel value of diff
    - max pixel value of diff
- using some configurable sensitivity threshold s, define that movement has occurred when

Enhancements:
- denoising the diff: there will be some differences from shadows, etc. 
to avoid false positives or false negatives: one approach would be to use blur to get a sort of moving
average of the photos over time

main program:
    //fills photo history queue
    while number of imgs in photo history queue < IMG_HISTORY_LENGTH:
        take photo
        add to queue
    
    //main loop
    while True:
        take photo
        compare to queue
        if difference > MOTION_SENSITIVITY_THRESHOLD:
            send SMTP notification to SMTP_ADDRESS
            img_capture_counter = 0
            while img_capture_counter < IMAGE_CAPTURE_DURATION:
                save photo, with timestamp in photo name
                purge oldest photo from queue, deleting from memory
                add photo to queue
                take new photo
                img_capture_counter++
                sleep IMAGE_CAPTURE_FRAME_RATE
        else:
            sleep MOTION_DETECTION_FRAME_RATE

Additional issues:
- logging (for saving photos, purging history, and logging errors)

'''

import cv2
import numpy as np
import os
import skimage

#displays image until a key is pressed
def show_image(np_array):
    cv2.imshow("test", np_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#takes two images as np arrays, used MSE to compare how
#different they are, normalized by average of summed pixel values
#in each image
def img_compare(img1, img2):
    mse = ((img1 - img2) ** 2).mean()
    return mse

def img_compare_history(history: list, 
                        new_img: np.array):
    hist_avg = sum(history) / len(history)
    norm = hist_avg.mean()
    mse = img_compare(new_img, hist_avg) / norm
    return mse

def img_compare_history_blend(history: list, new_img: np.array):
    hist_blur = map(lambda img1, img2: skimage.util.compare_images(img1, img2, method='blur'), history)
    diff = skimage.util.compare_images(hist_blur, new_img, method='diff')
    return diff

WEBCAM_PATH = '/home/jacob/Pictures/Webcam'
imgs = sorted([img for img in os.listdir(WEBCAM_PATH) if '.jpg' in img])
print(imgs)

#read in as GRAY_SCALE
img1 = cv2.imread(WEBCAM_PATH+'/'+imgs[0], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(WEBCAM_PATH+'/'+imgs[1], cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(WEBCAM_PATH+'/'+imgs[2], cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread(WEBCAM_PATH+'/'+imgs[3], cv2.IMREAD_GRAYSCALE)

img_list = [img1, img2, img3, img4]
for i in range(len(img_list)):
    for j in range(len(img_list)):
        mse = img_compare(img_list[i], img_list[j])
        print(f'mse of {i+1}, {j+1}:', mse)

hist = [img1, img2, img3]
mse = img_compare_history(hist, img4)
print(mse)

method='diff'
comp1 = skimage.util.compare_images(img1, img2, method=method)
comp2 = skimage.util.compare_images(img1, img3, method=method)

#read in as RGB
#im1 = cv2.imread(WEBCAM_PATH+'/'+imgs[0], cv2.IMREAD_COLOR)

#show_image(img1)
#show_image(img2)
#show_image(img3)

#show_image(comp1)
#show_image(comp2)


print('diff of img1 and img 2')
print(comp1.mean())
print('\ndiff of img1 and img 3')
print(comp2.mean())
print(comp1.max())
print(comp2.max())

#cv2.imwrite("comp1.jpg", comp1 * 255)
#cv2.imwrite("comp2.jpg", comp1 * 255)

method='blend'
comp1 = skimage.util.compare_images(img1, img2, method=method)
comp2 = skimage.util.compare_images(img1, img3, method=method)

#print('blend of img1 and img2')
#show_image(comp1)
#print('\nblend of img1 and img3')
#show_image(comp2)
#import pdb; pdb.set_trace()


#import pdb; pdb.set_trace()
