# Functions in Python:

"""
Syntax:
def function_name(parameters):
    docstring
    statement(s)
    return [expression]
"""

def hello1():
    print("hello, ");


name = input("Enter your name: ");
hello1();
print(name);

# function with parameter:

def hello2(to):
    print("hello, ", to);

name = input("Enter your name: ");
hello2(name);

# function with default parameter:

def hello3(to="world"):
    print("hello, ", to);

name = input("Enter your name: ");
hello3(name);

hello3()


############################################################

def main():
    n = input("What's name? ");
    greet(n);


def greet(to):
    print("greetings, ", to);

main();

# creating error in above code:

"""
def main():
    n = input("name? ");
    hello();


def greet():
    print("greetings, ", n);

main();

error because n is defined in the scope of main(), not int he scope of greet fucntion

"""

################################################################

# Project: create your own function which squares an entered num.

def main():
    n = int(input("Enter n: "));
    print(f"square of n is {square(n)}");

def square(n):
    return n*n;

main();