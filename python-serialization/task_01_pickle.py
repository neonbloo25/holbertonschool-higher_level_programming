#!/usr/bin/env python3
"""Let's get serial ft.pickle"""
import pickle


class CustomObject:
    """Target Class"""

    def __init__(self, name, age, is_student):
        """Instance Func"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Func Display"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Func Serialize"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, IOError) as e:
            print(f"Error saving file: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Func deSerialize w/ Try/Except"""
        try:
            with open(filename, 'rb') as file:
                if file.read(1):  # Verifica si el archivo tiene contenido
                    file.seek(0)  # Regresa al inicio para leer con pickle
                    return pickle.load(file)
                else:
                    print(f"Error: The file '{filename}' is empty.")
                    return None
        except (OSError, IOError, pickle.PickleError, EOFError) as e:
            print(f"Error loading file '{filename}': {e}")
            return None
