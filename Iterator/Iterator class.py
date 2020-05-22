

### Iterators can be implemented as classes; you just need to implement the __next__ and __iter__ methods.

## example of a class that mimics the range function, returning all values from a to b:

class MyRange:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):  # returns the iterator object itself
        return self

    def next(self):
        if self.a < self.b:  # returns the next item in the sequence
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration


myrange = MyRange(1, 4)
print(myrange.next())
print(myrange.next())
print(myrange.next())
##print (myrange.next())    ## it raises the StopIteration exception

## you can use ierator class in for loop

#for value in MyRange(1, 4):
 #    print(value)
