

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

    def move_tail_to_head(self):
        if self.head and self.head.next:
            cur = self.head
            prev = None

            while cur.next :
                prev = cur
                cur = cur.next

            cur.next =self.head
            prev.next = None
            self.head = cur

# input  A -> B -> C -> D -> Null
#output  D -> A -> B -> C -> Null
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()
llist.move_tail_to_head()
print("\n")
llist.print_list()