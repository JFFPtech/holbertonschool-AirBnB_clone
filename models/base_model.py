import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid.uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
