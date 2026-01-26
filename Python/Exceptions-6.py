# Exceptions:

# 1. SYNTAX ERROR:

# print(hello"); // throws syntax error


# 2. Value Error: something is wrong in below: if we write a word like lion, value error is o/p

x = int(input("Wnats x: "));
print(f"x is {x}");

# for error handling we have try-except:

# try:
#     y = int(input("Whats y: "));
#     print(f"y is {y}");
# except ValueError:
#     print("y is not an integer");

# print(f"y is {y}");
# above throws error if we dont write an integer. error is name error, also we get value error. how we get both error? so when we input str, y is unable to covert to int, to value error, but at the same time print(f"y is {y}"); is on line 21 executes anyway, hence y was actually never created wrt line 16, so name error. Soln to above:

try:
    y = int(input("Whats y: "));
except ValueError:
    print("y is not an integer");
else:
    print(f"y is {y}");

# lets improve above code with loops:

while True:
    try:
        z = int(input("Whats z: "));
        break;#aliter of line 40.
    except ValueError:
        print("z is not an integer");
    # else:
    #     break;

print(f"z is {z}");

# lets put above in a fn:

def main():
    b = get_int("Whats number: ");
    print(f"b is {b}");

def get_int(prompt):
    while True:
        try:
            return int(input(prompt));
            # return a;
        except ValueError:
            # print("a is not integer");
        # else:
        #     return a;
            pass;

main();