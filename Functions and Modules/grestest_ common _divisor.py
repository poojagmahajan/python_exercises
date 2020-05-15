

#  Write a findGCD function that takes in two numbers as input a and b
#  and finds the greatest common divisor of the two.

# hint  -  Use the built-in function math.gcd(number1,number2) function
#          to return the greatest common divisors of two numbers

import math   # math is a module

def findGCD(a, b):
  return math.gcd(a, b)
print(findGCD(24, 18))

