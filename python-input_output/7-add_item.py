#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""
import json
import os
saveJ = __import__('5-save_to_json_file').save_to_json_file
loadJ = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename="add_item.json", *args):
    """Target Function"""
    if os.path.exists(filename):
        items = loadJ(filename)
    else:
        items = []

    items.extend(args)
    saveJ(filename, items)

    """
    -Old Code-
    items = loadJ(filename)
    items.append(args.items())
    saveJ(filename, items)
    """
