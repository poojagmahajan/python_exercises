

###  A Python generator is a convenient way to implement an iterator. Instead of a class,
# a generator is a function which returns a value each time the yield keyword is used.
#  yield is work like return except it allows funcion to continue

#example of a generator to count the values between two numbers:

def myrange(a, b):
  while a < b:
    yield a
    a += 1
a = myrange(2, 4) # call the generator function which returns an object
print (next(a)) # iterate through items using next
print (next(a))


#  Yield Odd Numbers From 1 to n

def odd(n):
  for value in range(n):
    if value % 2 != 0:
      yield value

#p = odd(8)
#print(next(p))

for j in odd(8):
  print(j)

### Yield Numbers From n Down to 0

def reverse(n):
  for value in range(n, -1, -1):
    yield value

for i in reverse(8):
  print(i)

 #### Yield Fibonacci Sequence From 1st to Nth Number

def fibonacci(n):
    myArray = []
    for i in range(n):
        if i == 0 or i == 1:
            myArray.append(i)
            yield i
        else:
            x = myArray[i - 2] + myArray[i - 1]
            myArray.append(x)
            yield x


for i in fibonacci(8):
    print(i)