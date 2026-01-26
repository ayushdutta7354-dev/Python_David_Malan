#is power of 2:

    #by loop:
    # if a ==0:
    #     return False
    
    # while a%2==0:
    #     a/=2
    
    # return a ==1

def isPowerOfTwo(a:int)->bool:
    #base case:
    if a ==0:
        return False
    if a == 1:
        return True
    if a %2 ==1:
        return False
    return isPowerOfTwo(a//2);

print(isPowerOfTwo(20))
print(isPowerOfTwo(16))
print(isPowerOfTwo(32))