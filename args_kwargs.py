def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


def auth(**kwargs):
    for key in kwargs:
        print(f'{key} - {kwargs[key]}')


print(multiply(2, 4, 6, 1, 3))
auth(Tolkien='Fantasy', Abbnett='Sci-Fi')
