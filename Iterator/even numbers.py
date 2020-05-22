

### print enen numbers from 1 to n

class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        evenArray = []  # next method returns this list
        for i in range(1, self.n + 1):
            if( i % 2 == 0):  # checks if number is even
                value = i
                evenArray.append(i)  # adds the even number to the list
            else:  # number was odd
                i += 1
        return evenArray


myrange = MyRange(8)
print(myrange.next())