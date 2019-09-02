def Descending_Order(num):
    #Bust a move right here
    num_list = []
    num = str(num)
    for i in num:
        num_list.append(i)
    num_list.sort(reverse=True)
    num_string = ''.join(num_list)
    num = int(num_string)
    return num