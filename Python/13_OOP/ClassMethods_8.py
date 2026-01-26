# Class Methods:

"""
Docstring for ClassMethods_8

🧠 What is @classmethod in Python?

A class method is a method that:

belongs to the class itself

NOT to a specific object (instance)

"""

import random;

class Hat:
    def __init__(self):
        self.houses = ["house 1", "house 2", "house 3", "house 4", "house 5"];

    def sort(self, name):
        print(name, "is in ", random.choice(self.houses));


hat = Hat();

hat.sort("Ayush");

# nex lec