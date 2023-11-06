"""
https://www.youtube.com/watch?v=xCsIkPLS4Ls&ab_channel=NeetCode

This is a tricky problem, relies on mathematical knowledge in that subsequences
are calculated via 2^x, as well as a greedy approach, because within our subsequence,
we're always bounded by the maximum value, since we'll never be able to add a value
greater than our max to the subsequence without going past the target. 

1) sort the array first
2) Find index r where the sum of our smallest number (l) and the greatest (r) < target, using the while loop which
will continue until it meets this condition and gives us the right r value
3) if l <= r (meaning we haven't gone too far with decrementing the right side), we calculate the amount of subsequences using
2^(r-l), and then we mod that amount and add to our result.

See the neetcode link above for a better explanation.

Time Complexity: O(NLogN)
Space: O(1)

"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10**9 + 7
        r = len(nums) - 1
        for l in range(len(nums)):
            # figure out the stopping point at which we can't include
            # any more elements without going past the target
            while (nums[l] + nums[r] > target and l <= r):
                r -= 1
            # if we haven't gone too far
            if l <= r:
                # the amount of subsequences is always equal to 2^(r-l), 
                # since the first element we must always include, so the difference
                # between the left and right pointers will give us the remaining amount
                # of numbers that can be chosen
                amt = 2 ** (r - l)
                res += amt
                # mod the result as this a requirement for the problem to avoid
                # res from becoming too big
                res %= mod
                
        return res