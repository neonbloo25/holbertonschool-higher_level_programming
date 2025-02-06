#!/usr/bin/python3
"""Create a class, empty"""


class BaseGeometry:
    """target class"""

    def __init__(self, name="", value=0):
        self.name = name
        self.value = value

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """target function"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("name> must be greater than 0")
