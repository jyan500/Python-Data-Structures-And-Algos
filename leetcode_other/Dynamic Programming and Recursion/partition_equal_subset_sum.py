"""
https://leetcode.com/problems/partition-equal-subset-sum/
https://www.youtube.com/watch?v=ZFuagJEpeEU&ab_channel=leetcodeWithCarter
https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask

Time complexity: O(N*sum), where N is len(nums) and sum is the sum(nums)
Space complexity: O(N*sum) for the memoization dict
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # one trick for this problem:
        # the target sum that the subsets should sum to 
        # is total sum / 2, if this isn't a whole number (i.e total % 2 != 0)
        # we cannot logically split the 
        # array into subsets that would sum up to this target since
        # every number in the array is a whole number and not a decimal

        self.total = sum(nums)
        if self.total % 2 != 0:
            return False
        self.memo = dict()
        def dfs(i, amount, nums):
            if (amount, i) in self.memo:
                return self.memo[(amount, i)]
            if i >= len(nums) or amount >= self.total/2:
                return amount == self.total/2
            # knapsack type relation
            # you either:
            # 1) pick the current number to contribute to our total OR
            # 2) skip over it
            # this recursion is finding one "half" of the subset that adds up to our total/2,
            # which proves the existence of both subsets that add up to total (since if we find one half, and our case of self.total % 2 == 0, proves that
            # another half must exist)
            # we memoize both the current amount AND i and not just amount OR
            # i because we could get arrive at the same amount via different combinations
            # of numbers
            res = dfs(i+1, amount + nums[i], nums) or dfs(i+1, amount, nums)
            self.memo[(amount, i)] = res
            return res
        
        return dfs(0, 0, nums)
            