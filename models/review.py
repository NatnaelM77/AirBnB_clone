#!/usr/bin/python3

"""
contain state class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ''
    user_id = ''
    text = ''
