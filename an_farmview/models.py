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