#!/usr/bin/python3
"""Test Model for BaseModel Class"""

import unittest
from models.base_model import BaseModel
from models import base_model
from models import storage
import uuid
import os


class test_BaseModel(unittest.TestCase):
    """test for BaseModel """

    def test_str(self):
        """test for __str__ method"""
        b = BaseModel()
        printb = b.__str__()
        self.assertEqual(printb, "[BaseModel] ({}) {}".format(b.id,
                         b.__dict__))

    def test_save(self):
        """Test for save method"""
        obj = BaseModel()
        obj.save()
        key = "BaseModel.{}".format(obj.id)
        comp = storage._FileStorage__objects[key]
        self.assertEqual(obj.id, comp.id)
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict(self):
        """Test for to_dict method"""
        obj = BaseModel()
        keys = ['__class__', 'id', 'created_at', 'updated_at']
        test_dict = obj.to_dict()
        self.assertCountEqual(keys, test_dict)
