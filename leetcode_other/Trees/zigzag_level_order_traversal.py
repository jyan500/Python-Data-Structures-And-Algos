"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

In each ith level,
Similar to regular level order traversal using BFS, except 
if i % 2 != 0, reverse the level's list before appending to final result

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        levelNum = 0
        while (q):
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelNum % 2 != 0:
                level.reverse()
            levelNum += 1
            res.append(level)
        return res
                