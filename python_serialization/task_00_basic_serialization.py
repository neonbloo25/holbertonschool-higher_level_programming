#!/usr/bin/env python3
"""Let's get serial ft. Json"""
import json


def serialize_and_save_to_file(data, filename):
    """Func Save"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """Func Load"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
