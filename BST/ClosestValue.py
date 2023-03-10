class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

t_10 = BST(10)
t_5a = BST(5)
t_5b = BST(5)
t_15 = BST(15)
t_2 = BST(2)
t_13 = BST(13)
t_22 = BST(22)
t_1 = BST(1)
t_14 = BST(14)
t_10.left = t_5a
t_10.right = t_15
t_5a.left = t_2
t_5a.right = t_5b
t_15.left = t_13
t_15.right = t_22
t_2.left = t_1
t_13.right = t_14
print('x')

d = {}
def findClosestValueInBst(tree, target):
    while tree:
        if tree.left:
            # tree = tree.left
            findClosestValueInBst(tree.left, target)
        d[abs(tree.value - target)] = tree.value
        if tree.right:
            findClosestValueInBst(tree.right, target)
    return d[min(list(d.keys()))]


x = findClosestValueInBst(t_10, 12)
print('x')