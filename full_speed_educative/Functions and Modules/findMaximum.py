

#  Implement the findMaximum function that receives two numbers as arguments x and y
#  and returns the maximum of the numbers.

# hint - use max()

def findMaximum(x, y):
  # max2 = 0
  if(x > y):
    max2 = x
    print(max2)
  else :    #max2 = y
    return y

print(findMaximum(2, 3))

####### or

def findMaximum(x, y):
  max2 = 0
  if(x > y):
    max2 = x
  max2 = y
  return max2
print(findMaximum(2, 3))

#### Using max()

def findMaximum(x, y):
  max2 = max(x, y)
  return max2
print(findMaximum(2, 3))