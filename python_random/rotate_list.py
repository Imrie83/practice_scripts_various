from datetime import datetime


# slowest version?
def rotate(my_list, num_rotations):
    start = datetime.now()
    if num_rotations == len(my_list):
        return my_list

    if num_rotations > len(my_list):
        num_rotations = num_rotations - len(my_list)

    my_slice = my_list[0:-num_rotations]
    my_list = my_list[-num_rotations:]
    my_list.extend(my_slice)
    time = datetime.now() - start
    return f"{my_list}, execution time: {time}"


# slower version
def rotate_3(my_list, num_rotations):
    start = datetime.now()
    if num_rotations == len(my_list):
        return my_list

    if num_rotations > len(my_list):
        num_rotations = num_rotations - len(my_list)

    for i in range(len(my_list[:-num_rotations])):
        my_slice = my_list.pop(0)
        my_list.append(my_slice)

    time = datetime.now() - start
    return f"{my_list}, execution time: {time}"


# Fastest version
def rotate_2(my_list, num_rotations):
    start = datetime.now()
    if num_rotations == len(my_list):
        return my_list

    if num_rotations > len(my_list):
        num_rotations = num_rotations - len(my_list)

    my_list[num_rotations:], my_list[:-num_rotations] = (
        my_list[:num_rotations],
        my_list[num_rotations:],
    )
    time = datetime.now() - start
    return f"{my_list}, execution time: {time}"


# #### TESTS SHOULD ALL BE TRUE ####
print(
    "{0}\n should equal \n{1}\n {2}\n".format(
        rotate(["a", "b", "c", "d", "e", "f"], 1),
        ["f", "a", "b", "c", "d", "e"],
        rotate(["a", "b", "c", "d", "e", "f"], 1) == ["f", "a", "b", "c", "d", "e"],
    )
)
print(
    "{0}\n should equal \n{1}\n {2}\n".format(
        rotate_3(["a", "b", "c", "d", "e", "f"], 1),
        ["f", "a", "b", "c", "d", "e"],
        rotate_3(["a", "b", "c", "d", "e", "f"], 1) == ["f", "a", "b", "c", "d", "e"],
    )
)
print(
    "{0}\n should equal \n{1}\n {2}\n".format(
        rotate_2(["a", "b", "c", "d", "e", "f"], 1),
        ["b", "c", "d", "e", "f", "a"],
        rotate_2(["a", "b", "c", "d", "e", "f"], 1) == ["b", "c", "d", "e", "f", "a"],
    )
)
