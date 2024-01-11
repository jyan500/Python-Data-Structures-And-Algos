'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''

"""
Revisited on 8/24/2023
Key Concept:
1) To figure out the new index for i after rotation,
add the rotation factor k to the current index, and then mod by
the length of the array 

2) If a problem requires rotation (i.e something that wraps around from the end to beginning,
like array rotation, time (AM/PM) related problems, or number related problems,
think of using mod (%) operator)

1 2 3 4 5 6 7
k = 3

i.e for element 5, i = 4
4 + 3 = 7
7 % 7 = 0

for element 6, i = 5
5 + 3 = 8
8 % 7 = 1

output should be 
5 6 7 1 2 3 4

O(N) time
O(N) space
"""
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        copy = nums.copy()
        for i in range(len(copy)):
            newIndex = (i + k) % n
            nums[newIndex] = copy[i]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        ## store the value of the list as the key and the new rotated index as the value
        ## concept:
        ## find the index of the first item that needs to be shifted
        ## i.e [1,2,3,4,5,6,7], k = 3
        ## the first item will be 5 in this case
        ## find the index of that item (which is -3)
        ## take everything after index of -3 to the end of the list and add it to everything before index of -3
        ## set the resulting list to be the slice of the original nums (in order to count as modifying in place)
        ## if k is greater than the length of the list
        ## re-calculate k using mod 
        if (k > len(nums)):
            k = k % len(nums)
        nums[0:len(nums)] = nums[-k:] + nums[:-k]

    def rotate(self, nums: List[int], k: int) -> None:
    	## O(N) space
	    # this was a solution that I must've written a long time ago, but I don't remember how it works
    	if (len(nums) > 1):
            new_list = []
            for i in range(len(nums)):
                if (i+k < len(nums)):
                    new_list.insert(i+k, nums[i])
                else:
                    new_list.insert((i+k) % len(nums), nums[i])
            for i in range(len(new_list)):
                ## this does not work because pop modifies the length of the list, throwing
                ## off the indices
                ## nums.insert(i, nums.pop(nums.index(new_list[i])))
                ## below is much more efficient since we simply just overwrite the values of the 
                ## previous indexes
                nums[i] = new_list[i]