class Stack(object):
    def __init__( self ):
        self.items = []

    def __len__( self ):
        return self.size()

    def size( self ):
        return len(self.items)

    def push( self, item ):
        self.items.append(item)

    def pop( self ):
        if not self.is_empty():
            return self.items.pop()

    def peek( self ):
        if not self.is_empty():
            return self.items[-1]

    def is_empty( self ):
        return len(self.items) == 0

    def __str__( self ):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s


class Queue(object):
    def __init__( self ):
        self.items = []

    def __len__( self ):
        return self.size()

    def enqueue( self, item ):
        self.items.insert(0, item)

    def dequeue( self ):
        if not self.is_empty():
            return self.items.pop()

    def size( self ):
        return len(self.items)

    def is_empty( self ):
        return len(self.items) == 0

    def peek( self ):
        if not self.is_empty():
            return self.items[-1].value


class Node(object):
    def __init__( self, value ):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__( self, root ):
        self.root = Node(root)

    def search( self, find_val, traversal_type ):
        if traversal_type == "preorder":
            return self.preorder_search(tree.root, find_val)
        elif traversal_type == "inorder":
            return self.inorder_search(tree.root, find_val)
        elif traversal_type == "postorder":
            return self.postorder_search(tree.root, find_val)
        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    def print_tree( self, traversal_type ):
        # Recursive traversals
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        # Iterative traversals
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "inorder_iterative":
            return self.inorder_iterative(tree.root)
        elif traversal_type == "preorder_iterative":
            return self.preorder_iterative(tree.root)
        elif traversal_type == "postorder_iterative":
            return self.postorder_iterative(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    def size_( self, node ):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

    def size( self ):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size


# Calculate size of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
#
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size())
print(tree.size_(tree.root))
