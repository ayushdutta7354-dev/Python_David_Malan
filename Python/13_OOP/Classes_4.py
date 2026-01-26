# classes contd:

class Student:
    def __init__(self, name, house):
        self.name = name;
        self.house  = house;
        #self is a parameter which is equal to the instance of clsses(objectes created)


def main():
    student = get_student();
    print(f"Name: {student['name']}, {student.house}")


def get_student():
    name = input("enter name: ");
    house = input("enter house: ");
    # student = Student(name, house);
    return Student(name, house);


if __name__ == "__main__":
    main();