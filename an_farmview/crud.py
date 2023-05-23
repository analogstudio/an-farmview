from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import desc

from . import models, schemas
from .config import settings


def get_envmonitor(db: Session, envmonitor_id: int):
    return db.query(models.EnvMonitor).filter(models.EnvMonitor.id == envmonitor_id).first()


def get_envmonitors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EnvMonitor).order_by(desc(models.EnvMonitor.timestamp)).offset(skip).limit(limit).all()


def create_envmonitor(db: Session, envmonitor: schemas.EnvMonitorCreate):


    limit_rowcount(db=db, model=models.EnvMonitor)

    db_envmonitor = models.EnvMonitor(
        timestamp=func.now(),
        temperature01=envmonitor.temperature01,
        temperature02=envmonitor.temperature02
    )
    
    db.add(db_envmonitor)
    db.commit()
    db.refresh(db_envmonitor)
    return db_envmonitor


def get_ubl(db: Session, skip: int=0, limit: int=100):
    return db.query(models.UBL).order_by(desc(models.UBL.timestamp)).offset(skip).limit(limit).all()



def create_ubl(db: Session, ubl: schemas.UBLCreate):

    limit_rowcount(db=db, model=models.UBL)

    db_ubl = models.UBL(
        timestamp=func.now(),
        redshift_entitled=ubl.redshift_entitled,
        redshift_used=ubl.redshift_used,
        redshift_available=ubl.redshift_available,

        nuke_entitled=ubl.nuke_entitled,
        nuke_used=ubl.nuke_used,
        nuke_available=ubl.nuke_available,
    )
    
    db.add(db_ubl)
    db.commit()
    db.refresh(db_ubl)
    return db_ubl

def limit_rowcount(db: Session, model):

    row_count = db.query(model).count()

    if row_count > settings.max_table_row_count:
        to_delete = row_count - settings.max_table_row_count

        rows_to_delete = db.query(model).order_by(model.id.asc()).limit(to_delete)

        for row in rows_to_delete:
            print(f'{row.id}, {row.timestamp}')
            db.delete(row)

        db.commit()
        print(f'Rows: {row_count} is greater than settings {settings.max_table_row_count}')
    else:
        print(f'Rows: {row_count} is not greater than settings {settings.max_table_row_count}')

    return row_count
