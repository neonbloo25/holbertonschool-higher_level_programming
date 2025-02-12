#!/usr/bin/python3
"""Input/Output week!"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='UTF8') as file:
        content = file.read()
    print(content)
