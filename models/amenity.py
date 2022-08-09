#!/usr/bin/python3
"""
Amenity class: Public class attributes:name: string - empty string.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute:
        name: (str)
    """
    name = ""
