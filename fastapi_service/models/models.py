from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Traffic(Base):
    __tablename__ = "traffic"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    ip = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    received_traffic = Column(Float, nullable=False)
    customer = relationship("Customer", back_populates="traffic")


Customer.traffic = relationship(
    "Traffic", order_by=Traffic.id, back_populates="customer"
)
