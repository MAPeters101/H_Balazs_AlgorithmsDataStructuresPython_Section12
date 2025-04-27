
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

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        # First node in the BST
        if self.root is None:
            self.root = Node(data)
        # BST is not empty
        else:
            self.insert_node(data, self.root)

    def remove_node(self, data, node):
        # First we have to find the node we want to remove
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # We found the node we want to remove
            # There are 3 options
            # LEAF NODE CASE
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

            # WHEN THERE IS A SINGLE CHILD
            elif node.left_node is None and node.right_node is not None:  # node !!!
                print("Removing a node with single right child...%d" % node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = None

                node.right_node.parent = parent
                del node



    def insert_node(self, data, node):
        # Go to the left subtree
        if data < node.data:
            if node.left_node is not None:
                # Left node exists, so we keep going
                self.insert_node(data, node.left_node)
            else:
                # There is no left child, so we create one
                node.left_node = Node(data, node)
        # We have to go to the right subtree
        else:
            if node.right_node is not None:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    def get_min(self):
        if self.root is not None:
            return self.get_min_value(self.root)

    def get_min_value(self, node):

        if node.left_node:
            return self.get_min_value(node.left_node)

        return node.data

    def get_max(self):
        if self.root is not None:
            return self.get_max_value(self.root)

    def get_max_value(self, node):

        if node.right_node:
            return self.get_max_value(node.right_node)

        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    # O(N) linear running time
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(12)
    bst.insert(-5)
    bst.insert(44)
    bst.insert(-12)
    bst.insert(19)
    bst.insert(22)

    bst.traverse()
    print()
    print('Min value: %s' % bst.get_min())
    print('Max value: %s' % bst.get_max())

