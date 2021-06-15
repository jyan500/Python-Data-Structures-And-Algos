'''
Given the root of a binary tree, invert the tree, and return its root.
https://leetcode.com/problems/invert-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if (root):
            ## swap the values of the left and right node
            tmp = root.left
            root.left = root.right
            root.right = tmp
            ## recursively run down the left side 
            self.invertTree(root.left)
            ## recursively run down the right side
            self.invertTree(root.right)
        ## once bottom of the tree is reached, return the root since all the nodes have been swapped at this point
        return root