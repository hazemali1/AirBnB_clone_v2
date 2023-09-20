#!/usr/bin/python3
"""
Module with class User
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    class User that inherits from BaseModel
    """
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    __tablename__ = "users"
    places = relationship("Place", backref="User", cascade="all, delete")
