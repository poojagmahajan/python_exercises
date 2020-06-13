
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

    def height( self, node ):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


# Calculate height of binary tree:
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

print(tree.height(tree.root))