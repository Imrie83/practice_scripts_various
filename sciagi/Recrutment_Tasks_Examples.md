## Bubble Sort:
```python
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
```

## Upper case count:
```python
import sys

file_name = sys.argv[1]
count = 0
with open(file_name) as f:
    text = f.read()

    for letter in text:
        if letter.isupper():
            count += 1

print(count)
```

## Flatten list with generator:
```python
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

```