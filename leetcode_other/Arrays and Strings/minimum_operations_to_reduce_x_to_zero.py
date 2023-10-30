"""
Key Concept: 
Reverse Thinking + Sliding Window

Finding the minimum operations to reduce x to zero is essentially
saying to find numbers that add up to x

1 1 4 2 3, x = 5

The problem statement describes the optimal way of solving
which is "remove" 2 and 3 on the right side to get 0, but
using our reverse thinking:

If there's a combination of numbers on the left and right side
that equal 5, there must be a "middle" portion that's not chosen

in that case it's 1 1 4

This middle portion will add up to the remainder of the total sum of the array subtracted
from our target (which is 6)

1 1 4

Therefore, this problem is actually a maximum subarray where the sum equals our target,
where the target = sum of total array - X

Once we find that, we take total length of array - length of this subarray to get the answer


"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        l = 0
        cur = 0
        res = float("inf")
        n = len(nums)
        for r in range(len(nums)):
            cur += nums[r]
            if cur == target:
                windowSize = r - l + 1
                res = min(n - windowSize, res)
            elif cur > target:
                while (cur > target and l <= r):
                    cur -= nums[l]
                    l += 1
                    if cur == target:
                        windowSize = r - l + 1
                        res = min(n - windowSize, res)
                    
        return res if res != float("inf") else -1
                
    
        