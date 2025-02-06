#!/usr/bin/python3
"""Create a class, empty"""


class BaseGeometry:
    """target class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """target function"""
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
