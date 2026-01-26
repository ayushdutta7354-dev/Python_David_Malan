# map contd:

students = [
    {"name": "ayush", "house": "house 3"},
    {"name": "ramesh", "house": "house 2"},
    {"name": "suresh", "house": "house 1"},
    {"name": "khushboo", "house": "house 3"},
    {"name": "akanksha", "house": "house 3"},
]

house_3 = [student["name"] for student in students if student["house"] == "house 3"]

print(house_3)

# aliter:

# FILTER in Pyhton:


def is_house3(s):
    return s["house"] == "house 3"


house3 = filter(is_house3, students)

print(house3)
# we get a filter object in memory address form.

for el in house3:
    print(el)


# aliter:
print("--------------------")
house3_ = filter(lambda s: s["house"] == "house 3", students)

for el in house3_:
    print(el)

# we can also iterate over deictionary by filter:

studentInfo = [
    {"name": "ayush", "job": "electronics engineer"},
    {
        "name": "ramesh",
        "job": "IT",
    },
    {"name": "suresh", "job": "design"},
    {"name": "rohan", "job": "electronics engineer"},
    {"name": "rahul", "job": "electronics engineer"},
]


def is_engineer(s):
    return s["job"] == "electronics engineer"


electronics_engineer = filter(is_engineer, studentInfo)

for el in electronics_engineer:
    print(el)
