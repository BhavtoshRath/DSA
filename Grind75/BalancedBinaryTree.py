# https://leetcode.com/problems/balanced-binary-tree/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    # Recursive, bottom-up
    def isBalanced(self, root):
        def dfs(root):
            if root is None:
                return [True, 0]  # [isBalanced, Height_of_tree]
            left = dfs(root.left)
            right = dfs(root.right)
            isBalanced = left[0] is True and right[0] is True and abs(left[1]-right[1]) < 2
            
            return [isBalanced, 1+ max(left[1], right[1])]

        return dfs(root)[0]




