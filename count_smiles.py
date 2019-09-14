def count_smileys(arr):
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']
    count = 0
    print(arr)
    for i in arr:
        print(i)
        if i[0] in eyes and i[1] in mouth:
            count += 1
        elif i[0] in eyes and i[1] in nose and i[2] in mouth:
            count += 1
    return count
