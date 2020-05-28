
## find Max value in list


def findMaximum(list):

    maximum = list[0]
    for num in list:
        if num > maximum:
            maximum = num
    return maximum

list =[1, 2, 7, 4, 5]

print(findMaximum(list))

## find max value with its index

def findMaximumValueIndex(list):
    maximum = list[0]
    index = 0
    for i, value in enumerate(list):
        if value > maximum:
          maximum = value
          index = i
    return [index, maximum]

list = [1, 2, 7, 4, 5]
[index, maximum] = findMaximumValueIndex(list)

print("Index:", index)
print("Maximum Value:", maximum)