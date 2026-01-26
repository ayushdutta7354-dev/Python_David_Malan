# writing to file using csv:

import csv;

name = input("Enter your name: ");
house = input("Enter house number: ");

with open("Student_4.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"]);#we wrote fieldnames so that python can recognize which coln is whom
    writer.writerow({"name":name, "home":house});