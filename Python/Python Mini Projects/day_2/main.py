from sys import argv;

def main():
    greet_user();



def greet_user():
    for _ in argv[1:]:
        print("greetings, ", _);


if __name__ == "__main__":
    main();