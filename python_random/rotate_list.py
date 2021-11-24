from datetime import datetime


# faster version
def rotate(my_list, num_rotations):
    start = datetime.now()
    if num_rotations == len(my_list):
        return my_list

    if num_rotations > len(my_list):
        num_rotations = num_rotations - len(my_list)

    my_slice = my_list[0:-num_rotations]
    my_list = my_list[-num_rotations:]
    my_list.extend(my_slice)
    print(datetime.now() - start)
    return my_list


# slower version
# def rotate(my_list, num_rotations):
#     start = datetime.now()
#     if num_rotations == len(my_list):
#         return my_list
#
#     if num_rotations > len(my_list):
#         num_rotations = num_rotations - len(my_list)
#
#     for i in range(len(my_list[:-num_rotations])):
#         my_slice = my_list.pop(0)
#         my_list.append(my_slice)
#
#     print(datetime.now() - start)
#     return my_list






#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c', 'd']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['c', 'd', 'e', 'f', 'a', 'b']))