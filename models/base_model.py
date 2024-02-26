import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models in the AirBnB clone project.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        Sets the id, created_at, and updated_at attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.
        Adds the '__class__', 'created_at', and 'updated_at' keys.
        Returns the dictionary representation of the BaseModel instance.
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = type(self).__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
