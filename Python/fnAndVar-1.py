# Introduction:

print("Hello, World!");

'''
print is a function: function is a piece of code that perfoms a task and can be reused whenever called.

what ever we pass inside () parentheses are arguments or fn input
'''

# another function:

# ask user for the input
name = input("Hi, what's your name?\n");

# say hello to input
print("Hello, ", end=""); #end doesnt add a new line after print
print(name); 

# aliter:

print("Hello, " + name); # string concatenation
# + operator joins two strings


# Aliter
'''
# f-string or formatted string literals
# f-string allows embedding expressions inside string literals, using curly braces {}
'''
print(f"Hello, {name}"); 


# .strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).

name = name.strip();
print(f"Hello, {name}");

# .capitalize() method returns a copy of the string with its first character capitalized and the rest lowercased.

name = name.capitalize();

print(f"Hello, {name}");

# .title() method returns a copy of the string where the first character of each word is capitalized.

name = name.title();
print(f"Hello, {name}");

# chaining methods: name.strip().title()....and so on
name = name.strip().title();
print(f"Hello, {name}");

# putting everything on the first line itself:
name = input("Hi, what's your name?\n").strip().title();
print(f"Hello, {name}");

# .split() method splits a string into a list where each word is a list item. The default separator is any whitespace.

first, last = name.split(" "); # unpacking the list into two variables first and last

print(f"Hello, {first}");
