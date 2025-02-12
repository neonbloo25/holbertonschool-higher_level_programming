#!/usr/bin/python3
"""Input/Output week!"""


def append_write(filename="", text=""):
    """Target function"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
