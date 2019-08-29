my_list = [4,1,2,1,2]

seen = {}
dupes = []

for x in my_list:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1
for i in dupes:
    # print(i)
    if i in my_list:
        while i in my_list:
            my_list.remove(i)
print(my_list[0])
    # return my_list[0]
    # if i in my_list:
    #     my_list.remove(i)
    # print(my_list)
#     for i in dupes:
#         print(i)
#         # my_list.remove(i)
# print(my_list)

# print(dupes)
# print(my_list)