# format user input using regex:

# initialy:

name = input("Enter your name: ").strip();

if "," in name:
    first, last = name.split(",");
    name = f"{last} {first}";
    print(f"hello, {name}");

# by regex:

print("----------------------------");

import re;

matches = re.search(r"^(.+), *(.+)$", name);

# first, last = matches.group();
# or

# first = matches.group(2);
# last = matches.group(1);

# or := volaris operator: if and only if

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1);
print(f"hello, {name}");


