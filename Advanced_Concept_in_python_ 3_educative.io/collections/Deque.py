
'''deques “are a generalization of stacks and queues”.
They are pronounced “deck” which is short for "double-ended queue'''

from  collections import  deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print (d)

d.pop()
d.popleft()
print(d)

d.clear()
print(d)

d.extend([1,2,3])
d.extendleft([4,5,6])
print(d)

d.rotate(1)   # rotate by 1 to right
d.rotate(2)
d.rotate(-1)  # roatate by 1 to left
print(d)

###############

from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)

d.append('bork')
print (d)
d.appendleft('test')
print (d)

