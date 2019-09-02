import math
def is_square(n):
    n = str(n)
    if n[0] == '-':
        return False
    n = int(n)
    root = math.sqrt(n)
    print(root)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False
