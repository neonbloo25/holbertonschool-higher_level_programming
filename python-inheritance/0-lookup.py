#!/usr/bin/python3
"""
Write a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Function that returns list"""
    object = list(dir(obj))
    return object
