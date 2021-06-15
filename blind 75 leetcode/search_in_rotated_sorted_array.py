'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, 
nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.
Note: Solution MUST BE IN O(LogN)


## concept
## https://www.youtube.com/watch?v=IQyJX5ddEx0&ab_channel=%E5%B1%B1%E6%99%AF%E5%9F%8E%E4%B8%80%E5%A7%90
## 1. Find index of peak element (also known as the inflection point), where the peak element is the number where the elements to the left are
## smaller, but the elements to the right of it are not bigger, but smaller! In that case, this would break
## the sorted order, but then we would know that the array was rotated around this point.
## 2. Apply binary search on the subarray, if the target is smaller than the peak element, search the left
## if the target is bigger, search right.
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

    def binarySearch(self, nums: List[int], left : int, right : int, target : int) -> int:
    	while (left <= right):
            mid = (left + right) // 2
            print('mid index: ', mid)
            print('value of mid:', nums[mid])
            if (nums[mid] == target):
                print('returned mid')
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    	return -1

    def search(self, nums: List[int], target: int) -> int:
        if (len(nums) == 0):
            return -1
        peak_index = self.findPeakIndex(nums)
        ## if the target is less than the number at the peak index, search the left half
        if (peak_index >= 0 and target >= nums[0] and target <= nums[peak_index]):
            return self.binarySearch(nums, 0, peak_index, target)
        else:
            ## search the right half
            return self.binarySearch(nums, peak_index+1, len(nums)-1, target)