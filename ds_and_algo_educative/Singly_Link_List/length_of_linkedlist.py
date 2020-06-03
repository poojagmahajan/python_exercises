
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

    def len_iterative(self) :   # length by iterative method
        count = 0
        cur_node = self.head
        while cur_node :
            count +=1
            cur_node = cur_node.next
        return count

    def len_recursive(self,node):
        if node is None :
            return 0
        return 1 + self.len_recursive(node.next)


llist = LinkedList()
print("The length of an empty linked list is:")
print(llist.len_recursive(llist.head))
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("The length of the linked list calculated recursively after inserting 4 elements is:")
print(llist.len_recursive(llist.head))
print("The length of the linked list calculated iteratively after inserting 4 elements is:")
print(llist.len_iterative())
