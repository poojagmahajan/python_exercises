
# Given an AppendtoList() function, create a list named l with the following values:[1, 4, 9, 10, 23]

# and appends the number 90 at the end of the list.


def AppendtoList():
  l = [1, 4, 9, 10, 23]
  l.append(90)
  return l
l = AppendtoList()
print(l)

# or using concatenate

l1 = [1, 4, 9, 10, 23]
print(l1)
l1 = l1 + [90]
print(l1)