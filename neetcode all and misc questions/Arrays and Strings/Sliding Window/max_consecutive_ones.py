class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        maxAmt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
                maxAmt = max(cur, maxAmt)
            else:
                cur = 0
        return maxAmt