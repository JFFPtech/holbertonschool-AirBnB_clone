import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        all_objects = {}
        for key, value in FileStorage.__objects.items():
            all_objects[key] = value
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        if class_name == "BaseModel":
                            from models.base_model import BaseModel
                            obj = BaseModel(**value)
                        else:
                            raise ValueError("Class name not found")
                        FileStorage.__objects[key] = obj
                except json.JSONDecodeError:
                    print("** class does not exist **")
        except FileNotFoundError:
            pass
