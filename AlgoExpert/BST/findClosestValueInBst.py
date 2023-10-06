class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree: Tree, target: int):
    return helper(tree, target, float("inf"))

def helper(tree, target,closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return helper(tree.left, target,closest)
    if target > tree.value:
        return helper(tree.right, target, closest)
    else:
        return closest


# Creating a Tree with seven inputs
root = Tree(25)
root.left = Tree(20)
root.right = Tree(35)
root.left.left = Tree(7)
root.left.right = Tree(22)
root.right.left = Tree(31)
root.right.right = Tree(40)

for i in range(0, 50):
    print(i, findClosestValueInBst(root, i))