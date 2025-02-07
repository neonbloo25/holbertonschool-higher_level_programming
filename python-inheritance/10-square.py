#!/usr/bin/python3
"""Create a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Target Class(Inheriting)"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
