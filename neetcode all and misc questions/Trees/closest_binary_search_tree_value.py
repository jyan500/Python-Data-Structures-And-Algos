from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        """
        https://www.lintcode.com/problem/closest-binary-search-tree-value/description
        since this is a BST, we can get in order traversal first, 
        to retrieve a sorted list, and then figure out the closest value

        Time: O(N)
        Space: O(N)
        """
        self.inorder = []
        def search(node):
            if node:
                search(node.left)
                self.inorder.append(node.val)
                search(node.right)
                        
        search(root)
        for i in range(len(self.inorder)-1):
            if target == self.inorder[i]:
                return self.inorder[i]
            # if the target is in between two values, we calculate the distances between 
            # the target and the current value, and the target and the next value
            # and then pick the number that gives a smaller distance
            if self.inorder[i] < target < self.inorder[i+1]:
                distance1 = abs(target - self.inorder[i])
                distance2 = abs(target - self.inorder[i+1])
                if distance1 < distance2:
                    return self.inorder[i]
                else:
                    return self.inorder[i+1]
        # if we go to the end of the list without triggering any of the conditions above, 
        # that means the value closest to the target is the last value in the list
        return self.inorder[-1]