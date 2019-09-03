def reverse_list(x):
    """Takes an list and returns the reverse of it. 
    If x is empty, return [].
    >>> reverse_list([])
    []
    >>> reverse_list([])
    []
     """ 
    
    # Your code goes here...
    if not x:
        return x
    else:
        return x[::-1]

def sum_list(x):
    """Takes a list, and returns the sum of that list.
    If x is empty list, return 0.
    >>> sum_list([1,2,3])
    6
    >>> sum_list([])
    0
    """

    # Your code goes here...
    y = 0
    for i in x:
        y += i
    if not x:
        return 0
    else:
        return y

def head_of_list(x):
    """Takes a list, returns the first item in that list.
    If x is empty, return None
    >>> head_of_list([1,2,3])
    1
    >>> head_of_list([3,2,1])
    3
    """ 
    if x == []:
        return None
    else:
        return x[0]
    # Your code goes here...
