import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import settings

import an_farmview.snmp
import an_farmview.ubl

app = FastAPI()


app.mount('/static', StaticFiles(directory='an_farmview/static'), name="static")
templates = Jinja2Templates(directory='an_farmview/templates')


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get('/api/temp')
def api_temp():
    temperature_front = an_farmview.snmp.get_temperature_front()
    temperature_rear = an_farmview.snmp.get_temperature_rear()
    data = {
        'front': temperature_front,
        'rear': temperature_rear,
        }
    
    return data


@app.get('/api/ubl')
def api_ubl():
    redshift_available = an_farmview.ubl.get_redshift()
    data = {
        'redshift_available': redshift_available,
        }
    
    return data