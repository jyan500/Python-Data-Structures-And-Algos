# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
        https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
        
        with the "kth" type problems, a heap seems to be an appropriate choice,
        specifically, a max heap.

        Perform a level order traversal, getting the sum of each level and inserting it into the max heap
        Then get the kth largest sum
        """

        import heapq
        from collections import deque

        q = deque()
        maxHeap = []

        q.append(root)
        while (q):
            N = len(q)
            curSum = 0
            for i in range(N):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                curSum += node.val
            heapq.heappush(maxHeap, -1 * curSum)
        res = -1
        if len(maxHeap) >= k:
            for i in range(k):
                res = -1 * heapq.heappop(maxHeap)
        return res
        