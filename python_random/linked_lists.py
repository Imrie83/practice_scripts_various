from datetime import datetime
from random import random, randint


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


e = Node(2)
f = Node(4)
g = Node(6)
h = Node(8)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

#   A -> B -> C -> D -> None
start = datetime.now()

# DESC: iterative and recursive way to output a contend of a linked list.
def print_link_list(head):
    current = head
    output_list = []
    while current is not None:
        output_list.append(current.val)
        current = current.next
    return output_list


# def fill_values(head, output_list):
#     if head is None:
#         return None
#     output_list.append(head.val)
#     fill_values(head.next, output_list)
#
#
# def print_link_list(head):
#     output_list = []
#     fill_values(head, output_list)
#     return output_list


# DESC: sum values of linked list
# iterative O(n):
# def sum_linked_list(head):
#     list_sum = 0
#     current = head
#     while current is not None:
#         print(f'{list_sum} + {current.val} = {list_sum + current.val}')
#         list_sum += current.val
#         current = current.next
#     return list_sum


# recursive O(n)
def sum_linked_list(head):
    if head is None:
        return 0
    return head.val + sum_linked_list(head.next)


# # DESC: find value in linked list
# # iterative
# def find_value(head, val):
#     while head is not None:
#         if head.val == val:
#             return True
#         head = head.next
#     return False


# recursive
def find_value(head, val):
    if head is None:
        return False
    elif head.val == val:
        return True
    else:
        return find_value(head.next, val)


# DESC: find value at index
# iterative
# def find_val_by_index(head, index):
#     count = 0
#     while head is not None:
#         if count == index:
#             return head.val
#         count += 1
#         head = head.next
#     return None


# recursive
def find_val_by_index(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return find_val_by_index(head.next, index - 1)


# DESC: find value index
# recursive
def find_index(head, value):
    count = 0
    while head is not None:
        if head.val == value:
            return count
        head = head.next
        count += 1
    return None

# DESC: reverse linked list and return new head.
# iterative
def reverse_list(head):
    prev = None
    current = head

    while head is not None:
        next_val = current.next
        current.next = prev
        prev = current
        current = next_val
    return prev


end = datetime.now() - start
# print(print_link_list(a))
# print(sum_linked_list(e))
# print(f'Sum of list elements = {sum_linked_list(a)}')
print(find_value(a, 'E'))
print(find_value(a, 'C'))
print(find_index(a, 'B'))
print(end)
