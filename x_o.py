def xo(s):
    x_count = 0
    o_count = 0
    lower_s = s.lower()
    for i in lower_s:
        print(i)
        if i == 'x':
            x_count += 1
        elif i == 'o':
            o_count += 1
    if x_count == o_count:
        return True
    else:
        return False
