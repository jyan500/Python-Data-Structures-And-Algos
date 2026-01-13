"""
Revisited 1/12/2026
https://leetcode.com/problems/4sum/
Basically the same as 3 sum:
1) 
Sort the list

the idea is that you hold two variables constant at first in the 2 nested for loops,
and then run the two pointer while loop, one at the element to the left
of the last variable we held constant (j), and one at the end of the list.

2) Move the left and right pointers inwards towards each as long as the left index < right index
If the total sum of the two variables we held constant, plus the left and right pointer values is the target,
we add it to a set. We then move both pointers inwards to advance the while loop.

3) Otherwise, if our total sum is bigger than the target, we move the right pointer inwards since our number is too big
and we need a smaller number.

4) If our total sum is too small, we move the left pointer inwards since our number is too small and we need a bigger number

5) Set is converted back into a list at the end

Time Complexity:
O(N^3 + NLogN)

Space: O(number of quadruplets)

"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                """         
                note that the conditional must be l < r and not l <= r so that you don't pick the same value
                twice, as part of the problem states that the values chosen must be distinct per index
                """
                while (l < r):
                    totalSum = nums[i] + nums[j] + nums[l] + nums[r]
                    # if the sum is too big, we need to shrink the right side
                    # to get a smaller number
                    if totalSum > target:
                        r -= 1
                    # if the sum is too small, we need to increase the left side
                    # to get a bigger number
                    elif totalSum < target:
                        l += 1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        r -= 1
                        l += 1
        return list(res)