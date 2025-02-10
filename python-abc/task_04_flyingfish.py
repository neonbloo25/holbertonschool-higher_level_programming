#!/usr/bin/python3
"""The ABCs of Python"""


class Fish:
    """Base Class 1"""
    pass

class Bird:
    """Base Class 2"""
    pass

class FlyingFish(Fish, Bird):
    """Target Class"""
    pass
