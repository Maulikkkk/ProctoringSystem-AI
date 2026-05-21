import json

SESSION_FILE = "session_data.json"

def load_session():

    with open(SESSION_FILE, "r") as f:
        return json.load(f)

def save_session(data):

    with open(SESSION_FILE, "w") as f:
        json.dump(data, f, indent=4)

def increment_event(event_name):

    data = load_session()

    data[event_name] += 1

    save_session(data)