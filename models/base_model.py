#!/usr/bin/python3
"""
AirBnB project class of base model
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ constructor of class model """
        if kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = kwargs["created_at"]
                elif key == "updated_at":
                    self.__dict__["updated_at"] = kwargs["updated_at"]
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ str function """
        return "[{}] ({}) {}". \
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ save update datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ new dict """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
