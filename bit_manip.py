def eliminate_set_bits(number):
    # TODO
    if number.count('1') == 0:
        return 0
    else:
        all_one = number.replace('0', '')
        all_one = int(all_one, 2)
        return (all_one)
