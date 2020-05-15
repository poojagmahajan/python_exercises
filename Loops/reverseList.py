


### Reverse given list
#  Calculate the length of the list using the len() function.
#  Create a new list.
#  Run a backward loop starting from len to index 0.


def reverse (list)  :
    length = len (list)
    s = length    # e.g length is 5

    new_list = [None] * length     # create empty list
    for num in list :
        s= s-1   # s=4 ,means last index --- list [4]
        new_list[s] = num
    return new_list

list = [1,2,3,4,5]
print(reverse(list))



