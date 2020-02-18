#!/usr/bin/python3
'''
Base model
'''
import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}" \
        .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
