# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
        9/2/2025

        Variation of Level Order Traversal using BFS:
        1) perform level order traversal
        2) At each level, since the problem states we only need to reverse the node values,
        we could just extract all the values at each level, reverse them, and then set the values
        back into the nodes (rather than doing any pointer manipulation to reverse them within the tree itself)
        
        Time: O(N)
        Space: O(N), at every odd level, we need to store the values in a list to reverse them
        """

        from collections import deque
        q = deque()
        q.append(root)
        curLevel = 0
        while q:
            N = len(q)
            intermediate = []
            nodes = []
            for i in range(N):
                node = q.popleft()
                if curLevel % 2 != 0:
                    intermediate.append(node.val)
                    nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curLevel % 2 != 0:
                intermediate.reverse()
                # set the reversed values on each node at this level
                for i in range(len(nodes)):
                    nodes[i].val = intermediate[i]
            curLevel += 1
        return root