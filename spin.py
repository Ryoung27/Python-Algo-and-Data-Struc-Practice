import re
def spin_words(sentence):
    backward_list = []
    # Your code goes here
    wordList = re.sub("[^\w]", " ",  sentence).split()
    print(wordList)
    for i in wordList:
        if len(i) >= 5:
            backward_list.append(i[::-1])
        else:
            backward_list.append(i)
    return ' '.join(backward_list)
