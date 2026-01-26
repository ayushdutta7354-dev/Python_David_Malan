# Unpacking in python: we hacve seen this b4.  but now more powerfully.

first, last = input("name: ").split(" ");

print(f"hello, {first}");

# now moving fwd:

def total(galleons, sickles, knuts):
    return (galleons*19+sickles) * 28 + knuts;

coins = [100,25,75];
print(total(coins[0], coins[1], coins[2]), "knuts");

# note: i cant write total(coins), bcz coins is list. here comes unpacking:

print(total(*coins), "knuts");

# we cant pass list of len -gt 3 --> shows error:

if len(coins) > 3:
    print("invalid input");
else:
    print(total(*coins), "knuts");

# aliter:

print(total(galleons=100, sickles=45, knuts=25), "knuts");

# note: we cant use unpacking on set.

# unpack dictionary:

print("-------------");
coins_1 = {"galleons":100, "sickles": 25, "knuts":75};

print(total(coins_1["galleons"], coins_1["sickles"], coins_1["knuts"]), "knuts");

# or

print(total(**coins_1), "knuts");

# New topic:

def f(*args, **kwargs):
    print("Positional Args: ", args);
    print("Named Args: ", kwargs);

f(100,50,25);
f();
f(100);

f(1, galleons=100, sickles=50, knuts=25);

# we have don above since long time:

# print(*object, sep=" ", end="\n", ...);

# bcz of above we could do this:

print("hello", "world");