"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
1) Use Max Heap by setting all numbers in input to negative
2) heapify
3) heap pop out until k is reached

Time: O(NLogK)
Space: O(N)

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-nums[i] for i in range(len(nums))]
        heapq.heapify(nums)
        recent = None
        for i in range(k):
            recent = heapq.heappop(nums)
        return -1 * recent