# Generators in python:

def main():
    n = int(input("Enter n: "));
    print(sheep(n));

    for s in sheep_1(n):
        print(s);

    for s in sheep_3(n):
        print(s);



def sheep(n):
    return "😊" * n;

def sheep_1(n):
    flock = [];
    for i in range(n):
        flock.append("😊"*i);
    return flock;

# but above line returns flock list all at once, so if the i/p is tooo large, returning data all at once will kill the program. aliter:

def sheep_3(n):
    for i in range(n):
        yield "🎂" *i; #yield is generator object therefore we use for loop.


if __name__ == "__main__":
    main();
