def accum(s):
    mumble_list = []
    capital_mumble = []
    count = 0
    for i in s:
        i = i.lower()
        count += 1
        mumble_word = i * count
        mumble_list.append(mumble_word)
    for i in mumble_list:
        i = i.capitalize()
        capital_mumble.append(i)
    return '-'.join(capital_mumble)
