#!/usr/bin/python3
"""This module contains the BaseModel class for the AirBnB clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for AirBnB clone"""
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    dataTime = "%Y-%m-%dT%H:%M:%S.%f"
                    v = datetime.strptime(v, dataTime)
                if k != "__class__":
                    setattr(self, k, v)

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
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        formatTime = "%Y-%m-%dT%H:%M:%S.%f"
        obj_dict['created_at'] = self.created_at.strftime(formatTime)
        obj_dict['updated_at'] = self.updated_at.strftime(formatTime)
        return obj_dict