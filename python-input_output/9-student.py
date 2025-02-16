#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Target Function"""
        return class_to_json(self)


def class_to_json(obj):
    """direct insert from last task"""
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]

    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}

    elif isinstance(obj, str):
        return obj

    elif isinstance(obj, int):
        return obj

    elif isinstance(obj, bool):
        return obj

    elif hasattr(obj, "__dict__"):  # Handling custom class instances
        return {key: class_to_json(value) for key, value in vars(obj).items()}

    else:
        """If nothing matches type"""
        return obj
