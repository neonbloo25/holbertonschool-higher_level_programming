#!/usr/bin/python3
"""The ABCs of Python"""


class SwimMixin():
    """Class 1"""
    pass

class FlyMixin():
    """Class 2"""
    pass

class Dragon(SwimMixin, FlyMixin):
    """Target Class"""
    pass
