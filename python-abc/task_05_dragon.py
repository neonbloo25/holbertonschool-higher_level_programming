#!/usr/bin/python3
"""The ABCs of Python"""


class SwimMixin():
    """Class 1"""
    def swim(self):
        print("The creature swims!")

class FlyMixin():
    """Class 2"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Target Class"""
    def roar(self):
        print("The dragon roars!")
