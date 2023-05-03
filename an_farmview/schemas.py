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

