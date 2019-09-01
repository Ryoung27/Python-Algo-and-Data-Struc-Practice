import re
def pig_it(text):
    pig_latin_list = []
    new_pig = []
    pig_latin_list = re.findall(r"[\w']+|[.,!?;]", text)
    print(pig_latin_list)
    for i in pig_latin_list:
        if len(i) < 2 and i in ('.', ',', '!', '?', ';'):
            new_pig.append(i)
        else:
            i = i[1:]+i[0]
            i = i + "ay"
            new_pig.append(i)
#     print(new_pig)
    pig_string = ' '.join(new_pig)
    return pig_string
#         word[1:]+word[0]
