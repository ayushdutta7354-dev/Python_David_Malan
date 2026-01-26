# Map:

def main():
    yell("This is CS50");
    # what if we pass list to yell:
    yell_1(["This", "is", "CS50"]);
    yell_2("This","is","CS50");

# 1.
def yell(str):
    print(str.upper());

# 2.
def yell_1(words):
    uppercased = [];
    for word in words:
        uppercased.append(word.upper());
    print(*uppercased);

def yell_2(*words):
    # uppercased = map(str.upper, words);
    # aliter:
    uppercased = [word.upper() for word in words];#this is filetering in pyhton list
    print(*uppercased);

if __name__ == "__main__":
    main();

