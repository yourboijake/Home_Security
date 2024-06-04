from flask import Flask, Response, render_template, request
from datetime import datetime, timedelta
import json

MAX_QUEUE_SIZE = 100
FRAMERATE = 2  #frames per second
app = Flask(__name__)

#implement user verification for toggle API

#implement user verification for main page


@app.route('/', methods= ["GET", "POST"])
def home():
    if request.method == "POST":
        email_switch = request.form.get("email_switch")
        print(type(email_switch))

        #set values in settings.json and emails.txt
        with open('settings.json', 'w') as f:
            data = {}
            data['email_switch'] = request.form.get("email_switch")
            data['capture_switch'] = request.form.get("capture_switch")
            data['stream_toggle'] = request.form.get("stream_toggle")
            new_json = json.dumps(data, indent=4)
            f.write(new_json)

        with open('emails.txt', 'a') as f:
            f.write(request.form.get("email"))
    
    #retrieve settings values
    with open('settings.json', 'r') as f:
        data = json.load(f)
        email_switch = data['email_switch']
        capture_switch = data['capture_switch']
        stream_toggle = data['stream_toggle']

    return render_template('index.html', email_switch=email_switch, capture_switch=capture_switch, stream_toggle=stream_toggle)

@app.route('/togglestatus')
def toggle_api():
    user_cred = request.authorization.parameters
    cred = json.loads(open('cred.json', 'r').read())
    print(user_cred)
    print(cred)
    if cred.get(user_cred['username']) == user_cred['password']:
        stream_toggle = json.load(open('settings.json', 'r'))['stream_toggle']
        return {"stream_toggle" : stream_toggle}
    return '<h2>Authentication Failed</h2>', 401


if __name__ == '__main__':
    app.run(host='0.0.0.0')