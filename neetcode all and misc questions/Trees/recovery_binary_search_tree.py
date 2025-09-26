# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        https://www.youtube.com/watch?v=bJBwOMPhe6Y&ab_channel=TimothyHChang
        Brute Force
        1 3 2 4 -> 1 2 3 4
        you could get an inorder traversal and then sort it, and then set the values
        this would be O(NLogN) time and O(N) space

        There's a more complicated solution but it seems un-reasonable to come up with in an interview setting
       
        """
        self.temp = []
        def inorder(node):
            if node:
                inorder(node.left)
                self.temp.append(node)
                inorder(node.right)
        inorder(root)
        # sort the nodes by the value
        sortedValues = sorted([n.val for n in self.temp])
        # overwrite the values of the original nodes with the sorted values
        # without changing the structure of the nodes
        for i in range(len(sortedValues)):
            self.temp[i].val = sortedValues[i]

