class Student:
    def __init__(self, name, house):
        self.name = name;
        self.house = house;


def main():
    s1 = get_student();
    print(f"{s1.name} from {s1.house}");


def get_student():
    name = input("name: ");
    house = input("house: ");
    return Student(name, house);


if __name__ == "__main__":
    main();