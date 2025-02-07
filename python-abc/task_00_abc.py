#!/usr/bin/python3
"""The ABCs of Python ft. Abstract Method"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Target Base Class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Target Class 1"""

    def sound(self):
        print('Bark')


class Cat(Animal):
    """Target Class 2"""

    def sound(self):
        print('Meow')
