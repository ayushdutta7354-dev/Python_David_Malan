# Deep Copy: memory ref.

list_1 = [1, 2, 3]

list_2 = list_1

list_1[0] = 100
print(list_1, id(list_1))
print(list_2, id(list_2))

list_2[1] = 5
print(list_1)
print(list_2)

# change haapn in both bcz both ref to same memory location

# shallow copy:

list_3 = [45, 35, 78]

list_4 = list_3.copy()
# return shallow copy of prev list.

list_3[0] = 555
list_4[0] = 123

print(list_3, id(list_3))
print(list_4, id(list_4))

# slicing:

print(list(range(1,10)));
print(list(range(1,10,3)));
print(list(range(1,10,-2)));

li = [1,2,3,4,5,6]

print(li[0:3]);
print(li[1:]);
print(li[:]);
print(li[::-1]); #reverse slice