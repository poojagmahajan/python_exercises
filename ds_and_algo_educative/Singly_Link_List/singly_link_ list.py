

class Node :
    def __init__(self,data):   # create node
        self.data = data
        self.next = None

class LinkedList :          ##create list
    def __init__(self):
        self.head = None

    def printList(self):
        cur_node = self.head
        while cur_node :
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self,data):       ## The append method will insert an element at the end of the linked list
        new_node = Node(data)

        if self.head is None :     ## Empty Linked List Case
            self.head = new_node
            return

        last_node = self.head
        while last_node.next :     ## non empty linkedlist case
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):        ## insert an element at the beginning of the linked list
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,prev_node,data):
        if not prev_node :
            print("previous node is not exist")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.insert_after_node(llist.head.next, "D")

llist.printList()