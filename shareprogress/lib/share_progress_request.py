import requests
import json

class shareProgressRequest():
    def create_button(self, payload):
        headers = {'Content-Type': 'application/json'}
        r = requests.post("https://run.shareprogress.org/api/v1/buttons/update",
            data=json.dumps(payload), headers=headers)
        return r.json()

    def read_button(self, payload):
        headers = {'Content-Type': 'application/json'}
        r = requests.get("https://run.shareprogress.org/api/v1/buttons/read",
            data=json.dumps(payload), headers=headers)
        return r.json()
