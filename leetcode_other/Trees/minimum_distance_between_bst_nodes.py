# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """
        O(N) Time and Space Complexity
        build inorder list which will be sorted because it's a BST, and then find the difference between each adjacent value,
        since in a sorted array, if we compare list[i] with list[i+1], there's no need to compare list[i] with list[i+2] for example,
        because the difference would always be greater
        """
        # self.list = []
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         self.list.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        # self.min = float("inf")
        # for i in range(1, len(self.list)):
        #     self.min = min(self.min, self.list[i]-self.list[i-1])
        # return self.min
        """
        O(N) Time and O(1) Space Complexity (Optimal by Neetcode)
        Recognizing that we can do only one full traversal through the tree is the key here,
        doing an inorder traversal allows us to visit the nodes in sorted order already, so technically don't need
        to put everything into an array first.
        
        We can keep a "prev" variable that points to the node we saw last, and then just compare our current value with our prev
        to find the min
        """
        self.min = float("inf")
        self.prev = None
        def inorder(root):
            if root:
                inorder(root.left)
                # the first time around, we'll get all the way to the left most child node, and then set prev because
                # there's no other node to compare to since it's a leaf node, so only prev = root.val happens
                # any subsequent time we examine the root node, we can then compare it with prev since prev will have a value
                if self.prev != None:    
                    self.min = min(root.val-self.prev, self.min)
                self.prev = root.val
                inorder(root.right)
        inorder(root)
        return self.min