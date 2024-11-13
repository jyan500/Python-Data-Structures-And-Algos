# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        inorder traversal
        - visit left, visit right then the node
        
        using extra memory,
        visit the leaf nodes of both trees and store in array
        compare the two arrays in sequence
        
        O(2N) time 
        O(2N) space

        https://leetcode.com/problems/leaf-similar-trees/
        """
        def inorder(root, leafNodes):
            # store only the leaf nodes specifically
            if root:
                # if there is no left and no right, this is a leaf node
                if not root.left and not root.right:
                    leafNodes.append(root.val)
                else:
                    inorder(root.left, leafNodes)
                    inorder(root.right, leafNodes)
        
        root1Leaves = []
        root2Leaves = []
        inorder(root1, root1Leaves)
        inorder(root2, root2Leaves)
        return root1Leaves == root2Leaves
