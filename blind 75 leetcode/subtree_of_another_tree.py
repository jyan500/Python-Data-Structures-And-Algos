'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Runtime: O(N * M), where N is the number of nodes in root, and M is the number of nodes in subroot
Space: Min(N, M), because the recursion is determined by the tree that has less nodes
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    	## if the root is null, then this cannot be a subroot
    	if (root == None):
    		return False
        ## for each call, check if the sameTree function passes, if it continues
        ## to return True at each level of the tree, then subroot has been found
    	elif (self.isSameTree(root, subRoot)):
    		return True
        ## if false, then continue down the left and then the right
    	else:
    		return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
   	
   	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ## base case #1: if the two roots are null, then they're same trees
        if (p == None and q == None):
            return True
        ## base case #2: if either p or q is null but not both, then they're not the same the tree
        elif (p == None or q == None):
            return False
        ## base case #3: if the values of p and q are not equal to each other, they're not the same tree
        elif (p.val != q.val):
            return False
        else:
            ## verify whether the left subtree of p and left subtree of q is equal to the
            ## right subtree of p and right subtree of q
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 