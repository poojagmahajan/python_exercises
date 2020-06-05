

'''  case 1 : delete head node where only node present present( head )
     case 2 : delete head node where more than 1 node present

     case 3 : Deleting node other than head where cur.next is not None (node inbetween two nodes)
     case 4 : Deleting node other than head where cur.next is None (Last node to be delete)
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
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

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2:
                else:
                    nxt = cur.next  # here cur is 'A' in (A -> B)
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete(1)
dllist.delete(6)
dllist.delete(4)

dllist.delete(3)
dllist.print_list()