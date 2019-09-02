def disemvowel(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    lower_vowels = ('a', 'e', 'i', 'o', 'u')
    for i in string.upper():
        if i in vowels:
            i = i.upper()
            string = string.replace(i, '')
    for i in string.lower():
        if i in lower_vowels:
            i = i.lower()
            string = string.replace(i, '')
    return string 
