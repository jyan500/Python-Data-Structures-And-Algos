'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

https://www.youtube.com/watch?v=6cA_NDtpyz8&ab_channel=MichaelMuinos
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_val = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        self.postOrder(root)
        return self.max_val
    def postOrder(self, root: TreeNode) -> int:
        if (not root):
            return 0
        ## the value that is returned must always be greater than zero, otherwise it will subtract from the total max
        left = max(0, self.postOrder(root.left))
        right = max(0, self.postOrder(root.right))
        self.max_val = max(self.max_val, left + right + root.val)
        ## the max(left, right) only takes either the left or right since it can only take one path
        return max(left, right) + root.val
        
        
        