import os
import requests
import pprint

from an_farmview.config import settings

import an_farmview.snmp
    
def post():
    url = f'{settings.an_farmview_api_url}/envmonitor'

    data = {
        "temperature01": an_farmview.snmp.get_temperature_rear(),
        'temperature02': an_farmview.snmp.get_temperature_front()
        }

    r = requests.post(url, json=data)
    pprint.pprint(r.json())

def get():
    url_get = f'{settings.an_farmview_api_url}/envmonitors'
    getr = requests.get(url_get)
    pprint.pprint(getr.json())


if __name__ == '__main__':
    post()