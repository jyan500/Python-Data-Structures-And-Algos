# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        https://neetcode.io/solutions/house-robber-iii
        DFS/PostOrder Traversal
        At each point, we want to return an array with 2 values,
        that consists of the max that
        we can make if
        1) we rob the current node
        2) we don't rob the current node
        
        for case 1) if we rob the current node, do root.val and then add
        for the recursive calls for the left and right subtree, we take the index 1 element
        of each. This is because this is the "withoutRoot" case since we're not allowed to include
        the values of the direct children of this current node.
        
        for case 2) if we don't rob the current node, we get the return values of the recursive calls
        on the left and right, and then take the max of each between the pairs of values. This is because
        when we don't rob the current node, the max helps us determine whether it was better to rob the direct child or skip it.
        
        base case:
        if the root is None, return [0, 0]

        Time: O(N), this algorithm only visits each node once
        Space: O(N)
        """
        def search(root):
            if not root:
                return [0,0]
            leftPair = search(root.left)
            rightPair = search(root.right)
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)
            return [withRoot, withoutRoot]
        withRoot, withoutRoot = search(root)
        return max(withRoot, withoutRoot) 