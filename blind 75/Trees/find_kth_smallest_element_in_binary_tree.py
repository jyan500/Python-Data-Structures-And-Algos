'''
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

https://www.youtube.com/watch?v=C6r1fDKAW_o

Time complexity: O(N), because we traverse all the elements potentially if we had to find the largest element, or if the tree was just a linked list
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Revisited on 7/22/2023
This is similar to the solution below except it uses global variables instead of 
passing in an array as a param that gets updated through the recursive calls

Key concept:
traversing all the way to the left most child, because this is a BST
this will be the smallest value in the tree. We can use inorder to traverse
the values in sorted order

start decrementing k at each node afterwards, and see if k == 0, which means
we're at the k element

If so, this is the value we're looking for so set it (either in global variable,
or via an array like the first solution)
"""
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        self.res = 0
        self.k = k
        def kthSmallestHelper(root: Optional[TreeNode]):
            if not root:
                return
            kthSmallestHelper(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            kthSmallestHelper(root.right)
        
        kthSmallestHelper(root)
        return self.res

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ## keep track of a nums array where nums[0] contains the current (index + 1) that we're on
        ## nums[1] will contain the value that we want to return, which is the kth smallest element
        nums = [0, 0]
        self.inorder(root, nums, k)
        return nums[1]
    def inorder(self, root, nums, k):
        ## we use a regular inorder traversal since this is a binary search tree where all the nodes
        ## in the left subtree are smaller than the root, and all the nodes in the right subtree are larger than the root
        ## inorder will allow us to visit the smallest values first on the left side
        if (root == None):
            return 
        self.inorder(root.left, nums, k)
        ## we will increment nums[0] by 1 to show that we are at the kth element so far (indexing by 1 rather than at 0)
        nums[0] += 1
        ## once we hit the correct k value, we will return the root's value
        if (nums[0] == k):
            nums[1] = root.val
            return
        ## if we did not get the right k value yet, continue the recursion to the right side of the tree
        self.inorder(root.right, nums, k)