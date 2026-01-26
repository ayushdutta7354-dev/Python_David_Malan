# Classes in Python:

"""
Docstring for Classes_3

🧠 What is a Class in Python?

A class is a blueprint for creating objects.

Think of it like this:

Class → design / template

Object → real thing made from the template

Example in real life:

Class: Car

Objects: your car, my car, a taxi, a bus

All cars have:

color

brand

speed

But each car’s values are different.
"""

# class Student:
#     ... #this means do nothing for now
    
class Student:
    def __init__(name, house):
        pass



def main():
    student = get_student();
    print(f"Student name: {student['name']}, student favorite subject is {student['favsubject']}")

def get_student():
    student = Student();
    student['name'] = input("Enter name");
    student['house'] = input("Enter your house: ");
    return student;


if __name__ == "__main__":
    main();