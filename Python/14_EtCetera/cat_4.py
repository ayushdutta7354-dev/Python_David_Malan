# Constants in python:

# 1.
MEOWS = 3;

# 2.
MEOWS = 4;

for _ in range(MEOWS):
    print("MEOW");


# aliter:

class Cat:
    MEOW = 3;

    def meow(self):
        for _ in range(Cat.MEOW):
            print("meow");  

def main():
    cat = Cat();
    print(cat.meow);


if __name__ == "__main__":
    main();