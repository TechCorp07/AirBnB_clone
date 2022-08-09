#!/usr/bin/python3
"""
City class:state_id: string - empty string: it will be the State.id
name: string - empty string
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
    state_id: (str) will be State.id
    name:     (str)
    """
    state_id = ""
    name = ""
