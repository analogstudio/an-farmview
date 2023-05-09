import os
import requests
import pprint

import an_farmview.ubl

def post():
    url = f'{os.getenv("AN_FARMVIEW_API_URL")}/api/setubl'

    data = an_farmview.ubl.get_ubl_data()
    print(f'{__name__} - data to post: {data}')
    r = requests.post(url, json=data)
    print('requests.post result:\n\t')
    pprint.pprint(r.json())

def get():
    url_get = f'{os.getenv("AN_FARMVIEW_API_URL")}/api/getubl'
    getr = requests.get(url_get)
    pprint.pprint(getr.json())

if __name__ == '__main__':
    post()
