#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""
import json


def from_json_string(my_str):
    """Target Function"""
    my_str_back = json.loads(my_str)
    return my_str_back
