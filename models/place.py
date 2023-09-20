#!/usr/bin/python3
"""
Module with class Place
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
    Place
    """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    __tablename__ = "places"
    reviews = relationship("Reviews", backref="Place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, backref="place_amenity")
    
    def reviews(self):
        from models import storage
        l = []
        for k, v in storage.all().items():
            if v.place_id == self.id:
                l.append(v)
        return l
    
    @property
    def amenities(self):
        """getter"""
        from models import storage
        l = []
        for k, v in storage.all().items():
            if v.place_id == self.id:
                l.append(v)
        return l
    
    @amenities.setter
    def amenities(self, value):
        """setter"""
        if type(value) is Amenity and value.id not in self.amenity_ids:
            self.amenity_ids.append(value.id)
