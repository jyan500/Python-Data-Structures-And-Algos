# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(N)
        Space: O(N)
        1) Preorder traversal, but only traverse down to the leaf node by checking whether the root.left exists or root.right exists.
            At each level of preorder traversal, if traversing down the left, you add the left root val, otherwise, add the right root val
        2) If we're at the leaf node (where root.left and root.right don't exist), append cur to a global array to store this path
        3) Once all paths are retrieved after the preorder traversal finishes, return the sum.
        """
        self.res = []
        def getPathNums(root, cur):
            if not root.left and not root.right:
                self.res.append(int(cur))
                return
            if root.left:
                getPathNums(root.left, cur + str(root.left.val))
            if root.right:
                getPathNums(root.right, cur + str(root.right.val))
        getPathNums(root, str(root.val))
        return sum(self.res)