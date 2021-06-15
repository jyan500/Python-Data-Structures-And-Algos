'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Explanation:
https://www.youtube.com/watch?v=ihj4IQGZ2zc&ab_channel=NeetCodeNeetCode

Basic Concept:
the preorder will provide us the root of the tree at each level, and the inorder tells us what should
go in the left subtree and right subtree

definitions
preorder: visit root, visit left, visit right
inorder: visit left, visit root, visit right

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root