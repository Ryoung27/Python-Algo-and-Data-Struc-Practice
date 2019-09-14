def validate(n):
    print(n)
    n = str(n)
    n = n[::-1]
    new_values = []
    print(n)
    index = 1
    answer = 0
    for i in n:
        if index % 2 == 0:
            i = int(i)
            i = i * 2
            if i > 9:
                i = i - 9
            new_values.append(i)
            index += 1
        else:
            i = int(i)
            new_values.append(i)
            index += 1
    print(new_values)
    for i in new_values:
        answer += i
    print(answer)
    if answer % 10 == 0:
        return True
    else:
        return False
