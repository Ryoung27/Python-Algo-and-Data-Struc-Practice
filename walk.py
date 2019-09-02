def isValidWalk(walk):
    #determine if walk is valid
#     pass
    n = 0
    s = 0
    w = 0
    e = 0
    for i in walk:
        if i == 'n':
            n += 1
        elif i == 's':
            s += 1
        elif i == 'w':
            w += 1
        elif i == 'e':
            e += 1
    print(n)
    print(s)
    print(e)
    print(w)
    if (n + s + e + w) == 10:
            if n == s and e == w:
                return True
            else:
                return False
    else:
        return False
