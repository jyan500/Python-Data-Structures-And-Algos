"""
https://leetcode.com/problems/contiguous-array/
https://www.youtube.com/watch?v=Xkl4EknqW8Y&t=144s&ab_channel=CrackingFAANG
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """ 
        O(N^2) solution, finds every possible contiguous subarray
        by keeping track of a dict of the count of each 1 and 0
        """
        # count = {0: 0, 1: 0}
        # curLen = 0
        # maxLen = float("-inf")
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         count[nums[j]] += 1
        #         if count[0] == count[1]:
        #             curLen = count[0] + count[1]
        #             maxLen = max(curLen, maxLen)
        #     count = {0: 0, 1: 0}
        # return maxLen if maxLen != float("-inf") else 0
        """
        O(N) time solution

        https://www.youtube.com/watch?v=Xkl4EknqW8Y&t=144s&ab_channel=CrackingFAANG

        1) Key is to treat each 0 as -1 instead, and then keep track of a cumulative sum
        2) When our sum is zero (i.e for the sequence 1 0, 1 + -1 = 0), this means there's 
        an equal amount of ones and zeroes, we can store our max length.
        3) We store our cumulative sum as the key and index as the value in a hashmap
        4) We have to look at points in our hashmap where the cumulative sum has already been seen
           There's a trick where if that cumulative sum is reached again, that means anything between
           the stored index + 1 TO our current index would be a subarray. You can see that in the example below:
           1 0 0 0 0 1 1 1 1
           
           the cumulative sums at each point:
           1 0 -1 -2 -3 -2 -1 0
           
           You can see between -2 and -2, this shows corresponds 
           to 0 0 1
           but if you were to remove the first 0 (which is stored index + 1),
           that would actually be a subarray of length 2 (0, 1)
           
           Same with -1 and -1
           this corresponds to 0 0 0 1 1 
           
           If you were to remove the first 0 (which is stored index + 1),
           that would be subarray of length 4 (0, 0, 1, 1)
           
           We can find the length of the subarray by subtracting our current index
           and the stored index
           
        """
        count = {0: -1}
        """
        we have to initialize the count 0 as -1, to handle 
        an edge case when there's only 2 values: 0, 1
        
        0 1
        count = {0: -1}
        cumulativeSum = 0
        
        1st iteration
        stores sum = -1, index = 0 in the dict
        stores sum = 1, index = 1 in the dict
        
        As shown 1 - 0 to get maxLength would not be correct,
        since that's only 1, but the max length should be 2
        
        therefore, we initialize count 0's value to -1, so that we get
        1 - (-1) = 2
        
        """
        cumulativeSum = 0
        maxLength = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cumulativeSum -= 1
            else:
                cumulativeSum += 1
            if cumulativeSum in count:
                maxLength = max(maxLength, i - count[cumulativeSum])
            else:
                count[cumulativeSum] = i
        return maxLength
            
