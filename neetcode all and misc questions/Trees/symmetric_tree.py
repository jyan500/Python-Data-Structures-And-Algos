"""
First attempt:
invert one half of the tree, and then use same tree function,
checking if the left and right halves are the same after the inversion.
Since one side should be a mirror image of the other, after inverting one side,
it should be the same as the other

https://leetcode.com/problems/symmetric-tree/
O(2N) time
O(N) space - recursive calls 

Neetcode:
The optimal solution is quite similar to sameTree,
except you want to pass in root.left and root.right separately
and then in the recursive calls, you're checking whether the 
parent's left child == opposite side subtree's parent's right child, which are the outer nodes
and then the parent's right child == opposite child subtree's parent's left child, which are the inner nodes

O(N) time

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Revisited on 9/9/2025, I was trying to write a solution based on inorder traversal + checking
for a palindrome but it wasn't working out. So I had to revisit the optimal solution

Traverse down both halves both of the tree at once, but compare the left child of one half with the right child of the other half,
and then the right child of one half with the left child of the other half.
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False
            else:
                return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
        return isSameTree(root.left, root.right)

class Optimal:
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
		def sameTree(p, q):
	        if not p and not q:
	            return True
	        if not p or not q:
	            return False
	        if p.val != q.val:
	            return False
	        else:
	            return sameTree(p.left, q.right) and sameTree(p.right, q.left)
	    return sameTree(root.left, root.right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def invert(root):
            if root:
                root.left, root.right = root.right, root.left
                invert(root.left)
                invert(root.right)

        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            else:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        # invert one side of the tree, and then check if the two subtrees are the same
        invert(root.left)
        return sameTree(root.left, root.right)