"""
Concept:
Prefix Sum
https://leetcode.com/problems/range-sum-query-immutable/

1) Pre-calculating the prefix sum in the constructor allows the sumRange function to be O(1)
2) In our sumRange, we just need to take the value of prefix_sum[right] and subtract from prefix_sum[left-1],
which would essentially subtract away the sum of the numbers we're not including. Note it's left - 1 because
we still want to include the sum AT index left

Example:
-2 0 3 -5 2 -1

prefix version:
-2 -2 1 -4 -2 -3

if we calculate from i = 0 to 2

prefix_sum[right] = prefix_sum[2]
this would be 1

if we calculate from i = 2 to i = 5

prefix_sum[right] - prefix_sum[left-1]

prefix_sum[5] - prefix_sum[2-1]

-3 - (-2) = -1

If we manually calculate this range, we can confirm this is correct
looking at the original nums

3 + -5 + 2 + -1 = -2 + 2 + - 1 = -1



"""
 class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0 for i in range(len(nums))]
        self.prefix[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 >= 0:
            return self.prefix[right] - self.prefix[left-1]
        else:
            return self.prefix[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)