import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """Returns a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict