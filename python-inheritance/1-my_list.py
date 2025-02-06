#!/usr/bin/python3
"""A class that inherits from a main class"""


class MyList(list):
    """Inheriting Class"""

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        """Target Function"""
        print(sorted(self))
