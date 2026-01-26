# List:

print("Lecture on List in Python")

"""
in python list is like array in c++, but in c++ data in array is homogeneous(same datatype), in python its heterogeneous

list -> mutable, orderesrd element, allow duplicate data
"""

students = ["ayush", "abhi", "rohan", "ramesh", "suresh", 1, 2, 3, True]

print(students)

students.append("rahul") #mutable array
print(students)
print(type(students))

students.insert(2, "chandan");
print(students);

students_2 = [5,7,8];

students.extend(students_2); #join 2 array
print(students);

students.remove("suresh");
print(students);

students.pop();

print(students);
print(id(students));

students.clear();#this is the same list

students = [];#this is a new list in memory

print(id(students));

num = [5,78,0,35,-4,45,3,10];

num.sort(); #ascending
print(num);

num.sort(reverse=True); #descending
print(num);

#################################
