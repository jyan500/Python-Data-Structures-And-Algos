# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Revisited 5/23/2025
        https://leetcode.com/problems/range-sum-of-bst/
        O(N) at worst, because the every value could be between low and high,
        meaning you'd traverse the whole tree
        
        Given it's a binary search tree, we can figure out if 
        which side to iterate based on the current root, so we can
        avoid iterating un-necessarily on one side of the tree since
        we're only interested in nodes where the val meets the following condition:
        low <= val <= high
        
        in that case, we return the current root value + the results of 
        searching right and searching left (since we could go either way in this case)
        
        if root < low and root < high:
            search right
        if root > low and root > high:
            search left
        else:
            return root val + search right + search left 
        """
        
        if root:
            if root.val < low and root.val < high:
                return self.rangeSumBST(root.right, low, high)
            elif root.val > low and root.val > high:
                return self.rangeSumBST(root.left, low, high)
            else:
                return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        return 0
    