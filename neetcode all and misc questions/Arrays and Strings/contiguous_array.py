"""
https://leetcode.com/problems/contiguous-array/
https://www.youtube.com/watch?v=Xkl4EknqW8Y&t=144s&ab_channel=CrackingFAANG
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Revisited on 12/11/2025
        https://neetcode.io/solutions/contiguous-array

        brute force is to find every subarray and track the ones and zeroes of each

        The optimized solution is much trickier and involves keeping track of the difference
        of total ones and zeroes found so far in a hashmap, and map the difference to the index
        where it occurs

        The reason for this is because if we at a given index, and we know the total ones and zeroes
        so far, we can take ones - zeroes, and then look this up in the hashmap, and it will tell us
        if there is a subarray that ends at the index that is mapped to in this dictionary with this 
        difference value. We then take this value and subtract it from our current index i to
        get the subarray with equal amount of 1's and 0's.

        For example:
        0 1 1 1 1 1 0 0 0

        i = 0
        hashmap = {}
        ones = 0
        zeroes = 1
        ones - zeroes = -1
        hashmap = {-1: 0}

        i = 1
        hashmap = {-1: 0}
        ones = 1
        zeroes = 1
        ones - zeroes = 0

        Note here because ones == zeroes, this counts as an answer,
        so we could count this as 1 + 1 = 2, a subarray of length 2 that has one zero
        and one 1.
        hashmap = {-1: 0, 0: 1}

        i = 2
        hashmap = {-1: 0, 0: 1}
        ones = 2
        zeroes = 1
        ones - zeroes = 1
        hashmap = {-1: 0, 0: 1, 1: 2}

        i = 3
        hashmap = {-1: 0, 0: 1, 1:2}
        ones = 3
        zeroes = 1
        ones - zeroes = 2
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3}

        i = 4
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3}
        ones = 4
        zeroes = 1
        ones - zeroes = 3
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4}

        i = 5
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4}
        ones = 5
        zeroes = 1
        ones - zeroes = 4
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

        i = 6
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        ones = 5
        zeroes = 2
        ones - zeroes = 3
        note that the difference of 3 does exist in the hashmap, but we don't want
        to overwrite the existing value
        looking up 3, we get idx of 4. And 6 - 4 = 2
        so we get a subarray of 2 (which is just 1 0 as shown here)
        0 1 1 1 1 1 0 0 0
                  ^ ^
        
        i = 7
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        ones = 5
        zeroes = 3
        ones - zeroes = 2
        we look up 2 in the hashmap, and see that the idx of 3
        i - idx which is: 7 - 3 = 4
        so we get a subarray of length of 4 as shown here
        0 1 1 1 1 1 0 0 0
                ^ ^ ^ ^
        
        i = 8
        hashmap = {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        ones = 5
        zeroes = 4
        ones - zeroes = 1
        we look up 1 in the hashmap, and see that the idx of 2
        i - idx = 8 - 2 = 6
        which is the subarray as shown here
        0 1 1 1 1 1 0 0 0 
              ^ ^ ^ ^ ^ ^
        note that the idx of 2 is the "end" of the subarray (0 1 1), where
        there's a difference value of 1 (2 ones, 1 zero = difference of 1)
        so the remainder becomes the subarray we're looking for.

        Final result is 6

        Time: O(N)
        Space: O(N)
        """
        ones = 0
        zeroes = 0
        diffToIndex = {}
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                zeroes += 1
            if n == 1:
                ones += 1
            
            if ones - zeroes not in diffToIndex:
                diffToIndex[ones-zeroes] = i
            
            # if the count of ones equals the count of zeroes (Which usually happens
            # if we find this subarray for the first time), just add the two values
            # to get the total length
            if ones == zeroes:
                res = ones + zeroes
            elif ones - zeroes in diffToIndex:
                # get the ending index of the subarray that has this difference value
                idx = diffToIndex[ones-zeroes]
                # subtract the current index with the idx to get the remaining subarray
                # that contains the equal amount of zeroes and ones that we want.
                res = max(res, i - idx)
        return res

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
            
