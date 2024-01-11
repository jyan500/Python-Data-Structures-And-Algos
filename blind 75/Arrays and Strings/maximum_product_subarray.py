'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
https://www.youtube.com/watch?v=lXVy6YWFcRM&ab_channel=RandomCoderRandomCoder
https://leetcode.com/problems/maximum-product-subarray

O(N) time (loops through the array once)
O(1) space (only using two variables, no arrays or extra contiguous memory)
'''

class Solution2:

	# revisited this problem on 7-4-2023 using
	# https://www.youtube.com/watch?v=hnswaLJvr6g&ab_channel=takeUforward
	def maxProduct(self, nums: List[int]) -> int:
        """
        keep track of the running product coming from the front (prefix), and from the back (suffix)
        the logic is that this running prefix and suffix product will capture all possible subarrays
        that can be found, so we just need to find the max between the prefix and suffix product during
        the iteration
        For example:
        2, 5, -1, 3, 6
        if we take the prefix starting at 2
        and suffix starting at 6
        prefix = 2 * 5 = 10
        suffix = 6 * 3 = 18
        greatest is 18
        
        prefix = 2 * 5 * -1 = -10
        suffix = 6 * 3 * -1 = -18
        greatest is still 18
        
        prefix = 2 * 5 * -1 * 3 = -30
        suffix = 6 * 3 * -1 * 5 = -90
        greatest is still 18
        
        prefix = 2 * 5 * -1 * 3 * 6 = -180
        suffix = 6 * 3 * -1 * 5 * 2 = -180
        greatest is still 18
        
        If any of the numbers are zero, we need to "restart" the prefix/suffix product to 1 since
        if we kept it at 0, all the subsequent products would become 0 as well.
        """
        greatest = float("-inf") 
        prefix = 1
        suffix = 1
        length = len(nums)
        for i in range(length):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix * nums[i]
            suffix = suffix * nums[length - 1 - i]
            greatest = max(greatest, max(prefix, suffix))
        return greatest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## we need to set the result to max(nums) to handle an edge case where you have only one number in the nums
        ## like [-1], in this case we can't just set res to zero, otherwise we would get 0 as the maximum
        res = max(nums)
        
        ## we set the curMin and curMax to 1 since multiplying any number by 1 is just the same number
        curMin, curMax = 1, 1
        for n in nums:
            ## in the case num with value of 0, since any num multiplied by zero is zero, we just reset the curMin and curMax
            ## to 1 and move onto the next number, as if we skip the 0 entirely and "reset" the curMin and curMax
            if (n == 0):
                curMin, curMax = 1, 1
                continue
            tmp = n * curMax
            ## we have the tmp variable so that in the calculation of curMin, we will not use
            ## the new updated value of curMax
            
            ## the idea behind finding both the curMax and curMin is to deal with cases where we have negative and positive numbers mixed in
            ## Some examples:
            ## #1 (when n helps us find the max)
            ## if our array was [-1, 8] and n was 8
            ## the curMax right now would be -1
            ## if we were to calculate it, n * curMax = -8, n * curMin = -8, but n = 8. Meaning the curMax would be 8 

            ## #2 (when curMin helps us find the max)
            ## for an array like so [-1, -2, -3] and n was -3
            ## curMax is 2
            ## curMin is -2
            ## here, n * curMax = -6, n * curMin = 6, and n = -3, so curMin actually helps us find the proper max

            ## curMin would be the same process but using min instead of Max function.
            ## see the youtube link above for more explanation
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            ## res would just be the max between the current res value and the curMax that we found
            res = max(res, curMax)
        return res