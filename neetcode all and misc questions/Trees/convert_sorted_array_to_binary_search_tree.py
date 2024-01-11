"""
O(N) time
O(N) recursive calls space
Key concept:
1) because it's a sorted array, we can see that the middle element is the root of the tree,
and the left subtree is all elements to the left that are less than the root,
and the right subtree is all elements to the right that are greater than the root
2) We can recursively pass in the elements to the left of mid, and the elements to the right of mid

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:      
            left = 0
            right = len(nums)-1
            mid = left + (right - left) // 2
            leftSubtree = self.sortedArrayToBST(nums[0:mid])
            rightSubtree = self.sortedArrayToBST(nums[mid+1:])
            root = TreeNode(nums[mid], left = leftSubtree, right = rightSubtree)
            return root
