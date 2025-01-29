#!/usr/bin/python3
"""Class that contains a private attribute"""


class Square():
    """
    class Square():
        This is the class for the current task, a progress from the last one
    """

    def __init__(self, size=0):
        """Square class' main function"""
        self.__size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
