#!/usr/bin/python3
"""This module stores a file"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """This class represents a file storage system
    for objects in the AirBnB clone project."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary"""
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes and saves the objects in the __objects
        dictionary to a JSON file"""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            if value:
                serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes and reloads the objects from the JSON file"""
        my_dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Place': Place, 'Review': Review,
                   'Amenity': Amenity}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                deserialized_objects = json.load(file)
            for key, value in deserialized_objects.items():
                FileStorage.__objects[key] = my_dict[value['__class__']](**value)
