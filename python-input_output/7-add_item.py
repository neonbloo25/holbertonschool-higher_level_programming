#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""
import os
import sys
saveJ = __import__('5-save_to_json_file').save_to_json_file
loadJ = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """Target Function"""
    filename = "add_item.json"
    if os.path.exists(filename):
        items = loadJ(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    saveJ(filename, items)
