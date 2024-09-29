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
    def search(self, nums: List[int], target: int) -> int:
        """
        Revisited on 9/29/2024
        find the rotation point of the rotated sorted array:
        by comparing the number at the left and the number at the right to the number at mid,
        if the number at the right < nums[mid], we search right, as the rotation point should be
        in this section since we'd expect nums[right] > nums[mid].
        Otherwise, we'd search to the left.

        Once we figure out the rotation point, we'd essentially have two separate sorted arrays
        split by the rotation point. If we check if the target is in bounds of the right side,
        meaning the nums[rotationPoint] <= target <= nums[right], that means we search the right side,
        so the left would be rotationPoint, otherwise, we search the left side.
        
        """
        def findRotationPoint(left, right):
            mid = left + (right-left)//2
            if left >= right:
                return mid
            if nums[right] < nums[mid]:
                return findRotationPoint(mid+1, right)
            else:
                return findRotationPoint(left, mid)
        # perform regular binary search, where if the target < nums[mid],
        # we need to search left, otherwise, search right
        def findTarget(left, right):
            mid = left + (right-left)//2
            if (target == nums[mid]):
                return mid
            if (left >= right):
                return -1
            if target < nums[mid]:
                return findTarget(left, mid)
            else:
                return findTarget(mid+1, right)
        left = 0
        right = len(nums)-1
        rotationPoint = findRotationPoint(0, len(nums)-1)
        # if target is in bounds of the rotation point and the right side
        # search on the right side by setting left at the minIndex
        if nums[rotationPoint] <= target <= nums[right]:
            left = rotationPoint
        # otherwise, search on the left side by setting right to the minIndex
        else:
            right = rotationPoint
        return findTarget(left, right)
        

        
"""
revisited on 7/5/2023
approach:
find the index of the min element within the sorted rotated array
once we find that, we know that both the segment to the left and right
are sorted, so if the target element is in bounds of one of the left/right portions,
we do the binary search in that portion

recursive adaptation based on:
https://www.youtube.com/watch?v=QdVrY3stDD4&t=367s&ab_channel=NickWhite

O(LogN) time O(1) space
"""  
class Solution2:
    def findMinIndex(self, nums: List[int], left: int, right: int):
        # if left exceeds right, that means we've found the index
        # of the min element, the search is complete
        if left >= right:
            return left  
        mid = left + (right - left) // 2
        # this indicates the array is rotated, because
        # in a normal sorted array, the mid element should always be less than the right
        # in that case, continue the search down the right side
        if nums[mid] > nums[right]:
            return self.findMinIndex(nums, mid + 1, right)
        # otherwise, if it's less, that means we can find smaller values to the left
        # of mid, so continue the search down the left
        else:
            return self.findMinIndex(nums, left, mid)
        
    # perform regular binary search, where if the element is less than the midpoint,
    # we search the left side, otherwise we search the right
    def binarySearch(self, nums: List[int], left: int, right: int, target: int):
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if left >= right:
            return -1
        if target < nums[mid]:
            return self.binarySearch(nums, left, mid - 1, target)
        else:
            return self.binarySearch(nums, mid + 1, right, target)
        
    def searchHelper(self, nums: List[int], target: int) -> int:
        minIndex = self.findMinIndex(nums, 0, len(nums) - 1)
        left = 0 
        right = len(nums) - 1
        # if target is in bounds of the min index and the right side
        # search on the right side by setting left at the minIndex
        if nums[minIndex] <= target <= nums[right]:
            left = minIndex
        # otherwise, search on the left side by setting right to the minIndex
        else:
            right = minIndex
       	# perform regular binary search starting on one of the sides determined
       	# by the left/right indices set above  (either left to minIndex, or minIndex to right)
        return self.binarySearch(nums, left, right, target)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, target)

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