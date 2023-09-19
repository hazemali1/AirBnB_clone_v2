#!/usr/bin/python3
"""
Module with class City
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
    """
    City
    """
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
