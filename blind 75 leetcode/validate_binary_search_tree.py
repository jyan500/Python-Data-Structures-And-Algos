'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)
    def validate(self, root, min_val, max_val) -> bool:
        if (not root):
            return True
        elif (min_val != None and root.val <= min_val or max_val != None and root.val >= max_val):
            return False
        else:
            ## pass in root.val for max on the left subtree
            ## to check that the left subtree's nodes are less than that max
            ## pass in root.val for min on the right subtree
            ## since the right subtree's nodes must always be greater than that min
            return self.validate(root.left, min_val, root.val) and self.validate(root.right, root.val, max_val)