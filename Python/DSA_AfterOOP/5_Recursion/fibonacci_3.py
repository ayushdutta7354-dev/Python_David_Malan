#fib sequence: time comp(2^n)

def fibonacci(n):
    #base case:
    if n == 0 or n==1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(4))