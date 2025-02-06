#!/usr/bin/python3
"""Function verifies if type matches"""


def is_same_class(obj, a_class):
    """Target Function
    Returns: True/False"""
    if type(obj) is a_class:
        return True
    else:
        return False
