import json
import cv2
import os
import subprocess

#capture image, returning image name
def capture_image(cv2_camera) -> str:
    ret, frame = cv2_camera.read()
    img_fname = 'display_img.jpg'
    cv2.imwrite(img_fname, frame)

    return img_fname

#send image to remote server
def send_image(img_fname, scp_cred) -> subprocess.CompletedProcess:
    cmd = ['scp', '-i', scp_cred['keypath'], img_fname, scp_cred["user"] + '@' + scp_cred['ip'] + ':' + scp_cred['file_destination_path']]
    process = subprocess.run(cmd, capture_output=True, text=True)
    return process

#function that accesses REST API on server to identify whether it should be streaming or not 
def toggle_scp(keypath, api_cred):
    pass
