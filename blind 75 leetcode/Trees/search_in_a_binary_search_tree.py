'''
https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Concept: 
since this is a binary search tree, we can apply binary search to find the element we want
in O(LogN) time
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            ## if val is greater than root, search right half
            if (val > root.val):
                return self.searchBST(root.right,val)
            ## if val is less than root, search left half
            elif (val < root.val):
                return self.searchBST(root.left,val)
            ## if val == root.val, we can just return the current root, which will contain the subtree
            else:
                return root