

## Iterative method


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

    def reverse_iterative(self):

        prev = None
        cur = self.head

        while cur :
            nxt = cur.next   # assign nxt
            cur.next = prev   # assign prev to cur.next means cur('A') becomes none as prev = none.so 'A' os disconect from remain link

            prev=cur   # move pointers - prev becomes cur (prev is Node A)
            cur=nxt    # move pointer cur - cur becomes nxt means cur is now (node B) nxt also (node B)

        self.head = prev ## at end of loop node 'D' is prev

## Recursive method

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):   # helper method
            if not cur:   # LList with single node(having cur is none)
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

#llist.reverse_iterative()
llist.reverse_recursive()

llist.print_list()