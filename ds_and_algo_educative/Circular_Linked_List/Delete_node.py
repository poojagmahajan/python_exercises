
"""steps -
  1.  if List is not empty
   2.    if Deleting the head node
           set cur to head
           iterate till next of cur is head
               (means here cur is last node which points to head)
    3.            if head is only node in list means point to self
                    then make  head none
     4.           else (list having more nodes ,not just head)
                     head delete
                     and update new head to next node of old head
     5.   else (deleting node other than head)
            take two pointers cur and prev
            iterate till head
            update pointers prev and cur
            if key match
            then delete node and update cur """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, key):
        if self.head :  # List is not empty
            if self.head.data == key :  #node to be Delete is head node
                cur = self.head
                while cur.next != self.head :
                    cur = cur.next   # at end cur will be last node points to head
                if self.head == self.head.next :   #only one node in list
                    self.head = None
                else:                          # #head with other nodes preent in list
                    cur.next = self.head.next   #delete head
                    self.head = self.head.next   # make new head
            else:       # node to be delete is other than head
                cur = self.head
                prev = None
                while cur.next != self.head:  # traverse the list till end
                    prev = cur
                    cur = cur.next
                    if cur.data == key:   # if node match
                        prev.next = cur.next   #delete node
                        cur = cur.next


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")

cllist.remove("A")
cllist.remove("C")
cllist.print_list()