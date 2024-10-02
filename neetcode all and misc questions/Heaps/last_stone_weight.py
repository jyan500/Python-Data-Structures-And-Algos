"""
https://leetcode.com/problems/last-stone-weight/
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        https://neetcode.io/problems/last-stone-weight
        Use a max heap 
        continue popping off max heap twice at a time until there's at least one element in the max heap left
        O(NLogN) + O(MLogN), where M is the amount of times heappush() is called
        """
        import heapq
        # use negative numbers to create a max heap
        maxHeap = [-stones[i] for i in range(len(stones))]
        heapq.heapify(maxHeap)
        # there has to be at least two stones
        while len(maxHeap) > 1:
            # convert back to positive numbers
            stone1 = -1 * heapq.heappop(maxHeap)
            stone2 = -1 * heapq.heappop(maxHeap)
            if stone1 > stone2 or stone2 > stone1:
                # get the weight difference and multiply by -1
                # to put back onto the max heap
                newStone = -1 * abs(stone1-stone2)
                heapq.heappush(maxHeap, newStone)
        return -1 * maxHeap[0] if len(maxHeap) == 1 else 0

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