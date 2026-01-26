import cowsay;
from sys import argv;
import sys;
import json;
import requests;

if len(argv) == 2:
    cowsay.trex("hello,", argv[1]);


with open("temp.json", "r") as file:
    data = json.load(file);

print(data);

if len(argv) != 2:
    sys.exit();

response = requests.get("https://itunes.apple.com/search?term=SEARCH_TERM" + argv[1]);

print(response.json());
print(json.dumps(response.json()));

result_object = response.json();

for obj in result_object["results"]:
    print(obj);