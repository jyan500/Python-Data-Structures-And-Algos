'''
https://leetcode.com/problems/merge-sorted-array/
https://www.youtube.com/watch?v=P1Ic85RarKY&list=PLQdWvigIOnscz0Fgps9PtnymVkvJrZylH&index=3&t=303s&ab_channel=NeetCode
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        ## start merging in reverse order
        while (m > 0 and n > 0):
            ## if the number if nums1 is greater than the number in nums2
            if (nums1[m-1] > nums2[n-1]):
                ## set the element that the "last" index is pointing to be equal to nums1[m]
                nums1[last] = nums1[m-1]
                ## decrement m
                m-=1
            ## if the number nums1 is less than number in nums2
            else:
                ## set the element to be equal to nums2
                nums1[last] = nums2[n-1]
                ## decrement n
                n -= 1
            last -= 1
        
        ## fill the rest of nums1 with leftover nums2 elements
        while (n > 0):
            nums1[last] = nums2[n-1]
            n-=1
            last-=1
            
            
         

