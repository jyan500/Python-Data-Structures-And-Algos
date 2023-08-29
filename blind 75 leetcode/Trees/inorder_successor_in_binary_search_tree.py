"""
https://www.lintcode.com/problem/448/
https://www.youtube.com/watch?v=vo794ruCJnU&ab_channel=CrackingFAANG
Key Concepts:
1) Because this is a binary search tree, the left subtree always has smaller values than the root,
and the right subtree always has bigger values than the root
2) A successor is essentially the node with the next biggest value compared to our parameter p
3) Using this information, we can use binary search such that when we're locating p, if p is less than our current
root value, that means our current root value could be a successor, so we set our successor and search the left subtree.
If our p is greater than or equal to our root value (because a node cannot be a successor of itself), we continue searching
the right subtree.

We continue the recursion so that if we find an even smaller value for our successor (that's still greater than our p value),
we will set it while continually searching the left subtree, until our root is None.

Time: O(LogN)
Space: O(1)

"""

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        self.successor = None
        def helper(root, p):
            if root:   
                if p.val < root.val:
                    self.successor = root
                    helper(root.left, p)
                # search right subtree
                if p.val >= root.val:
                    helper(root.right, p)
        helper(root, p)
        return self.successor