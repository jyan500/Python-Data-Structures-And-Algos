'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

https://www.youtube.com/watch?v=kulWKd3BUcI&ab_channel=KevinNaughtonJr.KevinNaughtonJr.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## the idea is that we search continuously either the left or right subtree for both p and q
## if the values of p and q are both less than the root, then we know we haven't found the 
## lowest common ancestor yet
## however, once p and q are no longer on the same side of the tree (which means they have split, i.e either p is greater than root, but q is not greater), then the root is the lowest common ancestor

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root