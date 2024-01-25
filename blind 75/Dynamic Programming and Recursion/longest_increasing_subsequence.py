'''
https://leetcode.com/problems/longest-increasing-subsequence/solution/
DP Solution
https://www.youtube.com/watch?v=CE2b_-XfVDk&t=324s&ab_channel=TusharRoy-CodingMadeSimple

Top Down Solution
https://www.youtube.com/watch?v=ekKYRYFEm9w&list=PLQdWvigIOnscz0Fgps9PtnymVkvJrZylH&index=5&ab_channel=AnuragVishwa
'''

"""
Revisited on 8/21/2023
adapted from: 
https://leetcode.com/problems/longest-increasing-subsequence/discuss/1124603/Top-DownBackTrackingMemoization
Top down approach:
1) Find increasingly larger numbers within the array
2) when one is found, make a recursive call to find the next greatest number, where the result of this
recursive call will be the max length subsequence that can be found starting at this number. 
Pass in the index at which this element was found.
3) For memoization, we store the max length mapped to each index of nums.
4) Our "base case" is technically when we pass in an element, and no greater number is found.
In that case, the length of the subsequence is just 1, so we return the length

In the leetcode problem, it passes in the index instead of a smaller slice of the array which is smart
to save space. That way, we can just key into the original nums array and know the index which makes
memoization much easier.

Time complexity: O(N^2) (one loop per element, and then additional recursive calls from start to n-1)
Space Complexity: O(N^2) recursive calls

Example:
nums = [10, 9, 2, 5, 3, 7, 101, 18]

1) 
self.memo = {}
first call:
starting from i = 0
10

loops through 9 ... 18
finds 101 > 10

num = 101
start = 6
dfs(6, 101)

cannot find a number greater than 101,
therefore at index 6, the greatest length we get is 1

self.memo = {6: 1}

2) 
Back to 10, we store in our memo index 0 mapped to length 2, exit and now run dfs starting from i = 1 (9)
9

loops through 2 ... 18
finds 101
we already found 101 in our memoization, since index 6 is in memo
return 1

therefore, the max is now 1 + self.memo[6] which is 2
store memo, which is {1: 2} 

goes back to loop, finds 18

at 18, max length is 1 since there's no other elements past it
stores index 7 mapped to length 1 in self.memo, {7: 1}

self.memo = {0: 2, 6:1, 7:1, 1: 2}

3) 
exits, goes back to start running DFS on i = 2 now (element 2)
it will now loop through
5 ... 18
finds 5, does a recursive call

loops through 3 ... 18
finds 7, does a recursive call

loops through 101 ... 18
finds 101, this is already in our memoization so returns 1
1+1 = 2 (current subsequence is 7, 101)

finds 18, this is also already in our memoization so returns 1
1+1 = 2 

We store length 3 for the index 4
self.memo = {0: 2, 6:1, 7:1, 1:2, 4: 3}

goes back to 5 ... 18, adds one to the length
we store length 4 for the index2 
self.memo = {0: 2, 6:1, 7:1, 1:2, 4: 3, 2: 4}

This same process continues until all i ... n - 1 are examined,
the final answer should be 4, with the longest subsequence here
being 2, 3, 7, 101 OR 2, 5, 7, 101


"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Revisited on 1/25/2024
        O(N^2) Time Complexity (Same as above)
        1) Approach, find all possibilities, pick the maximum length at each subproblem
        10 9 2 5 3 7 101 18
        2 3 7 101
        
        10 101
        9 101
        
        2 3 OR 2 7
        Note that at 2, we have a choice of picking either 3 as the next element, OR
        7 as the next element, these are both valid increasing subsequences,
        so this is the first instance of the recursive sub problem. You can see 
        the decision tree that you'd have to make for each subsequent increasing number.
        
                           2 3 OR 2 7
                           
            2 3 7 OR 2 3 101           2 7 101 OR 2 7 18
                     
         2 3 7 18 OR 2 3 7 101                       
         
        
        
        """
        # we can store at a given index,
        # what's the longest increasing subsequence we can make at that index?
        # this will cut down on repeated subproblems
        self.memo = dict()
        def search(i):
            maxLen = 1
            if i in self.memo:
                return self.memo[i]
            for k in range(i, len(nums)):
                # if we find a number greater than our 
                # current number that also has a greater index,
                # this is a subproblem, because there's a chance
                # we could find multiple numbers greater than our current number,
                # which would be different subsequences, so do a recursive call.
                if nums[k] > nums[i]:
                    maxLen = max(1 + search(k), maxLen)
            self.memo[i] = maxLen
            return self.memo[i]
        
        maxLen = 1
        # for each i, we want to find a number greater than nums[i]
        for i in range(len(nums)):
            maxLen = max(search(i), maxLen)
        return maxLen


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memo = dict()
        self.nums = nums
        def dfs(start, num):
            if start in self.memo:
                return self.memo[start]
            length = 1
            for i in range(start, len(self.nums)):
                if self.nums[i] > num:  
                    length = max(length, 1 + dfs(i+1, self.nums[i]))            
            self.memo[start] = length
            return length
        maxLength = 0
        for i in range(len(self.nums)):
            maxLength = max(dfs(i+1, nums[i]), maxLength)
        return maxLength

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

 
            
        
        
        
               
                
        
