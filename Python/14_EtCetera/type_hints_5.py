# Tyoe hints in python: mention datatype in python

def meow(n:int) -> str: #this is called type hint, returns str
    # for _ in range(n):
    #     print("meow");
    return "meow\n" * n;

number: int = int(input("number: "));

meows: str = meow(number);#error even with mypy, but mypy is only for our use as developer.

print(meows);

# in terminal write: mypy type_hints_5.py --show-error-codes

# docstring tomorrow.