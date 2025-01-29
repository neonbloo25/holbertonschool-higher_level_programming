#!/usr/bin/python3
"""Class that contains a private attribute"""


class Square():
    """
    class Square():
        This is the class for the current task, a progress from the last one

    Methods:
    __init__(self, size): The Square class' main function.
    area(self): Obtains the Area of Size.

    pass
    """

    def __init__(self, size=0):
        """Square class' main function

        Args:
            size (int): private attribute. Defaults to 0.

        Raises:
            TypeError: case 1 - wrong type
            ValueError: case 2 - incorrect value
        """

        """Private Class Attribute"""
        self.__size = size
        """Type Error"""
        if not isinstance(size, int):  # Check if size is not an integer
            raise TypeError("size must be an integer")
        """Value Error"""
        if size < 0:  # Check if size is less than 0
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    pass
