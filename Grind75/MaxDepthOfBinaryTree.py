# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):  # Sol 1: Recursive
    if not root:
        return 0
    else:
        return 1 + max(max_depth(root.left), max_depth(root.right))


from collections import deque
def max_depth1(root):
    if not root:
        return 0
    level = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

max_depth1(root)
# print(max_depth1(root))