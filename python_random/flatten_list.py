lista = [1, 2, [3, 4, 5], [6, [7, 8, 9], 10], 11, 12]
print(lista)


def flatten(my_list):
    for nested in my_list:
        if isinstance(nested, list):
            yield from flatten(nested)
        else:
            yield nested


lista = list(flatten(lista))
print(lista)
