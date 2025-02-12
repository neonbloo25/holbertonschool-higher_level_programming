#!/usr/bin/python3
"""Input/Output week!"""


def write_file(filename="", text=""):
    """Target function"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
