#!/usr/bin/python3
"""This module contains the BaseModel class for the AirBnB clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for AirBnB clone"""
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the
        current datetime and saves the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
            A dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
