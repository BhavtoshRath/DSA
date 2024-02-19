# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


def max_depth(root):  # Sol 1: Recursive
    if not root:
        return 0
    else:
        return 1 + max(max_depth(root.left), max_depth(root.right))