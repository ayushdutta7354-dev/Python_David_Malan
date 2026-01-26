# OOP: Continue


def main():
    student = get_student();
    # mutating dictionary:
    if student['name'] == "ayush":
        student['house'] = "house 3"; 
    print(f"{student['name']} from {student['house']}");


def get_student():
    name = input("Enter name: ");
    house = input("Enter house: ");
    return {"name": name, "house": house}; #we can return dictionary on the move.



if __name__ == "__main__":
    main();


# CLASSES in python: