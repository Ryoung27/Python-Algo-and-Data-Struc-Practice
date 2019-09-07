def add_binary(a,b):
    #your code here
    number_to_convert = a + b
    print(number_to_convert)
    converted_number = bin(number_to_convert)
    return(str(converted_number[2:]))
