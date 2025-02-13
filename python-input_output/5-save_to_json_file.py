#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""
import json


def save_to_json_file(my_obj, filename):
    """Target Function"""
    if isinstance(my_obj, set):
        my_obj = list(my_obj)

    """try/except block running two excepts"""
    try:
        """The go-to option"""
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
    except PermissionError as e:
        """in case of Permissions issue"""
        print(f"[{e.__class__.__name__}] {e}")
    except TypeError as e:
        """in case of type error"""
        print(f"[{e.__class__.__name__}] {e}")
