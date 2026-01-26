#Time Complexity: Variation of time taken by algo as input size grow.

# diff variation of time compx:

# 1. O-n: for n i/p n operation.

def print_num(n):
    for i in range(n):
        print(i);

print_num(5);

# 2. O-n^2

def a(n):
    for i in range(n):
        for j in range(n):
            print(i,j, end=" ");

a(5);


# 3. O-1
print("\n");
def sum_nat(n):
    return (n*(n+1))/2;

print(sum_nat(5));

"""
in a time compx: O(n^2+n), neglect n, bcz n is inferior. similarly, O(n+k), neglect constant(k).
"""

# 4. O(logn): 1,2,4,8,16,....=> 2^0, 2^1,2^2,....=> 2^k = n => k = logn. (k: number of oiperation)

def b(n):
    i=1;
    while i<=n:
        print(i, end=" ");
        i*=2;


b(1000);