"""
https://leetcode.com/problems/find-peak-element/
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Binary Search:
        https://neetcode.io/solutions/find-peak-element
        
        The problem states that: nums[-1] = nums[n] = -∞
        which means that say if had 
        [1 2 3 4 5],
        5 is considered a peak element because it's greater than 4, and also greater than its neighbor
        outside of the boundaries of the array

        same with
        [5 4 3 2 1]
        5 is considered a peak element because it's greater than 4, and also greater than its neighbor 
        outside of the boundaries of the array
    
        The key to the problem is recognizing this fact, and then checking to see if the element to the right
        is greater than the current element. If so, that means this current element CANNOT be the peak element,
        HOWEVER, the next element COULD be a peak element. If the pattern continues where the element
        to the right is greater than the current, we're guaranteed to run into the peak element at the end of the array.

        Same logic applies if the array is monotonically decreasing,
        If the element to the right is less than the current, we have to search the left side instead,
        as this means the the element to the left is greater than the current, so the peak element
        is on the left side (with the last possible peak element being the element at index 0)

        Time: O(LogN)
        Space: O(LogN) (recursive stack)


        """
        left = 0
        right = len(nums)-1
        def search(left, right):
            mid = left + (right - left)//2
            if left >= right:
                return left
            if nums[mid+1] > nums[mid]:
                return search(mid+1, right)
            return search(left, mid) 

        # def search(left, right, nums):
        #     mid = left + (right-left)//2
        #     if left >= right:
        #         return left
        #     # if we're between the second to last index, or we're at index 1
        #     if mid >= 1 and mid <= len(nums) - 2:
        #         if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
        #             return mid
        #         if nums[mid-1] > nums[mid]:
        #             return search(left, mid, nums)
        #         if nums[mid+1] > nums[mid]:
        #             return search(mid+1, right, nums)
        #     # if we're at the 0 index
        #     if mid == 0:
        #         # if we're at 0 index, and the number to the right is less,
        #         # this is considered a peak element, since this element is automatically
        #         # greater than it's non-existing neighbor
        #         if nums[mid+1] < nums[mid]:
        #             return mid
        #         # if we're not at the peak element, we search the right side
        #         else:
        #             return search(mid+1, right, nums)
        #     # if we're at the last index
        #     if mid == len(nums) - 1:
        #         # if we're at the last index, and the number to the left is less,
        #         # this is a considered a peak element, since this element is automatically
        #         # greater than it's non-existing neighbor
        #         if nums[mid-1] < nums[mid]:
        #             return mid
        #         # if we're not at the peak element, we search the left side
        #         else:
        #             return search(left, mid, nums)
                
        return search(left, right, nums)