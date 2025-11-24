# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        level order traversal
        in each level, get the max
        """
        from collections import deque
        if not root:
            return []
        q = deque()
        q.append(root)
        maxValues = []
        while (q):
            N = len(q)
            curMax = float("-inf")
            for i in range(N):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # store the current max for this level
                curMax = max(curMax, node.val)
            maxValues.append(curMax)
        return maxValues
