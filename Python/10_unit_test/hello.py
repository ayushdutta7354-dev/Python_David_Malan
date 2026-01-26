def main():
    name = input("Enter name: ");
    if name.strip() == "":
        print(hello());
    else:
        print(hello(name));

def hello(to="World"):
    return f"hello, {to}";


if __name__ == "__main__":
    main();