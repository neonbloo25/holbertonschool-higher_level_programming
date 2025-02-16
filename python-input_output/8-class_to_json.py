#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""


def class_to_json(obj):
    """Target Class, with each type case"""

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
