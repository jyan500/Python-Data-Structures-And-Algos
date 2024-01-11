'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Slightly different solution, revisited on 7/17/2023
O(N) time, O(1) space
track a depth variable and continually increment it until the root is none,
then return it in the base case
continually take the max between the depths found on the left and right subtrees
"""
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root, 0)
    def maxDepthHelper(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        else:
            return max(self.maxDepthHelper(root.left, depth + 1), self.maxDepthHelper(root.right, depth + 1))

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if (root is None):
            return 0
        else:
            a = self.maxDepth(root.left)
            b = self.maxDepth(root.right)
            return max(a, b) + 1