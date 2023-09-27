"""
https://leetcode.com/problems/3sum-closest/
Time Complexity: O(N^2)
Space: O(1)

Key Concepts:
Similar to the regular two sum,
1) Sort the input array and keep track of the minimum distance and result.
2) use two pointers, where we hold one element constant i
and then use the left and right pointers going inwards, 
where if our sum < target, increment left (since that means our value is too small, and we need a larger number)
where if our sum > target, decrement right (since that means our value is big, and we need a smaller number)

3) during each iteration while we figure out a sum that's incrementally closer to our target,
we calculate the distance between our sum and target by taking the absolute value, and then
seeing if that is smaller than the minimum distance. If so, update min distance and our result
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        minDistance = float("inf")
        res = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                s = nums[i] + nums[left] + nums[right]
                if target == s:
                    return s
                if s < target:
                    left += 1
                if s > target:
                    right -= 1
                distance = abs(target - s)
                if distance < minDistance:
                    minDistance = distance
                    res = s
        return res