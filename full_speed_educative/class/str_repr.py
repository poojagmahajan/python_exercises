

# to print class
# use str method or repr

class Rectangle :
    def __init__(self,x1,y1,x2,y2):
        if x1<x2 and y1>y2 :
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        else :
            print("incorrect cordinates of rectangle")

    def __str__(self):
        return ( str(self.x1) + ',' + str(self.y1) + ',' + str(self.x2) + ',' + str(self.y2))

    def __repr__(self):
        return (str(self.x1) + ',' + str(self.y1) + ',' + str(self.x2) + ',' + str(self.y2))


r =Rectangle(2,7,8,4)

print( r )
