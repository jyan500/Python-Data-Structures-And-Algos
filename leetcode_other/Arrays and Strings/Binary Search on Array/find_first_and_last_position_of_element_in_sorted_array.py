'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Concept:
1) Apply binary search to find the index of our target element, call it target_index (to see if the target element is present in the array)
	We will also keep track of a res array, initialized to be [-1,-1], where res[0] is the first position of the element and res[1] is the last position of the elemtn

2) Once we find the target element, we can perform another binary search.
by checking the half of the array from index 0 to our target_index to get the first position of the element
	-within our binary search here, if our midpoint element is equal to our target, we will update res[0],
	so that if we narrow down our search but midpoint element is still the same as our target, we can update
	res[0] again to update our min value
	- however, if our midpoint element is less than our target, we need to adjust to search the right half
		since we've "overshot" and we need to search the other way

Similarly, we can perform another binary search by checking the half of the array
from target_index to the end of the list to get the last position of the element
	-within our binary search here, if our midpoint element is equal to our target, we will update res[1],
	so that if we narrow down our search but midpoint element is still the same as our target, we can update
	res[1] again to update our max value
	- however, if our midpoint element is greater than our target, we need to adjust to search the left half instead
	since we've "overshot" and need to search the other way

'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ## binary search
        left = 0
        right = len(nums)-1
        res = [-1,-1]
        ## perform an initial binary search to check if the target element exists in the list
        ## if so, save the index as the 0 and 1 index of our res list (representing the starting and ending index of our target value)
        target_index = -1
        while (left <= right):
            mid = (left + right)//2
            print(mid)
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                res[0] = mid
                res[1] = mid
                target_index = mid
                break
        
        ## if we didn't find the target, just return [-1,-1]
        if (target_index == -1):
            return res
        ## once we found a target index, we can find the starting point (min) of our target value
        ## by searching the left half of the array, from 0 to our target index
        left = 0
        right = target_index
        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] == target):
                ## if we see the target element, update the min
                ## as we continue to search the left, our min (res[0]) will decrease
                ## if we see the target element again
                res[0] = mid
                ## search the left half by decreasing the right
                right = mid-1
            ## if we see an element that is less than the target,
            ## we need to search the right half this time to find the target element
            if (nums[mid] < target):
                left = mid+1
        ## once we found a target index, we can find the ending point (max) of our target value
        ## by searching the right half of the array, from our target_index to the end of the list
        left = target_index
        right = len(nums)-1
         ## once we found a target index, we can find the starting point (min) of our target value
        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] == target):
                ## if we see the target element, update the max
                ## as we continue to search the right, our max (res[1]) will increase
                ## if we see the target element again
                res[1] = mid
                ## search the right half by increasing the left pointer
                left = mid+1
            ## if we see an element that is greater, we need to search the left half this time
            if (nums[mid] > target):
                right = mid-1
        return res

        '''
        nums = [5,6,7,7,7,7,8,8,8,8,10,12]
        initial binary search will give us index of 8
        
        
        '''
        
        
        
        '''
        nums = [5,7,7,8,8,10]
        target = 8
        left = 0
        right = 5
        
        1st iter
        mid = (0+5)//2 = 2
        nums[mid] = nums[2] = 7
        7 < 8, so search the right half
        left = mid + 1, left = 3
        
        2nd iter
        mid = (3+5)//2 = 4
        nums[mid] = 8
        8 == 8, so target is found
        but we've only found one 8, what about the others?
        
        change our approach?
        used binary search
        once we've found a target element, we do binary search to find the min,
        by resetting left to be 0 again, but right to be the target_index
        and then do another binary search to find the max,
        setting left to be the target index and right to be length of the list - 1
        '''