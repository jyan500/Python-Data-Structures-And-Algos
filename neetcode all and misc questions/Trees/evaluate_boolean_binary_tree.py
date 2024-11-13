# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        postorder traversal (left, right, root)
        O(N)
        if we're not at a leaf node yet,
            if the current node is 2, this is "OR" statement,
                so continue recurring down Left, right sides, but
                evaluate the return results of each with OR
            if the current is 3, this is "AND" statement,
                same as above, but evaluate return results with AND
        if we're at a leaf node,
            we return True if the node value is 1, otherwise return False
            
        """
        if (root):
            if (root.left and root.right):
                if root.val == 2:
                    return self.evaluateTree(root.left) or self.evaluateTree(root.right)
                if root.val == 3:
                    return self.evaluateTree(root.left) and self.evaluateTree(root.right)
            return True if root.val == 1 else False
        return True
        