# Module to calculate avg:

def average():
    while True:
        try:
            return (int(input("enter a: "))+int(input("enter b: "))+int(input("enter c: ")))/3;
        except ValueError:
            pass;


