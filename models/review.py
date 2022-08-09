#!/usr/bin/python3
"""
Review class:place_id: string - empty string: it will be the Place.id
user_id: string - empty string: will b the User.id,text: string - empty string
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:

    place_id:            (str) will be Place.id
    user_id:             (str) will be User.id
    text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""
