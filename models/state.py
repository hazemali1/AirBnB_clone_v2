#!/usr/bin/python3
"""
Module with class State
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """
    State
    """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    cities = relationship("City", backref="State", cascade="all, delete")
    
    def cities(self):
        """
        list of city
        """
        from models import storage
        l = []
        for k, v in storage.all(City).items():
            if v.state_id == self.id:
                l.append(v)
        return l
        