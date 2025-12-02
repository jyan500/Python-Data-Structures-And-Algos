from typing import (
    List,
)

"""
https://www.lintcode.com/problem/883/
Leetcode Premium
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        https://neetcode.io/problems/max-consecutive-ones-ii/question
        sliding window
        1 0 1 1 0 1 1 1 1
        
        if a second "0" is found, 
        move the left pointer until its one index after the 0 that we flipped

        Edge cases:
        if no zeroes are found, or only one zero is found, just take the length of the array as the max length
        """
        l = 0
        firstZeroIndex = None
        flag = False
        maxLength = 0
        for r in range(len(nums)):

            if nums[r] == 0:
                # set flag if we've found a first zero
                if not flag:
                    flag = True
                # if we find a second zero, calculate the max length and
                # set the left pointer to be one after the first zero we found.
                else:
                    flag = False
                    maxLength = max(maxLength, r - l)
                    l = firstZeroIndex + 1
                firstZeroIndex = r
        # if our flag is still true (meaning only one zero was found),
        # or no zeroes were found,
        # the max length will just be the num
        if flag or (not firstZeroIndex):
            maxLength = max(maxLength, len(nums))

        return maxLength
            
class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        """
        sliding window
        Approach:
        l = 0, r = 0
        if we see a 1, add to cur, and also set the max(cur, maxCur)
        if we see a 0, we need to check whether we've seen an index where 0 was found
            if we haven't
                increment cur 
                set last occurrence of zero to r 
            else:
                we need to decrement the amount of places based on the difference between
                the last occurrence of zero + 1 and the left pointer 
                for example, if the last occurrence of zero was at i = 4, and l = 2, we'd do 
                cur -= last occurrence of zero + 1 - left pointer, since we also include the current placement as an extra "one" value that's being subtracted
                we'd then need to shift the left pointer to the last occurrence of zero + 1
                set the last occurrence of zero to None
                continue
                

        r = 0 nums[r] is 1, cur = 1, maxCur = 1
        r = 1 nums[r] is 0, flipped = True, cur = 2, maxCur = 2
        r = 2 nums[r] is 1, cur = 3, maxCur = 3
        r = 3 nums[r] is 0, we have to move the left pointer until the last occurrence of 0 is found, and increment once more
        l = 2, cur = 1
        r = 3  nums[r] is 0, this time, flipped = False, so we can set to True. And increment cur = 2
        r = 4 nums[r] is 1, increment cur = 3

        answer is 3
        

        """
        l = 0
        r = 0
        cur = 0
        maxCur = 0
        lastOccurrenceOfZero = 0
        while r < len(nums):
            if nums[r] == 0:
                if lastOccurrenceOfZero == None:
                    lastOccurrenceOfZero = r
                    cur += 1
                else:
                    cur -= (lastOccurrenceOfZero + 1 - l)
                    l = lastOccurrenceOfZero + 1
                    lastOccurrenceOfZero = None
                    continue               
            else:
                cur += 1

            maxCur = max(cur, maxCur)
            r += 1     
        return maxCur 


if __name__ == "__main__":
    s = Solution()
    output1 = s.find_max_consecutive_ones([1,0,1,1,0])
    print(output1)
    assert output1 == 4
    output2 = s.find_max_consecutive_ones([1,0,1,0,1])
    print(output2)
    assert output2 == 3
    output3 = s.find_max_consecutive_ones([1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1])
    print(output3)
    assert output3 == 9
