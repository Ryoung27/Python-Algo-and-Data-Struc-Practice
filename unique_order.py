def unique_in_order(iterable):
    print(iterable)
    answer_list = []
    for i in range(len(iterable) - 1):
        if iterable[i] == iterable[i+1]:
            pass
        else:
            answer_list.append(iterable[i])
    if not answer_list:
        if iterable:
            answer_list.append(iterable[-1])
    else:
        if answer_list[-1] != iterable[-1]:
            answer_list.append(iterable[-1])
    return answer_list
