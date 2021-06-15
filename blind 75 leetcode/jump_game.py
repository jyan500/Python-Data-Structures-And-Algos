'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

https://leetcode.com/problems/jump-game/
explanation: https://www.youtube.com/watch?v=Zb4eRjuPHbM&ab_channel=NickWhite
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastKnownGoodPosition = len(nums) - 1
        ## traverse through array backwards starting from last index
        for i in range(len(nums)-1, -1, -1):
            ## if the current index plus the max jump value is greater than the last index
            if (i + nums[i] >= lastKnownGoodPosition):
                ## we can set the last good position to be the current index since 
                ## we know that we'll be able to reach the end through this current value of "i"
                lastKnownGoodPosition = i
        ## if we're at the first index in the array, we know that we're able 
        ## to reach the last item from the first
        return lastKnownGoodPosition == 0