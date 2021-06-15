'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
https://leetcode.com/problems/product-of-array-except-self/
https://www.youtube.com/watch?v=tSRFtR3pv74&t=148s&ab_channel=NickWhiteNickWhite
'''
class Solution:
	def mostEfficientSolution(self, nums: List[int]) -> List[int]:
		## O(1) space
		output = [1]
		## store the prefix values within the output array instead of having a separate prefix array
		for i in range(1, len(nums)):
			output.append(nums[i-1] * output[i-1])
		res = 1
		## calculate the postfix values (stored in res) where we multiply the prefix value by the postfix value,
		## except we multiply by the value of res
		## the value of res is simply the previous value of res times the current index of nums, because
		## that would be the value of every element to the right of that current index 
		for i in range(len(nums) - 1, -1, -1):
			output[i] = output[i] * res
			res = res * nums[i]
		return output

    def productExceptSelf(self, nums: List[int]) -> List[int]:
    	## first Nick White solution with O(N) space
        output = []
        ## get list of products that are after i by looping backwards
        postfix = []
        for i in range(len(nums)):
            postfix.append(1)
        ## note that in the last index of postfix ,the value is 1 since the product of everything to the right of the last item is the number itself
        for i in range(len(nums)-2, -1, -1):
        	## nums[i+1] would be the previous number (in the perspective of looping backwards) times the previous product that we have so far
            postfix[i] = nums[i+1] * postfix[i+1]
        

        ## get list of products that are before i by looping forwards
        prefix = [1]
        ## note that the first index of prefix, the value is 1 since the product of everything to the left of the first item is the number itself
        for i in range(1, len(nums)):
        	## nums[i+1] would be the previous number times the previous product that we have so far
        	prefix.append(nums[i-1] * prefix[i-1])

        ## use the prefix and postfix lists to calculate the product of everything before i and everything after i
        for i in range(len(nums)):
        	output.append(prefix[i] * postfix[i])
        return output

    def firstSolution(self, nums: List[int]) -> List[int]:
    	## first Neetcode Solution with O(N) space
        output = []
        ## get list of products that are after i by looping forwards
        postfix = []
        for i in range(len(nums)):
            postfix.append(0)
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            if (i == len(nums)-1):
                prev = nums[i]
            else:
                prev *= nums[i]
            postfix[i] = prev
        

        ## get list of products that are before i by looping backwards
        prefix = []
        prev = 1
        for i in range(len(nums)):
            if (i == 0):
                prev = nums[i]
            else:
                prev *= nums[i]
            prefix.append(prev)


        ## use the prefix and postfix lists to calculate the product of everything before i and everything after i
        for i in range(len(nums)):
            if (i == 0):
                output.append(postfix[i+1] * 1)
            elif (i >= len(nums)-1):
                output.append(prefix[i-1] * 1)
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output

