'''
	https://leetcode.com/problems/binary-search/
	Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

	You must write an algorithm with O(log n) runtime complexity.

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        return self.helper(nums, 0, len(nums)-1, target)

    def helper(self, nums, left, right, target):
        ## left + (right-left)//2 is to account for integer overflow (as opposed to (left+right)//2)
        ## if left and right are 16 bit unsigned integers, 2^16=65536, if left = 65530 and right was 65531
        ## if you calculated the midpoint using (left+right)//2 you would get an integer overflow, since 65530 + 65531 cannot be stored in a 16 bit integer
        ## but using left+(right-left)//2 you would not, because 65531-65530=1, 65530+1 = 65531, can be stored
        ## https://cs.stackexchange.com/questions/80415/why-is-binary-search-using-this-weird-thing-to-calculate-middle/97738
        midpoint = left+(right-left)//2
        if (target == nums[midpoint]):
            return midpoint
        ## if the left index ever exceeds the right index, then we haven't found the item we're looking for
        ## return -1
        elif (left >= right):
            return -1
        ## if our target element is less than the midpoint, we need to search the half of the array
        ## from the left index to our midpoint - 1
        elif (target < nums[midpoint]):
            return self.helper(nums, left, midpoint-1, target)
        ## if our target element is greater than the midpoint, we need to search the half of the array
        ## from the midpoint + 1, to our right index
        elif (target > nums[midpoint]):
            return self.helper(nums, midpoint+1, right, target)
