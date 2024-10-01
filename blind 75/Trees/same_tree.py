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

"""
Revisited on 9/30/2024
This is a similar logic to the first attempt,
but it splits into three different segments
if both nodes do not exist:
    return True
elif one node exists but not the other
    return False
else (if both nodes exist):
    if one node's value != the other node's value:
        return False
    # continue to compare the left subtrees and the right subtrees, if both sides remain True,
    # this means the parent tree is the same
    return recur(subtree1 left, subtree2 left) and recur(subtree1 right, subtree2 right)
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if neither node exists, we'd return true
        if not p and not q:
            return True
        # if one node exists in the tree and not the other, return False
        elif not p and q or p and not q:
            return False
        # if both nodes exist
        else:
            # if the values are not equal, return False
            if p.val != q.val:
                return False
            # continue to compare the left subtrees of p and q and the right subtrees of p and q
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        
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
            
        
            