#!/bin/usr/python3

"""
The engine that runs file storage, 
with various methods for JSON serialization
"""
import json
import importlib
from models.base_model import BaseModel


class FileStorage:
    """
    Start of FileStorage instance 
    """
    # Set filepath to file.json for data storage
    __file_path = 'file.json'
    # Empty dictionary to hold object IDs and objects
    # formatted as such: <classname>.<IDnumber>
    __objects = {}

    # Returns a dictionary of objects
    def all(self):
        """Returns dict objects"""
        return self.__objects

    # Saves new object into the dictionary
    # Key - [<classname>.id#]
    def new(self, obj):
        """Add new obj to dict"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Saves to existing instances"""
        with open(self.__class__.__file_path, "w") as file:
            # Serialize objects 
            objects = {key: val.to_dict() for
                    key, val in self.__objects.items()}
            # Write serialized obj to file
            json.dump(objects, file)
        

    def reload(self):
        """Load intance from save"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                # Loads obj from filei
                obj = json.load(file)
                for key in obj.keys():
                    # Extract class name
                    class_name = obj[key]["__class__"]
                    # Creates new instance of the class
                    new_obj = self.selectClass(class_name)(obj[key])
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            # Do nothing if file not found
            pass

    def selectClass(self, class_name):
        """Selects and returns the class from class_name"""
        module_name = f"models.{class_name}"
        # Generate the module name
        module = importlib.import_module(module_name)
        # Dynamically import the module
        return getattr(module, class_name)
        # Get the class from the module based on the class name
