

# Polimorphism using method
# def - poly - many ,morf - forms
# means same name in many forms(different tasks)
# here we have method name getArea() - for two diff classes
# this will have same name but it will calculate area of Rectangle(first class) and area of circle (2nd class)


class Rectangle():

    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area2
    def getArea(self):
        return (self.width * self.height)


class Circle():
    # initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
