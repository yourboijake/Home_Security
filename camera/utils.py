import cv2
import subprocess
from datetime import datetime
import requests
import json


#capture image, returning image name
#use_ts parameter is used to tell the image capture to record the timestamp associated with the image
def capture_image(cv2_camera, use_ts=False) -> str:
    ret, frame = cv2_camera.read()
    if use_ts:
        ts = datetime.now().strftime('%m%D%Y%H%M%S%f')
        img_fname = f'display_img_{ts}.jpg'
    else:
        img_fname = f'display_img.jpg'
    cv2.imwrite(img_fname, frame)

    return img_fname

#send image to remote server
def send_image(img_fname, scp_cred) -> subprocess.CompletedProcess:
    cmd = ['scp', '-i', scp_cred['keypath'], img_fname, scp_cred["user"] + '@' + scp_cred['ip'] + ':' + scp_cred['file_destination_path']]
    process = subprocess.run(cmd, capture_output=True, text=True)
    return process

#function that accesses REST API on server to identify whether it should be streaming or not 
def toggle_scp(api_cred) -> dict:
    session = requests.Session()
    session.auth = (api_cred['user'], api_cred['password'])
    res = session.get(api_cred['api_path'])
    return res
