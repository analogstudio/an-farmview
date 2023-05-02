import json
from fastapi import FastAPI

from .config import settings

import an_farmview.snmp
import an_farmview.ubl

app = FastAPI()


@app.get('/')
def root():
    return {
        "app_name": settings.app_name,
        "items_per_user": settings.items_per_user,
        "dnp": settings.fno_server,
    }


# def home():
#     # all the data is made in javascript in the template from api_temp api
#     return render_template('home.html')

@app.get('/api/temp')
def api_temp():
    temperature_front = an_farmview.snmp.get_temperature_front()
    temperature_rear = an_farmview.snmp.get_temperature_rear()
    data = {
        'front': temperature_front,
        'rear': temperature_rear,
        }
    
    return json.dumps(data)

@app.get('/api/ubl')
def api_ubl():
    redshift_available = an_farmview.ubl.get_redshift()
    data = {
        'redshift_available': redshift_available,
        }
    
    return data