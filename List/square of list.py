

## Given a getSquare() function, create a list with the squares of the first 10 numbers,
# i.e., in the range from 1-10.
# input empty list


def getSquare():

  l1 = []
  l1 = [x*x for x in range(1, 11)]

  return l1

#l1 = getSquare()
print (getSquare())
#print(l1)