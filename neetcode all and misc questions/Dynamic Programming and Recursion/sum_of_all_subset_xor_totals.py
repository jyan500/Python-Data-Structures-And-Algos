"""
https://leetcode.com/problems/sum-of-all-subset-xor-totals/
Approach:
same approach as subsets I on leetcode, using the knapsack theorem, except after getting all subsets,
perform XOR on each element and save the sum of all the XOR elements.

Time Complexity:
O(2^N), exponential, since at each point, there's two decision trees you can make (either accepting the current element,
or not accepting it)

Space: O(N) recursion stack
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        N = len(nums)
        def search(i, cur):
            if i >= N:
                subsets.append(cur)
                return
            search(i+1, cur+[nums[i]])
            search(i+1, cur)
        search(0, [])
        res = 0
        for subset in subsets:
            xor = 0
            for num in subset:
                xor ^= num
            res += xor
        return res