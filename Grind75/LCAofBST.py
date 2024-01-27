# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# https://www.youtube.com/watch?v=gs2LMfuOR9k&ab_channel=NeetCode
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  # Time complexity: O(logN), Space complexity: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr


# Logic: If both p and q are less than root, go to left sub tree,
# If both p and q are greater than root, go to right sub tree
# Else, root is the LCA