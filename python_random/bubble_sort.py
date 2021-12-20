from random import randint

my_list = [randint(0, 100) for i in range(10)]
print(my_list)


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubble_sort(my_list))
