

#### print numbers from n down to 0


class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        myArray = []
        for i in range(self.n, -1, -1): # from n to 0
            myArray.append(i) # adds the even number to the list
        return myArray

myRange = MyRange(8)
print(myRange.next())