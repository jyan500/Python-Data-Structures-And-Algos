"""
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
https://www.youtube.com/watch?v=JU5XdBZZtlk&ab_channel=NeetCode

Revisited 8/7/2025

Key Concept:
To get the minimum difference between scores, it'd make sense to sort them first.
And then apply sliding window of size K, where you continually
take the difference between the left side of the window (smallest) and the right side of the window (largest)
until you find the minimum difference.

"""
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k - 1
        res = float("inf")
        while (r < len(nums)):
            res = min(nums[r] - nums[l], res)
            r += 1
            l += 1
        return res