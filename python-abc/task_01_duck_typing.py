#!/usr/bin/python3
"""The ABCs of Python ft. Abstract Method"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Target Base Class"""
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Target Class 1"""
    def __init__(self, radius=0):
        if type(radius) in [int, float]:
            self.radius = abs(radius)
    
    def area(self):
        return (pi * (self.radius ** 2))
    
    def perimeter(self):
        return (2 * pi * self.radius)


class Rectangle(Shape):
    """Target Class 2"""
    def __init__(self, width=0, height=0):
        if type(width) in [int, float]:
            self.width = width

        if type(height) in [int, float]:
            self.height = height
        
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return (2 * self.height) + (2 * self.width)

def shape_info(shape):
    """Prints the information of a shape"""
    
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
