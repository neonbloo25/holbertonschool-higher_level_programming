#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""
import json


def load_from_json_file(filename):
    """Target Function"""
    with open(filename, 'r') as file:
        return json.load(file)
