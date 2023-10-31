"""
See remove duplicates from sorted array II
Similar solution, except the elements can only show up once rather than twice.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = dict()
        numUnderscores = 0
        firstUnderscore = 0
        for i in range(len(nums)):
            if nums[i] in counter:
                nums[i] = "_"
                if numUnderscores == 0:
                    firstUnderscore = i
                numUnderscores += 1
            else:
                counter[nums[i]] = 1
        j = firstUnderscore
        for i in range(firstUnderscore, len(nums)):
            if nums[i] != "_":
                nums[j] = nums[i]
                j += 1
        for k in range(j, len(nums)):
            nums[k] = "_"
        
        
        return len(nums) - numUnderscores
        