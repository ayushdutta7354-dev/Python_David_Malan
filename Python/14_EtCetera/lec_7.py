import sys;

# lets write meow program from earlier as follows:

if len(sys.argv) == 1:
    print("meow");
elif len(sys.argv) == 3:
    n = int(sys.argv[2]);
    print("meow\n"*n);
else:
    print("usage: meow.py");

# but to do above we aslo have argparse library in python.
