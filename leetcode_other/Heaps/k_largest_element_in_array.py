'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

https://leetcode.com/problems/kth-largest-element-in-an-array/

Concept:
use a max heap, since python's heapq implementation is a min heap by default
we can simulate a "max heap" by setting all the numbers in our list to negative
so after performing "heapify," the smallest (most negative value) will be the root of our heap

when we get our answer, we just need to multiply by -1 to flip the number back to being positive
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        print(nums)
        heapq.heapify(nums)
        ans = 0
        for i in range(k):
            ans = -1 * heapq.heappop(nums)
        return ans