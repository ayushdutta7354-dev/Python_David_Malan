#GCD and LCM:

#eucleadean algo:
def GCD(a,b):
    #base case:
    if b ==0:
        return a;

    #recursive case:
    return GCD(b,a%b);