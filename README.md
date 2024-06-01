Directory structure explanation:
- the camera directory contains all code that will be run on the Raspberry Pi
- the server directory contains all code that will be run on your remote server

Hardware requirements:
- Raspberry Pi, with internet connectivity
- USB webcam

Software installation steps:


Dev TODO:
- add pw protection to home page: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
- set up REST API on server to toggle camera streaming: https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/
- motion detection algorithm
- add SMTP to send emails on motion capture
- add S3 connection to save images (renaming the files with current ts)


Testing TODO:
- running Flask app on server


Finished Testing:
- set up camera script to capture video and scp to server
 