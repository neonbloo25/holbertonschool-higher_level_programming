#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""
import json
saveJ = __import__('5-save_to_json_file').save_to_json_file
loadJ = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename="", **args):
    """Target Function"""
    items = loadJ(filename)
    items.append(args)
    saveJ(filename, items)
