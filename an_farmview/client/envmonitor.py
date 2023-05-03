import requests
import pprint

def post():
    url = 'http://127.0.0.1:5000/envmonitor'

    data = {
        "temperature01": 99,
        'temperature02': 99
        }

    r = requests.post(url, json=data)
    pprint.pprint(r.json())

def get():
    url_get = 'http://127.0.0.1:5000/envmonitors'
    getr = requests.get(url_get)
    pprint.pprint(getr.json())


if __name__ == '__main__':
    post()