# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert node (simple BST insert)
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    # Traversals
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

# Driver code
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    print("Inorder Traversal:")
    tree.inorder(tree.root)   # Output: 20 30 40 50 60 70 80

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)  # Output: 50 30 20 40 70 60 80

    print("\nPostorder Traversal:")
    tree.postorder(tree.root) # Output: 20 40 30 60 80 70 50
