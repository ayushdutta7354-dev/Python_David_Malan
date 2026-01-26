#Modules: sys.argv: What is sys.argv?

"""
sys.argv is a list in Python that contains the command-line arguments passed to a Python script.

sys is a built-in module.

argv stands for Argument Vector.

In simple terms:

sys.argv gives your Python program access to values the user types when running the script from the terminal.
"""
import sys;

# print("hello, my name is", sys.argv[1]); #at index 0, sys.srgv stores the name of the file we are coding.

print(sys.argv);# list we get.
print(sys.argv[0]);

# if dont write anything after file name, we get index error. to avoid that:

try:
    print("Hello my name is ", sys.argv[1]);
except IndexError:
    print("Too few arguments");

# aliter above:

if(len(sys.argv)<2):
    print("too few args");
elif(len(sys.argv)>2):
    print("too many args");

# print("hello my nam eis ", sys.argv[1]);#its bug, bcz this line exevute anywas.

# Aliter:

# if(len(sys.argv)<2):
#     sys.exit("Too few args");
# elif(len(sys.argv)>2):
#     sys.exit("Too many args");

# print("hello my name ", sys.argv[1]);

# aliter:

if(len(sys.argv)<2):
    print("too few args");
elif(len(sys.argv)>2):
    print("too many args");
else:
    print("hello my nam eis ", sys.argv[1]);

# for creating multiple name tag:

for arg in sys.argv[1:]: #we sliced so that nobody.
    print("hello,", arg);






