# Dictionary Compehension:

students = ["ayush", "ramesh", "suresh"]

houses = []

for student in students:
    houses.append({"name": student, "house": "house 3"})

print(houses)


# aliter:

houses_ = [{"name": s, "house": "house 3"} for s in students]

print(houses_)

# lets create a dictionary with above:

houses__ = {st: "house 3" for st in students}

print(houses__)

# play with list: range and enumerate:

print("-------------------------------------------")

for i in range(len(students)):
    print(i + 1, students[i])


# aliter:

print("---------------");

for i, stu in enumerate(students):
    print(i+1, students[i]);