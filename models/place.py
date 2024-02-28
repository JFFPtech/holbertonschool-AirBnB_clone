#!/usr/bin/python3
"""Module for place"""

from models.base_model import BaseModel
from datetime import datetime
import models

class Place(BaseModel):
    """Place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Place constructor"""
        super().__init__(*args, **kwargs)
        models.storage.new(self)

    def __str__(self):
        """Place string representation"""
        return "[Place] ({}) {}".format(self.id, self.__dict__)
    
    def save(self):
        """Save method"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """To dict method"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict