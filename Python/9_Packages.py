# Packages: bundle of modules. python package manager is pip. To install a package, pip install [__package__]

import cowsay;
import sys;

if(len(sys.argv)== 2):
    cowsay.trex("hello, "+ sys.argv[1]);

import json;

with open("9_api.json", "r") as file:
    data=json.load(file);

print(data);

# APIs: What is an API?API = Application Programming Interface

"""
In simple terms: An API is a way for one program to talk to another program. Just like humans talk using language, computers programs talk using APIs. The API sends back a response in a format like JSON: 

JSON:

{
//json data and methods:
}
"""

import requests;

if(len(sys.argv) != 2):
    sys.exit();

response = requests.get("https://itunes.apple.com/search?term=SEARCH_TERM" + sys.argv[1]); 

print(response.json());
print(json.dumps(response.json()));


print("---------------------------------------------");
resultObj = response.json();

for obj in resultObj["results"]:
    print(obj);



