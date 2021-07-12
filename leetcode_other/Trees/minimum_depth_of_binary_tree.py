'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
    	## we start the total at 1 since the node itself is a min depth total of 1
        total = 1
        ## in the case there's no root node, just return 0 
        if (not root):
            return 0
        else:
            ## if there is a left and right node, return the minimum of the total between the two paths
            if (root.left != None and root.right != None):
                total = 1 + min(self.minDepth(root.left),self.minDepth(root.right))
            ## if there is only a left node, return the total on the left side
            elif (root.left != None):
                total = 1 + self.minDepth(root.left)
            ## if there is only a right node, return the total on the right side
            elif (root.right != None):
                total = 1 + self.minDepth(root.right)
        ## if the node doesn't have a left and right, return total
        return total