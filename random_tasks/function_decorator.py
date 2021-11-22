def multiply(a, b):
    return a * b

def multiply_decorator(fun, c):
    return fun * c

print(multiply(3, 5))
print(multiply_decorator(multiply(3, 5), 3))