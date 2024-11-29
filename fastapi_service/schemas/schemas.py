from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CustomerTraffic(BaseModel):
    name: str
    total_traffic: float

    class Config:
        from_attributes = True


class TrafficQuery(BaseModel):
    customer_name: Optional[str] = Field(None, max_length=100)
    start_date: Optional[datetime] = Field(None)
    end_date: Optional[datetime] = Field(None)
    ip: Optional[str] = Field(None, pattern=r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')


