#!/usr/bin/python3
""" this module creates a type class BaseModel """
import uuid
from datetime import datetime


class BaseModel:
    """ Defines a base model for other classes of its same type

    Args:
    *arg: I don't receive anything as parameter
    **kwargs: receives a dictionary as parameter

    Attributes:
    id(str): Generates a unique id for the objects that will be created
             from this class
    created_at: Saves the creation time of the object
    updated_at: Saves the update time of the object
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """This is a function what represents the
        class objects as a string
        """
        return ("[{0}] ({1}) {2}".format(BaseModel.__name__,
                                         self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute
        'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """this function returns a dictionary with the attributes of instance,
        class, a key __class__ with BaseModel value is added and
        the time is converted to iso format
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = BaseModel.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return (new_dict)
