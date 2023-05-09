from typing import List, Union
import datetime
from pydantic import BaseModel


class EnvMonitorBase(BaseModel):
    temperature01: int
    temperature02: int


class EnvMonitorCreate(EnvMonitorBase):
    pass


class EnvMonitor(EnvMonitorBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True


class UBLBase(BaseModel):
    redshift_entitled: int
    redshift_used: int
    redshift_available: int

    nuke_entitled: int
    nuke_used: int
    nuke_available: int


class UBLCreate(UBLBase):
    pass


class UBL(UBLBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True
