'''
https://leetcode.com/problems/longest-consecutive-sequence/
'''
class Solution:
	## O(N^2) time and O(N) space
	## The bottleneck is the while loop where we find if the next consecutive number in the sequence exists
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0): 
            return 0
        lookup = dict()
        for n in nums:
            lookup[n] = 1
        longest = 1
        longest_so_far = 1
        for i in range(len(nums)):
            cur = nums[i]
            ## lookup can be optimized here,
            ## if we know the smallest number at which we can start a sequence
            ## there's no need to repeat the work for the numbers following the smallest one in the sequence
            ## for example, if we have 1,2,3,4 as a sequence
            ## we don't need to repeat this loop for 2 and 3 and 4, etc because they will never be as long
            while (lookup.get(cur+1) != None):
                cur += 1
                longest_so_far += 1
            longest = max(longest, longest_so_far)
            longest_so_far = 1
        return longest

    ## O(N) time and O(N) space
    ## this is O(N) (and not N^2) because the while loop
    ## only runs starting at the beginning of a potential sequence
	## therefore, its O(N) when we run through the loop that finds the sequence, and O(N) for looping through the nums array
	## for a total of O(2N) which is still O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
    	if (len(nums) == 0):
    		return 0
    	lookup = dict()
    	for n in nums:
    		lookup[n] = 1
    	longest = 1
    	longest_so_far = 1
    	for i in range(len(nums)):
    		cur = nums[i]
    		## the key optimization is that we don't need to repeat work if
    		## the previous consecutive number already exists
    		## we only need to run the while loop for the smallest numbers that would potentially make a sequence
    		if (not lookup.get(cur-1)):
	    		while (lookup.get(cur+1) != None):
	                cur += 1
	                longest_so_far += 1
	    		longest = max(longest, longest_so_far)
	    		longest_so_far = 1
    	return longest