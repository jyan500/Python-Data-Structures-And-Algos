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

// Tried this problem again on 7/22/2021
the key insight was that for the inorder traversal, items to the left of our node contain the left subtree, and items to the right of our node contain the right subtree. 
        
after watching neetcode's video, the flaw in my thinking was that I was only looking for how to find 
the current's node left and right children, rather than looking at it from an entire left and right subtree perspective

For example looking at preorder1 and inorder1's values:

3 will always be the root of the tree
looking at 3 within the inorder1 list, nodes on the left are the left subtree of 3, nodes to the right are the right subtree. 

We can define this index where 3 is located as "m", and then partition our inorder and preorder lists
into left and right halves, and pass those into recursive calls to further build the left and right subtrees.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## Neetcode's solution
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    ## own solution based off of neetcode
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, inorder)

    def helper(self, preorder: List[int], inorder: List[int]):
        ## note that if the preorder list is empty
        ## that means our current node has no children, so we just return None
        if (len(preorder) == 0 or len(inorder) == 0):
            return
        m = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        ## for our left half, recursively call self.helper on the left subtree section of the preorder list
        ## (Everything from the first element (not including the root) to the end of the left subtree section m+1)
        ## as well as the left half of the inorder list (everything up to and including the index of current root)
        root.left = self.helper(preorder[1:m+1],inorder[:m])
        
        ## for our right half, recursively call self.helper on the left subtree section of the preorder list
        ## as well as the right half of the inorder list (everything beyond the index of current root)
        root.right = self.helper(preorder[m+1:],inorder[m+1:])
        
        ## by the end, we would've recursively built both left and right subtrees in our root.left and root.right
        ## so we can just return the root at the end
        return root
