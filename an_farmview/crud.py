from sqlalchemy.orm import Session

from . import models, schemas


def get_envmonitor(db: Session, envmonitor_id: int):
    return db.query(models.EnvMonitor).filter(models.EnvMonitor.id == envmonitor_id).first()


# def get_envmonitor_by_email(db: Session, email: str):
#     return db.query(models.EnvMonitor).filter(models.EnvMonitor.email == email).first()


def get_envmonitors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EnvMonitor).offset(skip).limit(limit).all()


def create_envmonitor(db: Session, envmonitor: schemas.EnvMonitorCreate):

    db_envmonitor = models.EnvMonitor(
        timestamp=envmonitor.timestamp,
        temperature01=envmonitor.temperature01,
        temperature02=envmonitor.temperature02
    )
    
    db.add(db_envmonitor)
    db.commit()
    db.refresh(db_envmonitor)
    return db_envmonitor

