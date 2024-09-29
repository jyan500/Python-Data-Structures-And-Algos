class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Revisited 9/29/2024
        https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
        in the rotated sorted array, there's always an index where the number immediately 
        to the right is larger than the number on the left like normal, 
        but the number to the left is larger than the number on the right, which indicates
        this is the rotation point.
        i.e 
        6,7,8,9,10,11,3,4,5
        here the rotation point is 3, normally the numbers on the left of 3
        should be less than 3 in normal ascending order, but in this case it is greater.

        In order to find this number in LogN, use binary search. But after find the mid point,
        compare it to the numbers at the LEFT pointer and the numbers at the RIGHT pointer, since otherwise,
        you wouldn't know which section of the array to search without making this comparison (since
        if you do the numbers of mid - 1 and mid + 1, you might get into a section where it's valid both ways
        and not know which way to look). 
        Also we know that if the number at the right pointer is less than nums[mid],
        then we look to the right, since the rotation factor should be in that section of the array,
        as we'd expect nums[right] to be greater than nums[mid], otherwise, we'd search to the left.
        
        In a case where the array is not rotated at all (or is rotated at a factor of the length of the array,
        which would just create the same array as if it were not rotated at all),
        the number at left is less and the number at right is greater all the time, 
        we'd just search the left side repeatedly

        for example, above. L starts out at 0, R is at 8
        6,7,8,9,10,11,3,4,5
        mid = L + (R - L)//2
        0 + (8//2) = 4
        nums[4] is 10
        here, the number on nums[0] is 6, but nums[8] is 5, which is also less.
        In that case, we have to search to the right, as the rotation factor would be
        that half of the array
        6,7,8,9,10,11,3,4,5
        L should now be 4 + 1 = 5
        R = 8
        mid = 5 + (8-5)//2 = 5 + 3//2 = 6
        nums[mid] is 3, so the left is greater but the right is also greater,
        so we have to search left
        L is now 5 and R is now 6,
        5 + (6-5)//2 = 5
        in this case, we'd do another right half search, making
        L = 6 and R = 6.
        The midpoint would end up being 6, L >= R, so return nums[6]
        """
        def binarySearch(left, right):
            mid = left + (right - left)//2
            # if the left >= right, we've exhausted our search, and should've
            # found the rotation point in the sorted array (which is also the minimum)
            if (left >= right):
                return nums[mid]
            # number at right less than mid,
            # search the right
            if nums[right] < nums[mid]:
                return binarySearch(mid+1,right)
            # otherwise, search the left
            else:
                return binarySearch(left, mid)

        return binarySearch(0, len(nums)-1)
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
class Solution2:
    """ 
    	revisited on 7/6/2023
    	Finding the min of the rotated sorted array using a modified binary search

	    in a regular sorted array, the midpoint's value should never be greater than
	    the right side's value because the values are always increasing from left
	    to right. If so, we know that the min must be on this side
		example:
	    3,4,5,1,2, when 5 is the midpoint, 
	    we need to binary search the values to the right of 5 because
	    5 > 2. There can't be a value smaller than 2 on the left side because that would
	    break the sorted order (if the array were to be unrotated back to its original form)

	    once we narrow down to 5, 1, 2,
	    where left is index 3 (value 5), right is index 4 ( value 2) and 
	    mid = 3 + (4 - 3) // 2 = 3 + 1//2 = 3 + 0 = 3
	    narrow down to:

	    example:
	    2, 2.5, 3, 4, 5 when 3 is the midpoint, we need to search the values to the left
	    of 3 since 3 < 5
	    Similar concept is expl


    """
    def findMinHelper(self, nums:List[int], left: int, right: int) -> int:
        mid = left + (right - left) // 2
        if left >= right:
            return nums[left]

        if nums[mid] > nums[right]:
            left = mid + 1
            return self.findMinHelper(nums, left, right)
        else:
            right = mid
            return self.findMinHelper(nums, left, right)

    def findMin(self, nums: List[int]) -> int:
        # in rotation, the sorted order is maintained
        left = 0
        right = len(nums) - 1
        return self.findMinHelper(nums, left, right)

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
