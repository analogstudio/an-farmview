from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import desc

from . import models, schemas


def get_envmonitor(db: Session, envmonitor_id: int):
    return db.query(models.EnvMonitor).filter(models.EnvMonitor.id == envmonitor_id).first()

def get_envmonitors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EnvMonitor).order_by(desc(models.EnvMonitor.timestamp)).offset(skip).limit(limit).all()

def create_envmonitor(db: Session, envmonitor: schemas.EnvMonitorCreate):
    db_envmonitor = models.EnvMonitor(
        timestamp=func.now(),
        temperature01=envmonitor.temperature01,
        temperature02=envmonitor.temperature02
    )
    
    db.add(db_envmonitor)
    db.commit()
    db.refresh(db_envmonitor)
    return db_envmonitor


def get_ubl(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UBL).order_by(desc(models.UBL.timestamp)).offset(skip).limit(limit).all()

def create_ubl(db: Session, ubl: schemas.UBLCreate):
    db_ubl = models.UBL(
        timestamp=func.now(),
        redshift_entitled=ubl.redshift_entitled,
        redshift_used=ubl.redshift_used,
        redshift_available=ubl.redshift_available,
    )
    
    db.add(db_ubl)
    db.commit()
    db.refresh(db_ubl)
    return db_ubl
