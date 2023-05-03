import requests
import pprint

import an_farmview.snmp
    
def post():
    url = 'http://127.0.0.1:5000/envmonitor'

    data = {
        "temperature01": an_farmview.snmp.get_temperature_rear(),
        'temperature02': an_farmview.snmp.get_temperature_front()
        }

    r = requests.post(url, json=data)
    pprint.pprint(r.json())

def get():
    url_get = 'http://127.0.0.1:5000/envmonitors'
    getr = requests.get(url_get)
    pprint.pprint(getr.json())


if __name__ == '__main__':
    post()