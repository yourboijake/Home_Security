import json

def validate_user(email, pw):
    valid_users = json.load(open('cred.json'))

    try:
        assert valid_users[email] == pw
        return True
    except:
        return False

