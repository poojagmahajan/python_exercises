

#######  The built-in iter method can be used to build iterator objects,
#        while the next method can be used to gradually iterate over their content:

my_iter = iter([1, 2, 3])
print (next(my_iter))
print (next(my_iter))
print (next(my_iter))

my_iter = iter([4,5])
print (next(my_iter))

my_iter = iter([1, 2, 3])
next(my_iter)
next(my_iter)
next(my_iter)



