#!/usr/bin/python3
"""This is module that create type class"""
import json
from models.base_model import BaseModel

class FileStorage():
    """This is a class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This is a metode that returns the dictionary"""
        return (self.__objects)

    def new(self, obj):
        """Add an object with its key to the dictionary"""
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update({key: value.to_dict()})
        with open(self.__file_path, "w") as file:
           file.write(json.dumps(new_dict))

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                contents = f.read()
                json.loads(contents)
        except:
            pass
