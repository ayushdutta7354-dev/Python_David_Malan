# OOP:

def main():
    # name = get_name();
    # house = get_house();
    # aliter
    # name, house = get_student();
    # aliter:
    student = get_student();
    student_info = get_student_2();
    # below 2 lines are to show that tuple is immutable:
    # if student[0] == "ayush":
    #     student[1] = "house 3";
    if student[0] == "ayush":
        student[1] = "house 3";
    print(f"{student[0]} from {student[1]}");
    print(f"{student_info['name']} from {student_info['house']}");


def get_name():
    name = input("Enter name: ");
    return name;

def get_house():
    house = input("Enter house: ");
    return house;


# aliter above:

def get_student():
    name = input("Enter name: ");
    house = input("Enter house: ");
    # return name,house;
    # return (name,house);#tuple: comma separated value like list but immutable.
    return [name,house];


# aliter of get_student:

def get_student_2():
    student = {};
    student["name"] = input("Enter name: ");
    student["house"] = input("Enter house: ");
    return student;

if __name__ == "__main__":
    main();



