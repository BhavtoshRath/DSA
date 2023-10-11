# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sum_l = []
    helper(root, 0, sum_l)
    return sum_l


def helper(node, runningSum, sum_l):
    if node is None: # To handle condition where node.left/node.right in line 23/24 are None
        return None
    runningSum += node.value
    if node.left is None and node.right is None:
        # stopping condition, when you are certain that sum for 1 branch is complete
        sum_l.append(runningSum)

    helper(node.left, runningSum, sum_l)  # Rec
    helper(node.right, runningSum, sum_l)  # Rec


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right.left = BinaryTree(10)

print(branchSums(root))
