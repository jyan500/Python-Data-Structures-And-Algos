"""
Key Concept:
This is a binary search, except if the element is not found in the case
of left pointer >= right pointer, we know that this is the element "closest" in value
to our target.
1) We check to see if the target <= nums[left pointer], 
if so, we return the left index, otherwise, we return the left index + 1

Time Complexity: O(LogN)
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        def search(left, right, nums, target):
            mid = left + (right - left)//2
            if left >= right:
                return left if target <= nums[left] else left + 1
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return search(mid+1, right, nums, target)
            else:
                return search(left, mid, nums, target)
        return search(left, right, nums, target)
            