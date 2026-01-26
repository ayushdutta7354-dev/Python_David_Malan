# operators in python:

"""
we can enter into python repl by typing 'python' or 'python3' in terminal.

Operators are special symbols that carry out arithmetic or logical computation.

"""

x = input("Enter first number: ");
y = input("Enter second number: ");

z = int(x) + int(y);

print("The sum is: ", z);

# aliter of above code:

p = int(input("Enter first number: "));
q = int(input("Enter second number: "));



print("Sum is: ", p + q);# here, int() function converts the input string into integer.

"""
Dataypes in python:
1. int - integer numbers
2. float - decimal numbers
3. str - string or sequence of characters
4. bool - boolean values True or False
5. list - ordered and mutable collection of items
6. tuple - ordered and immutable collection of items
6. dict - collection of key-value pairs
7. set - unordered collection of unique items
8. NoneType - represents the absence of a value


# Operators:
1. Arithmetic operators: +, -, *, /, %, //, **
"""

# let's create above code with float numbers:

a = float(input("Enter first number: "));
b = float(input("Enter second number: "));

print("Sum is: ", a + b);

# rounding off the float result to 2 decimal places:

num1 = float(input("Enter first number: "));
num2=float(input("Enter second number: "));

sum = round(num1+num2);

print("Sum is: ", sum);

print(f"{sum:,}");# adding comma as thousand separator

# division operator / always returns float result:


n1 = float(input("Enter first number for div: "));
n2 = float(input("Enter second number for div: "));
div = round(n1/n2, 3);# rounding off to 3 decimal places

print(div);