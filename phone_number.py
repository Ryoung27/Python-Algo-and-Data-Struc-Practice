def create_phone_number(n):
    #your code here
    phone_number = ''
#     print(n)
    phone_number = '('
    for i in n[0:3]:
        i = str(i)
        phone_number += i
    phone_number += ') '
    for i in n[3:6]:
        i = str(i)
        phone_number += i
    phone_number += '-'
    for i in n[6:10]:
        i = str(i)
        phone_number += i
    return phone_number