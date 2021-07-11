'''
https://leetcode.com/problems/longest-increasing-subsequence/solution/
DP Solution
https://www.youtube.com/watch?v=CE2b_-XfVDk&t=324s&ab_channel=TusharRoy-CodingMadeSimple

Top Down Solution
https://www.youtube.com/watch?v=ekKYRYFEm9w&list=PLQdWvigIOnscz0Fgps9PtnymVkvJrZylH&index=5&ab_channel=AnuragVishwa
'''
class Solution:
    ## converted from Tushar Roy's java solution
    ## https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/LongestIncreasingSubsequence.java
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## the longest increasing subsequence of the smallest subproblem (which is just the individual number itself) is always 1
        ## so we initialize the position to 1
        dp = [1] * len(nums)
        ## we skip the first element since the longest subsequence of the first element is always 1
        for i in range(1, len(nums)):
            for j in range(i):
            	## the recurrence relation is that if we encounter nums[i],if nums[i] > nums[j], we check the dp[i] position
     			## as well as the dp[j] position + 1 and pick whichever one is greater
     			## the reason why is that dp[i] will always contain the longest increasing subsequence at that point
     			## so we can use each previous step and add one to get the answer
                if (nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        ## by the end, the max of dp array will contain the longest increasing subsequence at that point
        return max(dp)


    ## recursive solution using brute force O(2^N)
    ## https://stackoverflow.com/questions/37561909/does-there-exist-a-top-down-dynamic-programming-solution-for-longest-increasing
    ## https://www.youtube.com/watch?v=ekKYRYFEm9w&list=PLQdWvigIOnscz0Fgps9PtnymVkvJrZylH&index=5&ab_channel=AnuragVishwa
    def lengthOfLIS(self, nums: List[int]) -> int:
    	return self.search(nums, float('-inf'), 0)

    ## the idea mentioned in the youtube video is that at each index
    ## we have the decision of either including the current item in our current subsequence and continue onto the next item
    ## OR we can exclude the current item and continue onto the next item
    ## and we'll recursively repeat this (either including or excluding the current item) and figure out the max between these two decision
    ## to determine the longest increasing subsequence
    def search(self, nums: List[int], prev, current) -> int:
    	## base case, if our current index is the length of the array, return 0
    	if (current == len(nums)):
    		return 0
    	include = 0	
		## if our current element is greater than our previous element we can make the decision to include it in our
		## subsequence
    	if (nums[current] > prev):
    		## pass in the current element down into prev, and increase the current index
    		include = 1 + self.search(nums, nums[current], current+1)
    	## in another recursive call, we'll figure out the total amount if we exclude the current element
    	exclude = self.search(nums, prev, current+1)
    	## then we take the max between the two to figure out which total was larger
    	return max(include, exclude)

 
            
        
        
        
               
                
        
