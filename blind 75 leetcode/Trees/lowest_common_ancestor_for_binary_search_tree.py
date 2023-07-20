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

"""
Revisited on 7/20/2023, coming up with the same solution
OLogN time because it's a binary search tree
Key Concepts:
the lowest common ancestor in the binary search tree is the moment when p and q are no longer on the same
subtree, meaning either p >= root and q <= root OR p <= root and q >= root. In that case,
the root has to be the lowest common ancestor, since in a BST, all values to the right of root
are going to be greater, and all values on the left will always be less.

"""
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # this could just be an else statement like below, but for explanation purposes,
        # but clearer for learning purposes
        if p.val >= root.val and q.val <= root.val or p.val <= root.val and q.val >= root.val:
            return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root