#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""


class Student:
    """Target Class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Still target function, altered functionality"""
        if attrs is None:
            return {key: value for key,
                    value in self.__dict__.items()}

        else:
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}
