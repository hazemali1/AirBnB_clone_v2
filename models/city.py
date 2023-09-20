#!/usr/bin/python3
"""
Module with class City
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """
    City
    """
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    __tablename__ = "cities"
    places = relationship("Place", backref="City", cascade="all, delete")
