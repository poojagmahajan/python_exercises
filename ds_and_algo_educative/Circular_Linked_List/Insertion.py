
## Append      - insert node at last
## print_list  - print list
## prepend     - isert node at start as a head

class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        if not self.head :   ## if List is empty then make new node as head
            self.head = Node(data)
            self.head.next = self.head   ## Due to circularList head node poits to itself

        else :
            new_node = Node(data)

            cur = self.head
            while cur.next != self. head :
                cur = cur.next
            cur.next = new_node     # append new node at last of list
            new_node.next = self.head   # point new node to head ,to make list as circular

    def print_list(self):
        cur = self.head
        while cur :
            print(cur.data)
            cur = cur.next
            if cur == self.head :
                break

    def prepend(self,data):
         new_node = Node(data)

         if not self.head :
             new_node.next = new_node  #  point to itself to make it circular

         else:
             cur = self.head
             while cur.next != self.head :
                 cur  =cur.next
             cur.next = new_node
             new_node.next = self.head
             self.head = new_node   # this is diff between append and prepend...
             # here new node is head and in append next of new node is head

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()