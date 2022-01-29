#!/usr/bin/python3

"""
module FileStorage
"""

import os
import json


class FileStorage:
    """Class FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            cls_name = obj.__class__.__name__
            obj_id = obj.id
            self.__objects.update({
                obj: f'{cls_name}.{obj_id}'
            })

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            pass

    def reload(self):
        """Deserialize the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                pass
