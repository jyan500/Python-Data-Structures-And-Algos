'''
https://leetcode.com/problems/house-robber-ii/
Note that concept for the solution is explained here, but the video itself does a bottom-up approach for its solution
but I wanted to stick with top-down since it makes more sense to me:
https://www.youtube.com/watch?v=mFT2bIFKUFE&t=461s&ab_channel=NareshGupta
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Revisited 1/24/2024
        Approach mentioned in:
        https://www.youtube.com/watch?v=rWAJCfYYOvM&ab_channel=NeetCode

          3        
        2   2
        
        You can never rob
        0 AND n - 1, where n = len(nums)
        
        Recurrence Relation:
        1) Rob house at i, next i is i + 2
        2) Skip i and rob house at i + 1
        
        max(nums[i] + f(i+2), f(i+1))
        
        The trick is that we can re-use the same recurrence relation as House Robber I,
        except we run the function twice, where we only rob the houses from 1 ... n - 1
        and 0 ... n - 2, since this meets the condition where we can't rob 0 and n - 1 together

        [2, 3, 2, 4]
        
        first run through goes through [3, 2, 4], where we don't have the option of robbing 0
        second run through goes through [2, 3, 2], where we don't have the option of robbing n - 1
       	
       	We then take the max between both of these function calls to get the max amount we can rob
       	without breaking the constraints 
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if len(nums) == 1:
            return nums[0]
        self.memo = dict()
        def search(i, nums):
            if i >= len(nums):
                return 0
            if i in self.memo:
                return self.memo[i]
            self.memo[i] = max(nums[i] + search(i+2, nums), search(i+1, nums))
            return self.memo[i]
        
        allButFirstHouse = search(0, nums[1:])
        self.memo = dict()
        allButLastHouse = search(0, nums[:len(nums)-1])
        return max(allButFirstHouse, allButLastHouse)

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
