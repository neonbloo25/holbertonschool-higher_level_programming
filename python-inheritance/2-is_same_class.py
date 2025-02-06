#!/usr/bin/python3
"""Function verifies if type matches"""


def is_same_class(obj, a_class):
    """Target Function
    Returns: True/False"""
    if isinstance(obj, a_class) or type(obj) == type(a_class):
        return True
    else:
        return False
