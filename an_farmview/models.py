import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,  DateTime
from sqlalchemy.orm import relationship

from .database import Base

from sqlalchemy.sql import func

class EnvMonitor(Base):
    __tablename__ = "envmonitor"

    id = Column(Integer, primary_key=True, index=True)
    
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    temperature01 = Column(Integer)
    temperature02 = Column(Integer)


class UBL(Base):
    __tablename__ = "ubl"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    redshift_entitled = Column(Integer)
    redshift_used = Column(Integer)
    redshift_available = Column(Integer)
    nuke_entitled = Column(Integer)
    nuke_used = Column(Integer)
    nuke_available = Column(Integer)