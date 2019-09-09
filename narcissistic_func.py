def narcissistic( value ):
    print(value)
    total = 0
    leng_of_val = len(str(value))
    leng_of_val = int(leng_of_val)
    value = str(value)
    for i in value:
        print(int(i) ** leng_of_val)
        total += int(i) ** leng_of_val
    print(total)
    value = int(value)
    if value == total:
        return True
    else:
        return False
