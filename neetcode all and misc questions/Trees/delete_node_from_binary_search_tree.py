# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    	# Approach:
        # put all nodes into a sorted list via inorder traversal, excluding the node we want to delete
        # and then reconstruct it.
        # In the array representation of the inorder traversal, the root of the subtree
        # is always the mid point, so the left subtree is everything to the left of mid, and 
        # the right subtree is everything to the right of mid
        # (Note that it may be possible to do this problem by removing the node and bubbling up the proper node to become
        # the new root, but I decided to take this more straight forward approach instead)
        # revisited on 11/14/2024 with the same solution
        # Time: O(N) 
        # Space: O(N) 
        self.l = []
        def inOrder(root, key):
            if root:
                inOrder(root.left, key)
                if root.val != key:
                    self.l.append(root.val)
                inOrder(root.right, key)
        inOrder(root, key)
        def reconstruct(l):
            if len(l) > 0:
                mid = len(l)//2
                left = reconstruct(l[:mid])
                right = reconstruct(l[mid+1:])
                return TreeNode(l[mid], left, right)
        return reconstruct(self.l)