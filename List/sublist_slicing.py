

list = [1,2,3,4,5]

print(list[0:3])

print(list[3:6])  #excluding 6th

print([1,3,4,5] +  [6,7,8,9,10])  # concatenation

for val in list :   # transeverse list element by element
     print(val)


#Given a getSublist() function, create a list named l [1, 4, 9, 10, 23]. Using list slicing,
# get the sublists [1, 4, 9] and [10, 23].

def getSublist(l) :
    print (l[0:3])
    print(l[4:6])

getSublist([1, 4, 9, 10, 23])


