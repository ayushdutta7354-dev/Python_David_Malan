with open("Students_2.csv") as file:
    for line in file:
        row = line.rstrip().split(",");
        print(f"{row[0]} lives in {row[1]}");

# csv means comma separated value:

with open("Students_2.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",");
        print(f"{name} lives in {house}");


print("-------------------------------------------------------------");
students = [];
with open("Students_2.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",");
        student = {"name": name, "house":house};
        # student["name"] = name;
        # student["house"] = house;
        print(f"{student['name']} lives in {student['house']}");
        students.append(student);

print("-----------------------------------------------------------------");


# if we want sorted output with sorting on the basis of name:

def get_name(student_dictionary):
    return student_dictionary["name"];

for student in sorted(students, key=get_name):
    print(f"{student['name']} lives in {student['house']}");

# if we want sorted output with sorting on the basis of house:

print("------------------------------------------------------");

def get_house(student_dictionary):
    return student_dictionary["house"];

for student in sorted(students, key=get_house):
    print(f"{student['name']} lives in {student['house']}");

# aliter of above 2:

print("-------------------------------------------------------------------");


for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is in {student['house']}");

print("-------------------------------------------------------------------");

for student in sorted(students, key=lambda student: student['house']):
    print(f"{student['name']} is in {student['house']}");


# lambda is an anonymous fn: What is lambda in Python?

# A lambda is a way to create a small, anonymous (nameless) function in one line.

# Think of it as a mini-function you write quickly when you don’t want to define a full def function.


