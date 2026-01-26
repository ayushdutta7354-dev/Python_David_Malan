# Libraries in python: 

# 1. What is a Module in Python? # A module is just a single Python file that contains code (functions, variables, classes).

# You can import a module like this: 
# import module_name

# simulate coin toss:

import random;#

coin = random.choice(["heads", "tails"]);

print(coin);

# if we dont have to use module name random: we can do below

from random import choice;

dice = choice([1,2,3,4,5,6]);
print(dice);

# another fn in random module is randint(a,b) a and b inclusive:

randomInteger = random.randint(1,10);
print(randomInteger);

# random.shuffle(list): shuffles the input list

cards = ["Jack", "Queen", "King"];
random.shuffle(cards);

print(cards);

for card in cards:
    print(card);

# lets create our own module:

import avg_module_7;

score = avg_module_7.average();

print(score);

import Libraries_7;
import sys;

if(len(sys.argv) == 2):
    Libraries_7.hello(sys.argv[1]);
    Libraries_7.goodbye(sys.argv[1]);