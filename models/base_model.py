#!/usr/bin/python3
""" module for BaseModel class """

from uuid import uuid4
import models
from datetime import datetime
import engine.file_storage as storage


class BaseModel:
    """ class of the base model of higher-level data models """
    def __init__(self, *arg, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at.replace()
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary representation of the model """
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct

    def __str__(self):
        """ returns a string representation of the model """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
