class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
        Time: O(NLogK) 
        Space: O(N)
        """
        import heapq
        maxHeap = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, -1 * int(nums[i]))
        res = 0
        for i in range(k):
            res = heapq.heappop(maxHeap)
        return str(-1*res)
            