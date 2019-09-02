import re
def find_short(s):
    word_count_1 = []
    wordList = re.sub("[^\w]", " ",  s).split()
    for i in wordList:
        len_i = len(i)
        word_count_1.append(len_i)
    min_answer = min(word_count_1)
    return min_answer
