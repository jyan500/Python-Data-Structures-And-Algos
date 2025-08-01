"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Concept:
Sliding Window, l and r
r continues to increment, add to the sum until
the current sum >= target
then, continually increment l until the current sum 
is less than the target. While doing this,
also calculate the min window size

example:

2 3 1 2 4 3

2 + 3 + 1 + 2 = 8

increment l so 2 is removed (min window size of 4 so far)

3 1 2 4, cur sum is now 10

increment l so 3 is removed

1 2 4, cur sum is now 7 (min window size of 3 so far)

1 2 4 3 (cur sum is now 10)

removes 1, cur sum is now 9

removes 2, cur sum is now 7 (min window size of 2)

returns the min window size of 2

"""
class Solution:
    # Revisited 8/1/2025
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        minCurrentLength = float("inf")
        length = 0
        l = 0
        for r in range(len(nums)):
            currentSum += nums[r]
            while (currentSum >= target):
                minCurrentLength = min(minCurrentLength, r - l + 1)
                currentSum -= nums[l]
                l += 1
        return minCurrentLength if minCurrentLength != float("inf") else 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(N^2) solution
        # res = float("inf")
        # for i in range(len(nums)):
        #     curSum = 0
        #     for j in range(i, len(nums)):
        #         curSum += nums[j]
        #         if curSum >= target:
        #             res = min(j-i+1, res)
        # return res if res != float("inf") else 0
        l = 0
        curSum = 0
        res = float("inf")
        for r in range(len(nums)):
            curSum += nums[r]
            if curSum >= target:
                while(curSum >= target):
                    res = min(r-l+1, res)
                    curSum -= nums[l]
                    l += 1
        return res if res != float("inf") else 0

            
            