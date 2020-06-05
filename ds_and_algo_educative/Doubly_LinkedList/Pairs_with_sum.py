
'''  In this exercise, you are required to find pairs from a doubly linked list which sum to a specified number.
e.g  Find pairs which sum up to 5.
 ans  (1,4)(2,3)

'''

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__ (self):
        self.head = None

    def append (self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def print_list (self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def pairs_with_sum (self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(dllist.pairs_with_sum(5))