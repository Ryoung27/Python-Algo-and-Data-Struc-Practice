def digital_root(n):
    total = 0
    string = str(n)
    for i in string:
        integer = int(i)
        total = total + integer
#     print(total)
    if len(str(total)) > 1:
        total_string = str(total)
        total = 0
        for i in total_string:
            integer = int(i)
            total = total + integer
#     print(len(str(total)))
    return(total)
