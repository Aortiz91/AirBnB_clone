#!/usr/bin/python3
""" Base Model"""

from uuid import uuid4
from datetime import datetime
import models
from cmd import Cmd

class BaseModel:
    """ class"""
    def __init__(self):

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ returns the printable of [ class name], (self.id) and self.__dict"""
        return ("[{}] ({}) {}".format(self.class.__name__, self.id, self.__dict__)

    def save(self):
        """updates datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary with kew/value of dict"""
        newDict = self._dict__.copy()
        newDict["__Class__"] = self.__class__.__name__
        newDict["created_at"] = newDict["created_at"].isoformat()
        newDict["updated_at"] = newDict["updated_at"].isoformat()
        return newDict