import os
import requests
import pprint

import an_farmview.ubl

def post():
    url = f'{os.getenv("AN_FARMVIEW_API_URL")}/api/setubl'

    data = an_farmview.ubl.get_redshift2()
    print(f'{__name__} - data: {data}')
    r = requests.post(url, json=data)
    pprint.pprint(r.json())

def get():
    url_get = f'{os.getenv("AN_FARMVIEW_API_URL")}/api/getubl'
    getr = requests.get(url_get)
    pprint.pprint(getr.json())

if __name__ == '__main__':
    post()