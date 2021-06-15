'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.


## concept
## https://www.youtube.com/watch?v=IQyJX5ddEx0&ab_channel=%E5%B1%B1%E6%99%AF%E5%9F%8E%E4%B8%80%E5%A7%90
## 1. Find index of peak element (also known as the inflection point), where the peak element is the number where the elements to the left are
## smaller, but the elements to the right of it are not bigger, but smaller! In that case, this would break
## the sorted order, but then we would know that the array was rotated around this point.
## 2. Because the element to the right of the peak element is the smallest, just return the element at index peak_index + 1.
'''

class Solution:
    def findPeakIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if (len(nums) == 1):
            return 0
        if (nums[0] < nums[-1]):
            return len(nums) - 1
        ## find the peak element
        while (left <= right):
            mid = (left + right) // 2
            ## numbers to the right of mid are smaller, that means that we've found the peak element, return the index
            if (nums[mid] > nums[mid+1]):
                return mid
            elif (nums[left] <= nums[mid]):
                left = mid + 1	
            else:
                right = mid - 1
        return 0

    def findMin(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        ## find the peak index, which represents the largest element in the list
        ## because the list is already sorted, the smallest element should be one index to the right in the list
        ## which is peak_index + 1
        peak_index = self.findPeakIndex(nums)
        ## if the peak index is the last index (which means the list was not rotated), just return the first item in the list
        if (peak_index == len(nums) - 1):
            return nums[0]
        return nums[peak_index + 1]
