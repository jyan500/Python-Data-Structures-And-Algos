'''
https://leetcode.com/problems/longest-increasing-subsequence/solution/
https://www.youtube.com/watch?v=CE2b_-XfVDk&t=324s&ab_channel=TusharRoy-CodingMadeSimple
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
 
            
        
        
        
               
                
        
