# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Key Concept:
1) Because we're given a BST, we can use binary search to figure out the proper insertion spot.
2) If the given value is less than our root, we search the left subtree. If it's greater,
we search the right subtree
3) When we find the spot where we need to go left, but the root doesn't have a left child, this is where we'll insert.
Same if it's on the right side

Time Complexity:
O(LogN) to find out the proper insertion spot via binary search since this is a BST
"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        def insert(root, val):
            if root:
                # if val is less than root val, it goes on the left
                if val < root.val:
                    if root.left:
                        insert(root.left, val)
                	# if there's no left child, this is where we'll insert
                    else:
                        root.left = TreeNode(val, None, None)  
                # if val is greater than root val, it goes on the right
                if val > root.val:
                    if root.right:      
                        insert(root.right, val)
                	# if there's no right child, this is where we'll insert
                    else:
                        root.right = TreeNode(val, None, None)     
        insert(root, val)
        return root
                
                