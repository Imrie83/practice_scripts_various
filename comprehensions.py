# comprehensions are single line alternatives to creating a list, dictionary or generator

my_list = [2 ** i for i in range(20)]
my_dict = {f'position - {i + 1}:': 2 ** i for i in range(20)}

print(my_list)
print(my_dict)
