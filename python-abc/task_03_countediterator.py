#!/usr/bin/python3
"""The ABCs of Python"""


class CountedIterator:
    """Key Class"""
    def __init__(self, data):
        """func1"""
        self.data = iter(data)
        self.counter = 0

    def get_count(self):
        """
        func2
        returns count
        """
        return self.counter

    def __next__(self):
        """
        func3
        override __next__
        """
        try:
            item = next(self.data)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
