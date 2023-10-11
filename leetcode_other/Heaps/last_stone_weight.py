"""
https://leetcode.com/problems/last-stone-weight/
"""
class Solution:
    """
    Max Heap Solution
    """
    def lastStoneWeight2(self, stones: List[int]) -> int:
        import heapq
        maxHeap = [-stones[i] for i in range(len(stones))]
        heapq.heapify(maxHeap)
        # take the first two elements off the top of the heap
        while (len(maxHeap) > 1 and maxHeap[0] != 0):
            # by doing element - element, this can be 0 if the elements have the same value,
            # which is why we have the top condition mapHeap[0] != 0
            heapq.heappush(maxHeap, heapq.heappop(maxHeap)-heapq.heappop(maxHeap))
        # return - to turn the number back into positive
        return -maxHeap[0]



    """
    Brute Force
    while loop, while there are at least 2 stones,
    continue the computations, and then re-sort
    after each computation
    O(N * NLogN)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        if len(stones) == 1:
            return stones[-1]
        while (len(stones) > 1):
            y = stones[-1]
            x = stones[-2]
            if x == y:
                # destroy both
                stones = stones[:-2]
            else:
                # x is destroyed
                # y is recalculated
                newY = y - x
                stones = stones[:-2] + [newY]
            stones.sort()
        return stones[-1] if len(stones) > 0 else 0