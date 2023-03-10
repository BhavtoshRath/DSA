class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)



root = BST(27)
root.insert(27)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
