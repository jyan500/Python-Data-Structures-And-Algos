'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
https://leetcode.com/problems/maximum-subarray/

Kadane's Algorithm
'''

class Solution:
	def alternativeSolution(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        current_sum = float('-inf')
        for i in range(len(nums)):
            # if you add the current number, 
            # and the current number is still greater than the current sum, 
            # we can set the current sum to be the current number, as the subarray
            # starting at this number should have a greater sum than the subarray before it
            if nums[i] >= current_sum + nums[i]:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
        	# check to see if the current sum is greater than the largest sum 
            largest_sum = max(largest_sum, current_sum)

        return largest_sum

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float(-inf)
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = max(nums[i], cur_sum+nums[i])
            max_sum = max(cur_sum,max_sum)
            
        return max_sum