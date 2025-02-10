#!/usr/bin/python3
"""The ABCs of Python ft. Abstract Method"""
__import__("sys")


class VerboseList(list):
    """Target Class"""

    def append(self, object):
        pass

    def extend(self, iterable):
        pass

    def remove(self, value):
        pass

    def pop(self, index):
        pass
