#!/usr/bin/python3
"""Function verifies if x inherits in/directly from y class"""


def inherits_from(obj, a_class):
    """Target Function

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        True: if inherits from y
        False: if otherwise
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
