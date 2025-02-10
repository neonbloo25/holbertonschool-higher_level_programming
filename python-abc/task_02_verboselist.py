#!/usr/bin/python3
"""The ABCs of Python ft. Abstract Method"""
__import__("sys")


class VerboseList(list):
    """Target Class"""

    def append(self, object):
        """func1"""
        print(f"Added [{object}] to the list.")
        return super().append(object)

    def extend(self, iterable):
        """func2"""
        print(f"Extended the list with [{len(iterable)}] items.")
        return super().extend(iterable)
    
    def remove(self, value):
        """func3"""
        print(f"Removed [{value}] from the list.")
        return super().remove(value)
    
    def pop(self, index=-1):
        """func4"""
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
 