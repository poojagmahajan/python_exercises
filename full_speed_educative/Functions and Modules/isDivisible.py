#   Implement a function named isDivisible that receives two parameters (named x and y)
#   and only returns true if “x” can be divided by “y”(and false otherwise).

#  A number is divisible by another when the remainder of the division is zero. Use the modulo operator ("%").

def isDivisble(x ,y):
    if  x % y == 0:
        return True
    else :
        return False

print(isDivisble(24, 4))
print(isDivisble(24, 7))