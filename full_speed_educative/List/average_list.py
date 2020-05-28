

# Average of given list

def getAverage():
    l1 = [1, 4, 9, 10, 23]
    avg = sum(l1) / len(l1)
    return avg


avg = getAverage()
print(avg)


########## OR

l = [1,4,9,10,23]
list_sum = sum(l)
list_length = len(l)
average = list_sum/list_length
print(average)

