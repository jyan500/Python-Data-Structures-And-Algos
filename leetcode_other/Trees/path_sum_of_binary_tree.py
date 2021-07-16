'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

https://leetcode.com/problems/path-sum/

Approach: create a helper function to keep track of running total
Since we want to check for leaf nodes, we want to make sure that the root.left and root.right are not None
before we continuing traversing, so we also want to make sure to only traverse down paths
that have root values. When traversing through, pass along the sum so far

Once we reach a leaf, we just need to check if the sum that we just calculated in this recursive call
is equal to the targetSum

Time Complexity: O(N), because there's a possibility that we will visit every node to find the possible path sum
Space Complexity: O(H), where H is the height of the tree, for H amount of possible recursive calls

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        ## base case to check for empty tree
        if (not root):
            return False
        else:
            return self.search(root, targetSum, 0)
        
    def search(self, root, targetSum: int, total: int)->bool:
        val = total + root.val
        if (root.left != None and root.right != None):
            return self.search(root.left, targetSum, val) or self.search(root.right, targetSum, val)
        elif (root.left != None):
            return self.search(root.left,targetSum, val)
        elif (root.right != None):
            return self.search(root.right,targetSum, val)
        else:
            return val == targetSum