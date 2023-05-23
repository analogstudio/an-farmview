import math
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import settings

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

import an_farmview.snmp
import an_farmview.ubl

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.mount('/static', StaticFiles(directory='an_farmview/static'), name="static")
templates = Jinja2Templates(directory='an_farmview/templates')


# using database stuff
@app.post("/envmonitor", response_model=schemas.EnvMonitor)
def create_envmonitor(envmonitor: schemas.EnvMonitorCreate, db: Session = Depends(get_db)):
    return crud.create_envmonitor(db=db, envmonitor=envmonitor)


@app.get("/envmonitors", response_model=List[schemas.EnvMonitor])
def read_envmonitors(skip: int = 0, limit: int = 300, db: Session = Depends(get_db)):
    envmonitors = crud.get_envmonitors(db, skip=skip, limit=limit)
    return envmonitors


@app.post("/api/setubl", response_model=schemas.UBL)
def create_ubl(ubl: schemas.UBLCreate, db: Session = Depends(get_db)):
    return crud.create_ubl(db=db, ubl=ubl)


@app.get("/api/getubl", response_model=List[schemas.UBL])
def read_ubl(skip: int = 0, limit: int = 10000, db: Session = Depends(get_db)):
    ubl = crud.get_ubl(db, skip=skip, limit=limit)
    return ubl


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


@app.get('/api/ubl_info')
def api_ubl_info(db: Session = Depends(get_db)):
    """
    returns some nicely formatted info easier in python than js...
    """

    # read from our API
    ubl = crud.get_ubl(db, skip=0, limit=1)
    
    mins = [ubl[0].redshift_available, ubl[0].nuke_available]

    return_string = []

    return_string.append(mins_info(mins[0], 'Redshift'))
    return_string.append(mins_info(mins[1], 'Nuke'))

    data = {
        'redshift_mins': f'{mins[0]:,}',
        'redshift_hours_mins': '<br>'.join(return_string),
        }
    
    return data


def mins_info(mins, name):
    # cover 'null'
    if not isinstance(mins, int):
        return ''
    
    # eg. if 10 machines / 10
    test_mins = mins / 10
    time_days = math.floor(test_mins / (60*24))
    time_mins_remainder = test_mins % (60*24)
    time_hours = math.floor(time_mins_remainder / 60)
    time_mins = int(time_mins_remainder % 60)

    return f'{name}: eg. 10 machines 24/7 : {time_days}days {time_hours}hours {time_mins}mins'
