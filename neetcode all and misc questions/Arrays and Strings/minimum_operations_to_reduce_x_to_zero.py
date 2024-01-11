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

1 1 4 2 3

1 1 4 equals our target, this is a window size of 3, so it would be length of array - windowsize (5 - 3 = 2),
which would be minimum of 2 operations to make x = 5 become x = 0. This adds up, since the only two numbers
remaining are 2 and 3 ( 2+3 = 5, 5 - 5 = 0) 

If we continue the logic...
1 + 1 + 4 + 2 is 8 which is too big, keep shrinking the window until the current sum is less than the target again,
which will be:
4 2 

this is a window size of 2, so length of array - windowSize (5 -2 = 3), this is the equivalent 
of 1 1 on the left side, and 3 on the right side (three operations). We've already found that
removing 2 and 3 takes less operations though.

Returns 2



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
                
    
