# Conditionals in python:

"""
comparator operators in python:
>
<
>=
<=
!=
"""

x = int(input("what's x? "));
y = int(input("What's y? "));

if x<y:
    print(f"{y} is greater than {x}");
if y<x:
    print(f"{x} is greater than {y}");
if x==y:
    print(f"{x} is equals to {y}");

# Aliter of above:

print("---------NEW LINE------------")

if x>y:
    print("x is greater than y");
elif x==y:
    print("x is equal to y");
else:
    print("x is less than y");

# Aliter:
print("--------------------------------------");
if x>y or x<y:
    print("x is not equal y");
else:
    print("x is equal y");

# Aliter:
print("--------------------------------------");

if x!=y:
    print("x is not equal y");
else:
    print("x equal y");

# Assignment:

score = int(input("Score: "));

if score >= 90 and score <= 100:
    print("Grade: A");
elif score>=80 and score<90:
    print("Grade: B");
elif score >=70 and score<80:
    print("Grade: C");
elif score >=60 and score >70:
    print("Grade: D");
elif score >=50 and score<60:
    print("Grade: E");
else:
    print("Grade: F");

# if we remove range and elif: all staements executed

if score>=90:
    print("Grade: A");

if score>=80:
    print("Grade: B");
if score>=70:
    print("Grade: C");
if score >=60:
    print("Grade: D");
if score >= 50:
    print("Grade: E");

# Q. determine if a number is even or odd:

num = int(input("Enter number: "));

if num%2==0:
    print("Even");
else:
    print("Odd");

def main():
    u = int(input("Enter the number u: "));
    if isEven(u):
        print("Even");
    else:
        print("Odd");

def isEven(n):
    # return True if n%2==0 else false;
    return n%2==0; #this returns boolean

main();

# In Python everything is a Object: LATER

# Match statements(Switch) in python:

name = input("Enter name: ");

if name == "Hermione" or name == "harry" or name == "Ron":
    print("Sylvinddor");
else:
    print("who?");

print("------------------------------------");
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor");
    case "Draco":
        print("Sylvinter");
    case _:
        print("Who? ");


