#!/usr/bin/python3
"""Class that contains a private attribute"""


class Square():
    """
    class Square():
        This is the class for the current task, a progress from the last one

        Attributes:
            size: a private attribute intentionally left empty

    pass
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):  # Check if size is not an integer
            raise TypeError("size must be an integer")
        if size < 0:  # Check if size is less than 0
            raise ValueError("size must be >= 0")
    pass
