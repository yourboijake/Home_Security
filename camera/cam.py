from utils import capture_image, send_image, toggle_scp
import os
import time

'''
main function that captures images and sends to remote server

the main loop is as follows:
- every X seconds, send API request to server to identify whether or not to stream images
- if true, capture image and scp
- if false, continue iterating until next API call

'''