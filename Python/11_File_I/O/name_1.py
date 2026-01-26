# now we want names in names_.txt to be sorted:

names = [];

with open("names_.txt") as file:
    for line in file:
        names.append(line.rstrip());

for name in sorted(names):
    print(f"hello, {name}");


# now we will learn .csv file in students.csv.