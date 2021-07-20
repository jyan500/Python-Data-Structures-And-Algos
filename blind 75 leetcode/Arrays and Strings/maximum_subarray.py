'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
https://leetcode.com/problems/maximum-subarray/

Kadane's Algorithm
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float(-inf)
        cur_sum = 0
        for i in range(len(nums)):
            ## check to see if the current number we're on is greater than our current sum
            ## if it is, we can just set the current sum to the current number we're on
            # if (nums[i] > cur_sum + nums[i]):
            #     cur_sum = nums[i]
            # else:
            #     cur_sum = cur_sum + nums[i]
            cur_sum = max(nums[i], cur_sum+nums[i])
            
            # if (cur_sum > max_sum):
            #     max_sum = cur_sum
            max_sum = max(cur_sum,max_sum)
            
        return max_sum