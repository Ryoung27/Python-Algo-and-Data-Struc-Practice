def likes(names):
    #your code here
    people_who_liked = 0
    for i in names:
        people_who_liked += 1
    print(people_who_liked)
    if people_who_liked < 1:
        return 'no one likes this'
    elif people_who_liked == 1:
        return f"{names[0]} likes this"
    elif people_who_liked == 2:
        return f"{names[0]} and {names[1]} like this"
    elif people_who_liked == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {people_who_liked - 2} others like this"
