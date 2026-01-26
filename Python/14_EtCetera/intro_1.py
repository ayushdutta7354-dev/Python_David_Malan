# Etcetera:

students = [
    {"name": "ayush", "house": "Vijay Nagar"},
    {"name": "ramesh", "house": "Greater noida"},
    {"name": "suresh", "house": "Sector 25"}
]

# 1. 
houses_list = [];

for student in students:
    if student["house"] not in houses_list:
        houses_list.append(student["house"]);

for house in sorted(houses_list):
    print(house);

# 2. aliter of above:

print("-------------------------------------------------");

houses_set = set();

for student in students:
    houses_set.add(student["house"]);

for house in sorted(houses_set):
    print(house);



