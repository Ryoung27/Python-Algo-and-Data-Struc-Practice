def iq_test(numbers):
    total = 0
    even_list = []
    odd_list = []
    new_numb = map(int, numbers.split(' '))
    for i in new_numb:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(numbers)
    print(even_list)
    print(odd_list)
    if len(even_list) > len(odd_list):
        answer_number = odd_list[0]
    else:
        answer_number = even_list[0]
    print(answer_number)
    for i in new_numb:
        total += 1
        if i == answer_number:
            return total
