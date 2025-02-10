#!/usr/bin/python3
"""The ABCs of Python"""


class Fish:
    """Base Class 1"""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """Base Class 2"""
    def fly(self):
        print("the bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Target Class"""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
