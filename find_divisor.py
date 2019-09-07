import math
def divisors(integer):
    answer_list = []
    print(integer)
    for i in range(2, math.floor(integer/2)+1):
        print(i)
        if integer % i == 0:
            answer_list.append(i)
    if not answer_list:
        return str(integer) + " is prime"
    else:
        return answer_list
