import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)
    
    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                file_content = file.read()
                print(file_content)
                if file_content:
                    self.__objects = json.loads(file_content)
                    for key, value in self.__objects.items():
                        class_name , obj_id = key.split('.')
                        self.__objects[key] = globals()[class_name](**value)
                else:
                    self.__objects = {}
        except FileNotFoundError:
            pass