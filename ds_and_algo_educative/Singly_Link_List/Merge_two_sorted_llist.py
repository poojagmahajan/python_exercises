

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

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None

        if not p:         ## If p is empty
            return q
        if not q:         ## if q is empty
            return p

        if p and q:       # if both p and q are not empty
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s   # new_head will be address of the smallest value
        while p and q:     ## iterate till p and q will null
            if p.data <= q.data:
                s.next = p   # Linked p(smallest) to list s
                s = p        # Move s to p
                p = s.next   # move p to next node
            else:
                s.next = q
                s = q
                q = s.next
        if not p:             # if p reaches to null
            s.next = q
        if not q:             #if q reaches to null
            s.next = p
        return new_head   ## as previous assignment new_head = s


llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()