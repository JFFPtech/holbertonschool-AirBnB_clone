#!/usr/bin/python3
""" User module """

import models
from models import base_model
from datetime import datetime

class User(base_model.BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")
        self.save()

    def __str__(self):
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