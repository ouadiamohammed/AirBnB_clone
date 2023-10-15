#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns all stored BaseModel objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds new object"""
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes FileStroage.__objects
        """
        with open(FileStorage.__file_path, 'w+') as f:
            dictofobjs = {}
            for key, value in FileStorage.__objects.items():
                dictofobjs[key] = value.to_dict()
            json.dump(dictofobjs, f)

    def reload(self):
        """
        deserializes instances got from json file
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dictofobjs = json.loads(f.read())
                for key, value in dictofobjs.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                        
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
                        
                    elif value['__class__'] == 'Place':
                        FileStorage.__objects[key] = Place(**value)
                    
                    elif value['__class__'] == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)

                    elif value['__class__'] == 'City':
                        FileStorage.__objects[key] = City(**value)
                        
                    elif value['__class__'] == 'Review':
                        FileStorage.__objects[key] = User(**value)
                        
                    elif value['__class__'] == 'State':
                        FileStorage.__objects[key] = State(**value)

        except FileNotFoundError:
            pass
