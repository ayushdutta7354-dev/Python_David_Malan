#Dictionary:

d1 = {
    "name": "Ayush Dutta",
    "id": 12345
}

print(d1);

#keys unique, value can be duplicate

print(d1["id"])
print(d1["name"])
print(len(d1))
print(type(d1))

#mutable:

d1["id"] = 123456;

print(d1);

d2 = {1:"ayush", 2:"abhi", 3:"rahul"};

d2.pop(2);

d2.update({10:"ramesh", 9: "suresh"});

print(d2);

#list of keys val:

print(list(d2.keys()))
print(type(list(d2.keys())[0]))
print(list(d2.values()))

##################################################################

#freq of element in list:

list1 = [1,2,3,3,3,4,5,5,5,6,7,7,7,7];
freq = {}

for i in list1:
    if i in freq:
        freq[i]+=1;
    else:
        freq[i] = 1


for i in freq:
    print(f"{i} is present {freq[i]} times");


print(freq)