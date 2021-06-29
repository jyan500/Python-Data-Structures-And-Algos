'''
https://leetcode.com/problems/house-robber-ii/
Note that concept for the solution is explained here, but the video itself does a bottom-up approach for its solution
but I wanted to stick with top-down since it makes more sense to me:
https://www.youtube.com/watch?v=mFT2bIFKUFE&t=461s&ab_channel=NareshGupta
'''

class Solution:
    ## the key difference between House Robber I and House Robber II is that...
    ## if we rob the last house in the list, we cannot rob the first
    ## and if we rob the first house, we cannot rob the last
    ## so essentially we have two cases, and we need to find the max amount we can steal in either case
    ## and compare them

    ## 1) we ignore the last house in the list, slicing out the last element and doing the recursion
    ## trying to find the max amount we can rob from 0...len(nums)-1, starting at len(nums)-1

    ## 2) we ignore the first house in the list, slicing out the first element and doing the recursion
    ## trying to find the max amount we can rob from 1 ... len(nums)-1, starting at len(nums)-1

    ## we just need to find the max between these two calls to the "search" function
    
    def rob(self, nums: List[int]) -> int:
        memo1 = dict()
        memo2 = dict()
        ## since we're doing list slicing, we need to keep in mind for edge cases here
        if (len(nums) <= 2):
            return max(nums)
        if (len(nums) == 0):
            return 0
       
        
        return max(self.search(nums[:len(nums)-1], len(nums)-1,memo1), self.search(nums[1:], len(nums)-1, memo2))

    def search(self, nums, i, memo) -> int:
        key = i
        if (key <= 0):
            memo[key] = 0
            return 0
        elif (key in memo):
            return memo[key]
        else:
            current_house = nums[i-1] + self.search(nums, i-2,memo)
            next_house = self.search(nums, i-1,memo)
            memo[key] = max(current_house, next_house)
            return memo[key]
