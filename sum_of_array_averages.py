import math
def sum_average(arr):
    # your code here
    average_list = []
    y = 0
    a = 0
    for i in arr:
        for x in i:
           y += x
        average_list.append(y/len(i))
        y = 0
    print(average_list)
    for i in average_list:
        a += i
    return (math.floor(a))
