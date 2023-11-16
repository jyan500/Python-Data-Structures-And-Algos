class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """ O(n) space solution which calculates the difference between the complete set of numbers with the given set """
        # return list(set([i+1 for i in range(len(nums))]).difference(set(nums)))
        """
        O(1) space solution
        Concept:
        1) We can use the indices of the array itself as a lookup to determine whether a given number
        in the range 1 ... n exists
        
        range is from 1 ... 4
        [1, 4, 4, 4]
        
        index 0 1 2 3 
        val   1 4 4 4 
        
        the index will represent the "key" for the lookup of the value, which will be the value - 1
        so val 1 maps to index 0
        val 4 maps to index 3, etc
        
        2) If we see a given value, we then mark it's corresponding value in the index to be -1 to become negative. Important is that when we actually check the corresponding value, we need to an absolute value, otherwise we wouldn't be able to map it back to the proper index.
        
        0 1 2 3
        1 4 4 4
        
        1 is found, so we mark the value under index 0 to be -1
        
         0 1 2 3
        -1 4 4 4
        
        4 is found, so we mark the value under index 3 to be -4
        
        0 1 2  3
       -1 4 4 -4
       
        4 is found again, so we re-mark the value under index 3 to be -4, etc
        
        3) We then check to see which values are negative. The values that are negative have been "found", while the values that weren't negative were not found. We look at the indices of the values not found, and then add 1 to get the final answer. 
        
        0 1 2  3
       -1 4 4 -4
       
        at the end, we have negative values under indices 0 and 3, but the values under
        1 and 2 are positive. So that means 1 + 1, 2+ 1, which represent values 2 and 3
        are not present in the array
         
        https://www.youtube.com/watch?v=8i-f24YFWC4&t=361s&ab_channel=NeetCode
        """
        
        for i in range(len(nums)):
            # this needs to be an absolute value in case 
            # we over-wrote this value earlier in the function and made it negative
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        # the return array does not count as additional space
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
        