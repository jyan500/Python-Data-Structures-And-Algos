'''
https://leetcode.com/problems/merge-sorted-array/
https://www.youtube.com/watch?v=P1Ic85RarKY&list=PLQdWvigIOnscz0Fgps9PtnymVkvJrZylH&index=3&t=303s&ab_channel=NeetCode
'''

# 2/5/2024 
# O(N) Time, O(N) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        res = []
        copy = nums1
        while (i < m and j < n):
            if copy[i] < nums2[j]:
                res.append(copy[i])
                i += 1
            elif copy[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(copy[i])
                res.append(nums2[j])
                i += 1
                j += 1
        if j < n:
            for k in range(j, n):
                res.append(nums2[k])
        elif i < m:
            for k in range(i, m):
                res.append(copy[k])
        for i in range(len(res)):
            nums1[i] = res[i]
        
        
"""
revisited on 7/28/2023
"""
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if i == m:
                nums1[i] = nums2[j]
                j+=1
                # shift the value of m so that we know where to start replacing the padded zeroes
                m+=1
            # if the value at nums1[i] is greater, then the value of nums2 will replace i,
            # and all other values get shifted over to the right, replacing one padded zero at the end
            elif nums1[i] > nums2[j]:
                # shift all elements after i to the right by 1
                # make a copy of nums array before we change it so we can set
                # the previous elements
                copy = nums1.copy()
                for k in range(i+1, len(copy)):
                    nums1[k] = copy[k-1] 
                nums1[i] = nums2[j]
                j+=1
                # shift the value of m so that we know where to start replacing the padded zeroes
                m+=1
            # if the value of the pointer at nums1 is less than nums2, keep incrementing 
            elif nums1[i] < nums2[j]:
                i+=1
            # if the value of the pointers are equal, add the element and shift the remaining to the right,
            # replacing one padded zero at the end
            elif nums1[i] == nums2[j]:
                # make a copy of nums array before we change it so we can set
                # the previous elements
                copy = nums1.copy()
                for k in range(i+1, len(copy)):
                    nums1[k] = copy[k-1]
                nums1[i] = nums2[j]
                i+=1
                j+=1
                # shift the value of m so that we know where to start replacing the padded zeroes
                m+=1
                
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
            
            
         

