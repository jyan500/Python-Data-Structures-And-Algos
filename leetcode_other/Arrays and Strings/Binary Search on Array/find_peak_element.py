"""
https://leetcode.com/problems/find-peak-element/
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=kMzJy9es7Hc&ab_channel=NeetCodeIO
        
        An important fact about this problem is that 
        if we have a monotically increasing array,
        1, 2, 3, 4, 5
        
        the last element 5 is a peak element as defined by the problem,
        because 5 > 4, and 5 is greater than the neighbor to the right of it
        that doesn't exist
        
        Therefore, we can apply binary search, and the way we determine which side
        to search on is to see which side is greater. If both sides are greater than the neighbor,
        we can search either side. However, if we run into an element where both neighbors are smaller
        than the element, that'd be a peak element.
        
        """
        left = 0
        right = len(nums)-1
        
        def search(left, right, nums):
            mid = left + (right-left)//2
            if left >= right:
                return left
            # if we're between the second to last index, or we're at index 1
            if mid >= 1 and mid <= len(nums) - 2:
                if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                    return mid
                if nums[mid-1] > nums[mid]:
                    return search(left, mid, nums)
                if nums[mid+1] > nums[mid]:
                    return search(mid+1, right, nums)
            # if we're at the 0 index
            if mid == 0:
                # if we're at 0 index, and the number to the right is less,
                # this is considered a peak element, since this element is automatically
                # greater than it's non-existing neighbor
                if nums[mid+1] < nums[mid]:
                    return mid
                # if we're not at the peak element, we search the right side
                else:
                    return search(mid+1, right, nums)
            # if we're at the last index
            if mid == len(nums) - 1:
                # if we're at the last index, and the number to the left is less,
                # this is a considered a peak element, since this element is automatically
                # greater than it's non-existing neighbor
                if nums[mid-1] < nums[mid]:
                    return mid
                # if we're not at the peak element, we search the left side
                else:
                    return search(left, mid, nums)
                
        return search(left, right, nums)