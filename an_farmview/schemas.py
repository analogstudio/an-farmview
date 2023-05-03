from typing import List, Union
import datetime
from pydantic import BaseModel


class EnvMonitorBase(BaseModel):
    temperature01: int
    temperature02: int
    timestamp: datetime.datetime


class EnvMonitorCreate(EnvMonitorBase):
    pass


class EnvMonitor(EnvMonitorBase):
    id: int

    class Config:
        orm_mode = True

