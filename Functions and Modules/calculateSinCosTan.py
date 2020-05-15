
#  Use the calculateSinCosTan() function; it takes a number x as a parameter
#  and shows the result of the sine, cosine, and tangent of the number.

import math
def calculateSinCosTan(x):
  sine = math.sin(x)
  cos = math.cos(x)
  tan = math.tan(x)
  return [sine, cos, tan]   # o/p in brackets

print("sine:", calculateSinCosTan(-1))
print("cos:", calculateSinCosTan(0))
print("tan:", calculateSinCosTan(1))