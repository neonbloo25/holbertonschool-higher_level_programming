#!/usr/bin/python3
"""Class Inheritance Task"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Target Class"""

    def __init__(self, size):
        """target function"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
