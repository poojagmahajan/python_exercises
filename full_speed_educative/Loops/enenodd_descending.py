

### print even - odd number in descending number

def printEvenOdd(n):
  while(n > 0):
    if (n % 2 == 0):
      print ("Even number:",n)
    else:
      print ("Odd number:",n)
    n = n - 1

printEvenOdd(10)