# Recusion intro:

"""
Docstring for recursion_1

fn calling itself until a base case is met. similar to a loop

diffn b/w loop
"""


def a(n):
    if n == 6:
        return

    print(n,end=" ")
    return a(n + 1)


a(0)

# abv with loop
print()
i = 0
while i<6:
    print(i, end=" ")
    i+=1


#print even numbers upto specified number
print()
def print_even(a,n):
    #base case
    if a == n:
        return
    
    if a%2!=0:
        return
    
    print(a, end=" ")
    return print_even(a+2,n)

print_even(0,12)
print()
print_even(-2,12)
print_even(3,12)


#print even numbers upto specified number
def print_odd(a,n):
    #base case:
    if a == n:
        return
    
    if a%2!=0:
        print(a,end=" ")
        return print_odd(a+2,n)

print()
print_odd(1,9)


