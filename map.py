numbers = (1, 2, 3, 4, 5)

def multiply(x):
    return x * 2

def addition(y):
    return y + y

result = map(multiply, numbers)
addition_result = map(addition, numbers)

print(list(result))
print(list(addition_result))