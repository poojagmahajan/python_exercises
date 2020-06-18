
# namedtuple which you can use to replace Python’s tuple.

from collections import namedtuple

Point = namedtuple('Point','x,y')   # this will create class name point with x and y
pt = Point(1,-4)
print(pt)
print(pt.x ,pt.y)




