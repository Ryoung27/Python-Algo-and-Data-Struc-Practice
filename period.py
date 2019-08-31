def period_is_late(last,today,cycle_length):
    #your code here
    date = last-today
    return (abs(date.days) > cycle_length)
