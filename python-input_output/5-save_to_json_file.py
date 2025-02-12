#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""
import json


def save_to_json_file(my_obj, filename):
    """Target Function"""
    if isinstance(my_obj, set):
        my_obj = list(my_obj)

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
