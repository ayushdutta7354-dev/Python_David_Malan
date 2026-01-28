# more robust code with dict reader
import csv;
friends_ = [];
with open("Student_3.csv") as file:
    reader = csv.DictReader(file); #csv.reader reades entire file.
    # make sure your csv file contains the name of columns, eg here: name, house
    for row in reader:
        friends_.append({"name": row["name"], "house": row["house"], "address":row["address"]});

for friend in sorted(friends_, key=lambda friend: friend["house"]):
    print(f"{friend["name"]} lives in {friend["house"]}");


print(friends_);
