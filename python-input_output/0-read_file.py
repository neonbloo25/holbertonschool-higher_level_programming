#!/usr/bin/python3
"""Input/Output week!"""


def read_file(filename=""):
    """Target function"""
    with open(filename, encoding='utf-8') as file:
        content = file.read()
    print(content)
