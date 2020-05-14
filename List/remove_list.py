

#remove list l2 from list l1

#use remove() function -- delete elemnt of l2 from l1

def removelist() :
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]

    l1.remove(l2[0])
    l1.remove(l2[1])

    return l1

l1 = removelist()
print (l1)

####### using for loop ######

def removeList() :
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]

    for ele in l2 :
        l1.remove(ele)

    print(l1)

removeList()