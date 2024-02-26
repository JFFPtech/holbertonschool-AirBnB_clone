import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = type(self).__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj