

#Given a getSquare() function, make a list comprehension that returns a list with the squares of all
# even numbers from 0 to 20, but ignores those numbers that are divisible by 3.

def getSquare():
    l1 = [x * x for x in range(0, 21, 2) if x % 3 != 0]
    # l1=[ x**2 for x in range(0, 21) if x % 3 != 0 and x % 2 == 0]

    return l1

print(getSquare())