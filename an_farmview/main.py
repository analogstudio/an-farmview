import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import settings

import an_farmview.snmp
import an_farmview.ubl

app = FastAPI()


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app.mount('/static', StaticFiles(directory=str(Path(BASE_DIR, 'templates'))), name="static")

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))



@app.get('/')
def root():
    return {
        "app_name": settings.app_name,
        "items_per_user": settings.items_per_user,
        "dnp": settings.fno_server,
    }

@app.get("/home/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("home.html", {"request": request, "id": id})


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
    
    # return json.dumps(data)
    return data

@app.get('/api/ubl')
def api_ubl():
    redshift_available = an_farmview.ubl.get_redshift()
    data = {
        'redshift_available': redshift_available,
        }
    
    return data