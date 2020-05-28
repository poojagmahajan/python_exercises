


# check if given list is sorted or not


def isSorted(list):
    flag = 0
    i = 1
    while i < len(list):
        if (list[i] < list[i - 1]):  # compare with the previous element
            flag = 1
        i += 1

    if (not flag):     # if (flag ==0):
        return True
    else:
        return False


print(isSorted([1, 2, 3, 4, 5]))
print(isSorted([1, 2, 5, 4, 2]))