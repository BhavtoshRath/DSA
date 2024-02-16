# https://leetcode.com/problems/diameter-of-binary-tree/description/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diameter_of_binary_tree(root):
    def dfs(node):
        if not node:
            return 0, 0  # depth, diameter

        left_depth, left_diameter = dfs(node.left)
        right_depth, right_diameter = dfs(node.right)

        current_diameter = left_depth + right_depth
        max_diameter = max(left_diameter, right_diameter, current_diameter)

        return max(left_depth, right_depth) + 1, max_diameter

    _, diameter = dfs(root)
    return diameter


# Example usage:
# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter of the binary tree:", diameter_of_binary_tree(root))
