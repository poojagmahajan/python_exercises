
# List comprehensions are a concise way to create lists.
# They consist of square brackets containing an expression followed by the for keyword;
# the result will be a list whose results match the expression.

# Example -how to create a list with the squared numbers of another list.

print([x*x for x in [2,3,4,5]] )

print(range(4))

print ([p*p for p in range(4)])

#  displays all elements from 0 to 9 which are divisible by 2.

print ( [ x for x in range(10) if x % 2 == 0 ]  )