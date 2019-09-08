def countBits(n):
    binary_count = 0
    binary_number = bin(n)[2:]
    print(binary_number)
    binary_string = str(binary_number)
    for i in binary_string:
        if i == '1':
            binary_count += 1
    return binary_count
