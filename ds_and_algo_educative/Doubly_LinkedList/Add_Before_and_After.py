

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

  def prepend(self, data):
    if self.head is None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    else:
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

  def add_after_node(self, key, data):
    cur = self.head
    while cur:
      if cur.next is None and cur.data == key:  ## if have to insert as a last node then append
        self.append(data)
        return
      elif cur.data == key:          ## for add node after any node  
        new_node = Node(data)
        nxt = cur.next
        cur.next = new_node
        new_node.next = nxt
        new_node.prev = cur
        nxt.prev = new_node
        return
      cur = cur.next

  def add_before_node(self, key, data):
    cur = self.head
    while cur:
      if cur.prev is None and cur.data == key:  # if node add before head then call prepend
        self.prepend(data)
        return
      elif cur.data == key:  # add node before any node
        new_node = Node(data)
        prev = cur.prev
        prev.next = new_node
        cur.prev = new_node
        new_node.next = cur
        new_node.prev = prev
        return
      cur = cur.next

  def print_list(self):
    cur = self.head
    while cur:
      print(cur.data)
      cur = cur.next


dllist = DoublyLinkedList()

dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.add_after_node(3,6)
dllist.add_before_node(4,9)

dllist.print_list()