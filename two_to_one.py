def longest(s1, s2):
    # your code
    s3 = s1 + s2
    s_list = []
    sorted_s_list = []
    for i in s3:
        s_list.append(i)
    s_list = list(dict.fromkeys(s_list))
    sorted_s_list = sorted(s_list)
    answer = ''.join(sorted_s_list)
    return answer
