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

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Makes squares"""
        if self.__size == 0:
            print("")
        for s in range(self.__size):
            for s in range(self.__size):
                print("#", end="")
            print()
        else:
            print()
