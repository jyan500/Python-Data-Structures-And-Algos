'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
https://leetcode.com/problems/same-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ## base case #1: if the two roots are null, then they're same trees
        if (p == None and q == None):
            return True
        ## base case #2: if either p or q is null but not both, then they're not the same the tree
        elif (p == None or q == None):
            return False
        ## base case #3: if the values of p and q are not equal to each other, they're not the same tree
        elif (p.val != q.val):
            return False
        else:
            ## verify whether the left subtree of p and left subtree of q is equal to the
            ## right subtree of p and right subtree of q
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        
            