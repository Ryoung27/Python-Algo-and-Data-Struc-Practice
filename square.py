def square_digits(num):
#     pass
    num = str(num)
    square_list = []
    for i in num:
        i = int(i)
        x = i * i
        x = str(x)
        square_list.append(x)
    y = ''.join(square_list)
    y = int(y)
    return y
    print(square_list)
