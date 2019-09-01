def find_outlier(integers):
    even_count, odd_count = 0, 0
    # iterating each number in list 
    for num in integers: 
        # checking condition 
        if num % 2 == 0: 
            even_count += 1
        else: 
            odd_count += 1
    if even_count > odd_count:
        for num in integers:
            if num % 2 !=0:
                return num
    elif odd_count > even_count:
        for num in integers:
            if num % 2 == 0:
                return num
