#!/usr/bin/python3
"""A class that inherits from a main class"""


class MyList(list):
    """Inheriting Class"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Target Function"""
        self.sort(reverse=False)


mylist = MyList()
mylist.print_sorted()
