
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        # Crucial when implementing the remove function
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        # We can access the root node exclusively
        self.root = None

    def insert(self, data):
        # First node in the BST
        if self.root is None:
            self.root = Node(data)
        # BST is not empty
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # Go to the left subtree
        if data < node.data:
            if node.left_node is not None:
                # Left node exists, so we keep going
                self.insert_node(data, node.left_node)
            else:
                # There is no left child, so we create one
                node.left_node = Node(data, node)
        else:
            if node.right_node is not None:
                # Right node exists, so we keep going
                self.insert_node(data, node.right_node)
            else:
                # There is no right child, so we create one
                node.right_node = Node(data, node)



