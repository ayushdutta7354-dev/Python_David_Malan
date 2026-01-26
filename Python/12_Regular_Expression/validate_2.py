# regex contd.

import re;

email = input("Enter your email: ").strip();

if re.search("@",email):
    print("valid email");
else:
    print("invalid");


# printing patterns in reg ex:


if re.search(".*@.*", email):
    print("valid");
else:
    print("invalid")



# in above we have .*@.* therefore even if we write ayush@, email valid.



if re.search(".+@.+", email):
    print("valid");
else:
    print("invalid")

# how to create above notion using *:

if re.search("..*@..*", email):
    print("valid");
else:
    print("invalid");

# creating more conditions pattern:

# in below if i write that, regex thinks that edu is the separator on whose lhs and rhs pattern is there
"""
if re.search(".+@.+.edu", email):
    print("valid");
else:
    print("invalid");
"""

if re.search(r".+@.+\.edu", email):
    print("valid");
else:
    print("invalid");

# in normal python, \ is escape character.so we use r"pattern" before pattern which means raw string. --> r"\n" means 2 characters bcz in regex we will use a lot of \.

if re.search(r"^.+@.+\.edu$", email):
    print("valid");
else:
    print("invalid");


# what if i write ayush@@@@@dutta.edu --> o/p is still valid. therefore we have []: which means set of characters and [^char]: means any character except char.

print("--------------------------------------------");

if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("valid");
else:
    print("invalid");



# what if user adds .edu at beginning of str: --> valid. so to exclude .edu at beginning, we write below:

print("------------------------");

if re.search(r"^[^@][^\.edu]+@[^@]+\.edu$",email):
    print("valid");
else:
    print("invalid");

# to include a range of char:

print("-----------------------------------------------");

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
    print("valid");
else:
    print("invalid");

# aliter: \w any alphanumeric char and _

if re.search(r"^\w+@\w+\.edu$",email):
    print("valid");
else:
    print("invalid");

"""
\d decimal digit, \D no decimal digit
\s whitespace, \S no whitespace
\w any alphanumeric char and _, \W no alphanumerica char and _
"""

# using or operator in above pattern

print("----------------------------------------------")

if re.search(r"^(\w|\s)+@(\w|\s)+\.edu$",email):
    print("valid");
else:
    print("invalid");

# if  i write AYUSH@DUTTA.EDU -->invalid, bcz .edu is in uppercase. to resolve this.

print("-------------------");

if re.search(r"^\w+@\w+\.edu$",email.lower()):
    print("valid");
else:
    print("invalid");

# flags in regex: we structure our  regex with flags like .IGNORECASE, .DOTALL.

if re.search(r"^\w.+@\w.+\.edu$",email, re.IGNORECASE):
    print("valid");
else:
    print("invalid");


# if we input ayush@dutta.something.edu --> invalid, to resolve: ?--> 0 repition or 1

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
    print("valid");
else:
    print("invalid");
