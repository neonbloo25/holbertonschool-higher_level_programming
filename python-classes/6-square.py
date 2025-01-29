#!/usr/bin/python3
"""Class that contains two private attributes"""


class Square():
    """
    class Square():
        This is the class for the final task,
        the culmination from all previous tasks and a bit more
    """

    def __init__(self, size=0, position=(0, 0)):
        """Square class' main function"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Now we work with position"""
        while 1:
            if type(value) is not tuple or len(value) is not 2:
                check += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
                break
        if check is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
