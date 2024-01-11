"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        O(2N) time
        O(1) memory
        if you reach a element that has been seen more than twice,
        replace it with a sentinel value. Keep track of a pointer that indicates
        the first time a sentinel value occurs.
        
        In a second loop, do something similar to "move zeroes". Using reverse thinking, rather than trying
        to move all sentinel values to the back, move all the 
        non-sentinel values up to the front, up to the pointer that tracked the first time the sentinel value occurs. 

        Keep track of another pointer that tracks the last sentinel value (j)
        
        Then pad the rest of the array from j ... len(nums) with sentinel values.
        
        Return the length of the array minus the amount of sentinel values
        """
        cur = nums[0]
        seen = 1
        numOfUnderscores = 0
        firstUnderscore = 0
        for i in range(1, len(nums)):
            if nums[i] != cur:
                cur = nums[i]
                seen = 1
                continue
            seen += 1
            if seen > 2:
                if numOfUnderscores == 0:
                    firstUnderscore = i
                nums[i] = "_"
                numOfUnderscores += 1
        j = firstUnderscore
        for i in range(firstUnderscore, len(nums)):
            if nums[i] != "_":
                nums[j] = nums[i]
                j += 1
        for k in range(j, len(nums)):
            nums[k] = "_"
                
        return len(nums) - numOfUnderscores
                    
            