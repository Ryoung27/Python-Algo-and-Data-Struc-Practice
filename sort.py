def get_sum(a,b):
    #good luck!
    new_list = []
    new_list.append(a)
    new_list.append(b)
    new_list.sort()
    a = new_list[0]
    b = new_list[1]
    final_answer = 0
    print(a)
    print(b)
    x = range(a, (b+1), 1)
    print(x)
    for n in x:
        final_answer = final_answer + n
    return final_answer
