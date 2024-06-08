import cv2
from skimage.metrics import mean_squared_error

#function to calibrate motion detectin parameters
def calibrate():
    old_frame, new_frame = None, None
    mse_vals = []
    cam = cv2.VideoCapture(0)
    img_count = 0
    print('running img capture loop')
    while True:
        ret, frame = cam.read()
        img_count += 1
        old_frame = new_frame
        new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if old_frame is not None and new_frame is not None:
            mse = mean_squared_error(old_frame, new_frame)
            mse_vals.append(mse)
        
        if cv2.waitKey(1) == 27 or img_count > 100:
            break  # quit on esc key or > 5k imgs

    threshold = max(mse_vals) / 2
    return threshold

print(calibrate())