# Home_Security

This repo contains instructions for a DIY home security system.

Hardware:
- Raspberry Pi 1 Model B+ ($30)
- ATPro 1080p Webcam ($10)
- MicroUSB charger (under $5)
- ethernet cable (under $5), or wifi adapter (~$20)
- external monitor (useful for setup)

Software:
- Raspberry Pi OS
- Python, with additional packages:
    - numpy
    - opencv
    - scikit-image
    - smtplib
- SMTP server (Postfix? Sendmail?)
- scripts in this repo

Installation Steps:
- boot Raspberry Pi OS on the Raspberry Pi
- install python, and relevant packages
- connect webcam, configure to take pictures with webcam (include test_webcam.py script to make sure its working)
- set up SMTP for sending notification of captured movement
- configure settings: 
    - MOTION_SENSITIVITY_THRESHOLD: (may vary due to placing, lighting, etc.)
    - IMG_STORAGE_DURATION_DAYS (delete stored pictures over X days old)
    - IMG_HISTORY_LENGTH: how many of previous photos should be compared against newest photo?
    - MOTION_DETECTION_FPS: how many pictures should be taken each second?
    - IMG_CAPTURE_FPS: how many pictures per second after motion is detected?
    - IMG_CAPTURE_DURATION_SECONDS: for how many seconds after motion is detected should images be captured?
    - SMTP_ADDRESS: address to send SMTP to, for notifications of motion detected
- how do you remote turn on/off the main script?
    - send SMTP to the device?, have cron jobs that periodically checks for new SMTP messages. If a STOP message comes in, kill the python process. If a START message comes in and the python process isn't running, start the python process
	- use SSH from mobile: get SSH client on my phone, and SSH into the Pi, executing the python script
- streaming to a phone?
