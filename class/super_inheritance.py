
# use of super() function
    # ParentClassName.__init__(self, methodParameter)
    #ParentClassName.methodName(self, methodParameter)

# with super() function
    #super().methodName(args)


# The coordinates and the length of the square
# Area of the square


class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # class constructor
        self.x1 = x1  # class variable
        self.y1 = y1  # class variable
        self.x2 = x2  # class variable
        self.y2 = y2  # class variable

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def area(self):
        return self.width() * self.height()


# write your code here
class Square(Rectangle):
    def __init__(self, x1, y1, length):
        x2 = x1 + length
        y2 = y1 + length
        super().__init__(x1, y1, x2, y2)


# test your code here
square = Square(2, 7, 7)
print("Length: " + str(square.width()) + ", Area: " + str(square.area()))
square2 = Square(1, 3, 5)
print("Length: " + str(square2.width()) + ", Area: " + str(square2.area()))