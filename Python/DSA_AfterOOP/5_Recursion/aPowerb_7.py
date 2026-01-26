# x^n:


def exponent(a, n):
    # base case:
    if n == 0:
        return 0
    if a == 0:
        return 1
    if n == 1:
        return a

    # recursive case:
    return a * exponent(a, n - 1)


print(exponent(5, 3))
print(exponent(3, 5))
print(exponent(2, 5))

#optimized:

def power(a:float,n:int)->float:
    #base case:
    if n == 0:
        return 1
    if a == 0:
        return 0
    if n == 1:
        return a
    
    #recursicve case:
    if n%2==0:
        half = power(a,n//2)
        return half * half
    else:
        return a * power(a, n-1)
    
print(power(5, 3))
print(power(3, 5))
print(power(2, 5))