'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

https://leetcode.com/problems/jump-game/
explanation: https://www.youtube.com/watch?v=Zb4eRjuPHbM&ab_channel=NickWhite
'''

"""
Revisited 8/29/2023
This should be an O(N^2) solution but it TLE's on leetcode
1) Basically visits every position possible based on the jump value on each index i,
memoizes if the end of the array can be reached from a given index i 

The greedy solution (O(N)) is accepted
https://www.youtube.com/watch?v=Yan0cv2cLy8&ab_channel=NeetCode
"""
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        self.memo = dict()
        def helper(nums, i):
            if i in self.memo:
                return self.memo[i]
            if i >= len(nums)-1:
                self.memo[i] = True
                return True
            if nums[i] == 0:
                self.memo[i] = False
                return False
            numJumps = nums[i]
            for j in range(i+1, i+numJumps+1):
                if helper(nums, j):
                    self.memo[j] = True
                    return True
            self.memo[i] = False
            return False
        return helper(nums, 0)

    def canJumpGreedy(self, nums: List[int]) -> bool:
        # starting from the back of the array,
        # can we reach our "goal post" based on our current position?
        goalPost = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            # can we reach the index of our goal post based on the max amount of 
            # jumps that can be taken?
            if i + nums[i] >= goalPost:
                # if so, set the goal post to this position i, since we know we can reach
                # the end from this position, so our new goal is to reach this position i
                # instead of the end
                goalPost = i
        # this indicates we can reach the end element from the first element
        return goalPost == 0

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