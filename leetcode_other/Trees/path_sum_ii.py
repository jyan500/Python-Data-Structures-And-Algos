"""
https://leetcode.com/problems/path-sum-ii/

Key Concept:
1) perform an inorder traversal, where we keep track of a running amount and an array
that stores the nodes we've traversed so far 
(See LCA of binary tree for a similar traverse algorithm)

2) if we're at a leaf node, where there's no children, check to see if our running total
equals the target sum. If so, add the current path to our global variable
3) If we've checked both the left and right sides, we pop out the last element in our path
to backtrack to form a different path

Time Complexity: O(N)
Space Complexity: O(number of leaf nodes), since a path is from root to leaf node

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        def traverse(root, targetSum, amt, path):
            if root:
                path.append(root.val)
                amt += root.val
                if not root.left and not root.right:
                    if amt == targetSum:
                        self.paths.append(path.copy())
                traverse(root.left, targetSum, amt, path)
                traverse(root.right, targetSum, amt, path)
                path.pop(-1)         
                
        traverse(root, targetSum, 0, [])
        return self.paths
        