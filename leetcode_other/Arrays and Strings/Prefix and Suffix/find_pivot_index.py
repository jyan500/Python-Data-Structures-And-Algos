"""
https://leetcode.com/problems/find-pivot-index/
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Concept:
        Prefix and Suffix Sums
        if we transform nums into both a prefix and suffix sum form, which is the cumulative
        sum up to that index i, prefix going from the front ,and suffix going from the back.
        We should be able to
        find where the index where the sum is the same on both arrays
        
        prefix sum form:
        nums = [1, 8, 11, 17, 22, 28]
        
        suffix sum form:
        nums = [28, 27, 20, 17, 11 ,6]
        
        Here the answer is 3 because the sum is the same
        
        If we loop through both indices and no value is the same, return -1
        
        """
        
        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i]
        
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1