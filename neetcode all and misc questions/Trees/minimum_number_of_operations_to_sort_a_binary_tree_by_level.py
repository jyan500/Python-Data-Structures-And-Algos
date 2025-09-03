# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        9/3/2025
        https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

        level order traversal - BFS
        extract the values at each level
        how to count the number of operations needed to make the values at each level sorted in increasing order?

        1) brute force
            swapping every pair and see which ones results in a sorted order
        2) greedy
            find the min() and then always try to swap it to the ith position,
            where i ... N, where N is len(values at this level)
            then on the next iteration, take the min from i ... N again, find the index,
            and swap it with i
            This is a working solution but gets TLE on leetcode, because it is an O(H*(M^2)) solution,
            having to take the min and getting the index are both O(M) operations inside a loop.

        how to optimize?
        - store a hashmap which maps the value to each index. This works
        because the problem states that the tree is entirely unique values.
        - sort the values of the array at each level
        - loop through the original array, and check whether originalArray[i] != sorted[i],
        if so this would be considered one "swap" operation, so increment by one

        This would now be O(H * (MLogM + O(M)), where M is the length of each level and H is the amount of levels,
        with additional O(H*M) for space complexity
        """
        from collections import deque, defaultdict
        q = deque()
        q.append(root)
        res = 0
        while (q):
            N = len(q)
            level = []
            indexMap = defaultdict(int)
            for i in range(N):
                node = q.popleft()
                level.append(node.val)
                indexMap[node.val] = i
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if (len(level) > 1):
                # sort the values at each level
                sortedLevel = sorted(level)
                for i in range(len(level)):
                    if sortedLevel[i] != level[i]:
                        # figure out where the correct sorted value for this ith value
                        # is within the original unsorted list and then swap the positions
                        getIndex = indexMap[sortedLevel[i]]
                        level[i], level[getIndex] = level[getIndex], level[i]
                        # swap the indexes within the index map as well
                        indexMap[level[i]], indexMap[level[getIndex]] = indexMap[level[getIndex]], indexMap[level[i]]
                        res += 1

                # original solution of finding the min repeatedly and swapping
                # for i in range(len(level)):
                #     curMinIndex = level.index(min(level[i:]))
                #     # swap to the position i if the index where the min is located
                #     # is not already at i, and then count this as one operation
                #     if curMinIndex != i:
                #         level[i], level[curMinIndex] = level[curMinIndex], level[i]
                #         res += 1
        return res