from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    https://www.lintcode.com/problem/508/
    """
    def wiggle_sort(self, nums: List[int]):
        """
        https://youtu.be/vGsyTE4s34w
        Note, there's a way to do this in O(N) Time which is the most optimized,
        see the neetcode link above.
        
        O(NLogN) Time
        O(1) Space
        sort the array in place first
        swap elements in pairs, starting on index i = 1
        until the last element nums.length - 1

        i.e
        1 2 3 4 5 6
        swaps index i = 1 and i = 2
        1 3 2 4 5 6
        swaps i = 3 and i = 4
        1 3 2 5 4 6
        this is actually a valid answer because
        nums[0] <= nums[1] >= nums[2] <= nums[3] , etc
        """

        nums.sort()
        i = 1
        while (i < len(nums)-1):
            # swap the current element and next
            nums[i],nums[i+1] = nums[i+1], nums[i]
            i+=2

        """
        O(N^2) Time
        O(N) Space
        copy the array and alternate between the smallest element of the list and the largest,
        as you loop through the original array and reset the elements. As you pick an element from the copy,
        pop it after so you get the next biggest/smallest element in the list
        """
        # copy = nums.copy()
        # for i in range(len(nums)):
        #     element = min(copy) if i % 2 == 0 else max(copy)
        #     nums[i] = element
        #     copy.pop(copy.index(element))
        