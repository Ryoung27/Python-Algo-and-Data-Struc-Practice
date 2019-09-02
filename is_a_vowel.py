def is_vow(inp):
    codes = (97, 101, 105, 111, 117)
    converted_list = []
    for i in inp:
        if i in codes:
            if i == 97:
                i = 'a'
                converted_list.append(i)
            elif i == 101:
                i = 'e'
                converted_list.append(i)
            elif i == 105:
                i = 'i'
                converted_list.append(i)
            elif i == 111:
                i = 'o'
                converted_list.append(i)
            elif i == 117:
                i = 'u'
                converted_list.append(i)
        else:
            converted_list.append(i)
    return converted_list
