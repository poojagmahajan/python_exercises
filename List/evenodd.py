
#  Given a ListofEvenOdds() function, create a list comprehension with all the even numbers from 0 to 20,
#  and another one with all the odd numbers.
#input - two empty lists


def ListofEvenOdds():

   l1 = [x for x in range(1,21) if  ( x%2 == 0 ) ]  # list of even numbers
   l2 =[x for x in range(1,21) if  ( x%2 != 0 ) ]   # list of odd numbers
    # l2 = [x for x in range(0, 21) if (x not in l1)
   return [l1, l2]

print(ListofEvenOdds())


#Given an evenSquare() function, create a list with the squares of the even numbers from 0 to 20.
# The final output should be the sum of even numbers in the list:
#Input -  A list with the square of even numbers from 0-20

def evenSquareSum():
  #write code here
  l1 = []

  #l1 = [x * x for x in range(0,21) if ( x % 2 == 0)]
  l1 = [x * x for x in range(0, 21, 2)]
  return  sum(l1)

print( evenSquareSum())