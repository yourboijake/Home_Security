Directory structure explanation:
- the camera directory contains all code that will be run on the Raspberry Pi
- the server directory contains all code that will be run on your remote server

Hardware requirements:
- Raspberry Pi, with internet connectivity
- USB webcam

Software installation steps:


Dev TODO:
- configure HTTPS for the server
- add pw protection to home page: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
- add SMTP to send emails on motion capture
- add S3 connection to save images (renaming the files with current ts)
- improve streaming quality: image glitches and high latency
- configure toggle to show no image unless toggle_stream is set to true
- make it look pretty! (CSS)

Testing TODO:
- motion detection algorithm
- configure auth for toggle REST API


Finished Testing:
- set up REST API on server to toggle camera streaming: https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/
- set up camera script to capture video and scp to server
- running Flask app on server, streaming video
- allow setting to turn toggle on and off
 