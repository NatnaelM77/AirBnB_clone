#!/usr/bin/python3

"""
module BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns printable string representation"""
        str = f'[self.__class__.__name__] ({self.id}) {self.__dict__}'
        return str

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance."""
        dct = self.__dict__.copy()
        dct.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        })
        return dct
