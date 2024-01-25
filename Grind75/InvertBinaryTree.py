# https://leetcode.com/problems/invert-binary-tree/description/

# Example of creating a BT:
# Input
# root = [4,2,7,1,3,6,9]
#        4
#      /   \
#     2     7
#    / \   / \
#   1   3 6   9

# Output
# root = [4,7,2,9,6,3,1]
#        4
#      /   \
#     7     2
#    / \   / \
#   9   6 3   1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)
    return root


def preorder_traversal(node):
    if node:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
preorder_traversal(root)

new_root = invertTree(root)

preorder_traversal(new_root)
