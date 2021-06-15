'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def twoSum(self, nums: List[int], target : int) -> List[int]:
	## map the target value - the current number with index of the current number
	pairs = dict()
	for i in range(len(nums)):
		## if the current number is found in the pairs dictionary...
		if (nums[i] in pairs):
			## then a pair has been found
			## return the indices of the two numbers
			return [pairs[nums[i]], i]
		else:
			## store the index of the number, and its potential complementary pair
			## by subtracting the target value with the current number
			pairs[target - nums[i]] = i 
	return None