#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''base model class
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
