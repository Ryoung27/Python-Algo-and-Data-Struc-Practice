def array_mash(a, b):
    # your code here
    answer_list = []
    print(a)
    print(b)
    for i in range(len(a)):
        answer_list.append(a[i])
        answer_list.append(b[i])
    return answer_list
