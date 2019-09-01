def is_palindrome(string):
    if type(string) == int:
        string = str(string)
    if string[::1] == string[::-1]:
        return True
    else:
        return False
