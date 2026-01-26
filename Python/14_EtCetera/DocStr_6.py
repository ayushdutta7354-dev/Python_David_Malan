# DocStrings in python: Doc string means documenting our fn  of what it does and how it works. 

def meow(n: int) -> str:
    """
    Docstring for meow n times.
    
    :param n: takes in integer
    :type n: int
    :raise typeError: If n is not an int
    :return: a string of n meows, one per line
    :rtype: str
    """ 
    return "meow\n" *n;

num: int = int(input("Enter num: "));
print(meow(num));