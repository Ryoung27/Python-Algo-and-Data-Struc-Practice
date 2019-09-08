from functools import reduce
from operator import mul

def persistence(n, count=0):
    # your code
    if n < 10:
        return count
    new_number = reduce(mul, map(int, str(n)))
    
    return persistence(new_number, count + 1)
        
