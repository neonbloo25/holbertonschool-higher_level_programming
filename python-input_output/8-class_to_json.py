#!/usr/bin/python3
"""I/O Week! tf. Json(ree! ree! ree!)"""


def class_to_json(obj):
    """Target Class"""
    if isinstance(obj, list):
        return {
            'type': 'list',
            'length': len(obj),
            'elements': [class_to_json(item) for item in obj]
        }
    elif isinstance(obj, dict):
        return {
            'type': 'dict',
            'length': len(obj),
            'keys': len(obj.keys()),
            'values': [class_to_json(value) for value in obj.values()]
        }
    elif isinstance(obj, str):
        return {
            'type': 'string',
            'length': len(obj),
            'value': obj
        }
    elif isinstance(obj, int):
        return {
            'type': 'int',
            'value': obj
        }
    elif isinstance(obj, bool):
        return {
            'type': 'boolean',
            'value': obj
        }
    else:
        return {
            'type': 'unknown',
            'value': obj
        }

