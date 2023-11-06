"""
https://www.youtube.com/watch?v=Wmb3YdVYfqM&ab_channel=NeetCode
Key Concept:
1) Sort first so that we can guarantee what the ordering of the elements will be
2) Realizing that to ensure that i is not equal to the average of it's neighbors,

either A) both neighbors are larger than the value at i OR B) both neighbors are smaller than the value at i
for example:

1 2 3 4 5 

If you take the first half of the input array (either len(nums)//2 for even length arrays, or len(nums)//2 + 1 for odd length)
and space it out, then put the second half in the remaining spots

1 _ 2 _ 3


1 4 2 5 3

You can see that both values to the left and right of 4 are smaller, 
same with 5.

This is a valid answer.



"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0 for i in range(len(nums))]
        k = 0
        mid = len(nums)//2 if len(nums) % 2 == 0 else len(nums)//2 + 1
        for i in range(mid):
            if k < len(nums):
                res[k] = nums[i]
                k += 2
        k = 1
        for i in range(mid, len(nums)):
            if k < len(nums):
                res[k] = nums[i]
                k += 2
        return res
            
        