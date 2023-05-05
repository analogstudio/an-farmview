import os
import requests
import pprint

import an_farmview.snmp
    
def post():
    url = f'{os.getenv("AN_FARMVIEW_API_URL")}/envmonitor'

    data = {
        "temperature01": an_farmview.snmp.get_temperature_rear(),
        'temperature02': an_farmview.snmp.get_temperature_front()
        }

    r = requests.post(url, json=data)
    pprint.pprint(r.json())

def get():
    url_get = f'{os.getenv("AN_FARMVIEW_API_URL")}/envmonitors'
    getr = requests.get(url_get)
    pprint.pprint(getr.json())


if __name__ == '__main__':
    post()