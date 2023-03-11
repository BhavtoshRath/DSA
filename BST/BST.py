class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        current = self
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = BST(data)
                    break
                else:
                    current = current.left
            else:
                if data > current.data:
                    if current.right is None:
                        current.right = BST(data)
                        break
                    else:
                        current = current.right
        return self

    def contains(self, data):
        current = self
        while current is not None:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return True
        return False

    def findminvalue(self):  # Find left-most node
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def findmaxvalue(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    def preorder(self, root):  # Traversal
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


root = BST(27)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

# root.preorder(root)
# root.contains(35)
print(root.findminvalue())