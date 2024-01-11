'''
Given a Binary Tree, convert it to a Circular Doubly Linked List (In-Place).  

The left and right pointers in nodes are to be used as previous and next pointers respectively in converted Circular Linked List.
The order of nodes in the List must be the same as in Inorder for the given Binary Tree.
The first node of Inorder traversal must be the head node of the Circular List.

https://www.geeksforgeeks.org/convert-a-binary-tree-to-a-circular-doubly-link-list/
(I think this question is also on leetcode premium)

'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def convertTree(self, root):
		