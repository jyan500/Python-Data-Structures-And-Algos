"""
https://leetcode.com/problems/balanced-binary-tree/
https://www.youtube.com/watch?v=QfJsau0ItOY&ab_channel=NeetCode

A height balanced binary tree is a binary tree in which 
the height of the left subtree and right subtree of any node does not differ by more than 1 
and both the left and right subtree are also height balanced.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Optimal Solution (Neetcode):
Save repeated work by determining the height AND whether the subtree is balanced
in the same recursive call

In each recursive call, return both the height, as well as whether the subtree is balanced
"""
"""
Revisited on 4/7/2025
Revisited on 9/30/2024
same solution as below
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def getHeight(root):
            if (root):
                leftHeight = getHeight(root.left)
                rightHeight = getHeight(root.right)
                if abs(leftHeight-rightHeight) > 1:
                    self.isBalanced = False
                return 1 + max(leftHeight, rightHeight)
            return 0
                
        getHeight(root)
        return self.isBalanced

""" 
    10/23 even simpler solution with the same concept, determine the balancing AS we calculate the 
    height of the tree. if we ever reach a point where
    the tree is unbalanced, just set a global var to false.
"""
class Solution3:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def height(root):
            if root:
                leftHeight = height(root.left)
                rightHeight = height(root.right)
                if abs(leftHeight - rightHeight) > 1:
                    self.isBalanced = False
                return 1 + max(leftHeight, rightHeight)
            return 0
        height(root)
        return self.isBalanced

class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, height):
            # in the base case, we can assume this is a balanced tree
            # and that the height of the root is 0
            if not root:
                return [True, height]

            # go down left subtree and right subtree, and then visit the root, essentially
            # doing a post order traversal
            left, right = dfs(root.left, height+1), dfs(root.right,height+1)
            isBalancedLeft, heightLeft = left
            isBalancedRight, heightRight = right
            # store whether the difference between the heights of the left and right subtrees is <= 1 and 
            # whether the left and right subtrees are also height balanced
            isBalancedSubtree = abs(heightLeft - heightRight) <= 1 and isBalancedLeft and isBalancedRight

            # return both the height of this subtree and whether this subtree is balanced
            return [isBalancedSubtree, max(heightLeft, heightRight)]

        isBalancedSubtree = dfs(root)[0]
        return isBalancedSubtree



"""
Brute Force Solution:
for each node, go through each subtree to determine whether the left and right subtree's height 
will not differ by more than 1
Time Complexity:
O(N^2), for each node, go through each subtree
Space Complexity:
O(N) for recursive calls
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def findMaxHeight(root, height):
            if not root:
                return 0 
            leftHeight = findMaxHeight(root.left)
            rightHeight = findMaxHeight(root.right)
            return 1 + max(leftHeight, rightHeight)
        # an empty tree is considered balanced since the left and right subtree heights are both 0,
        # so no difference
        if not root:
            return True
        leftHeight = findMaxHeight(root.left)
        rightHeight = findMaxHeight(root.right)
        # if the difference in height between the left and right subtree is less than 1
        # and the left and right subtree are also height balanced, return true
        return abs(rightHeight - leftHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)