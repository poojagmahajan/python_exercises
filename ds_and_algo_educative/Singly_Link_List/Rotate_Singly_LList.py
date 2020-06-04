
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def rotate(self, k):     # set pivot (k) here
        if self.head and self.head.next:
            p = self.head
            q = self.head

            while p and k>1:    ## k is 1 becoz, p and q already point to 1st node
                p = p.next      ## bring p , q to the pivot
                q = q.next
                k -=1
            #p=q                 ## store p (q is reused instead of new variable...as  p and q are same at pivot)

            while q.next:     ## stop at last node if take q here ...t will stop at null
                q = q.next

            q.next = self.head    ##  attach q to head
            self.head = p.next    ## node after pivot makes it head
            p.next = None          # make pivote points to none

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.rotate(4)
llist.print_list()