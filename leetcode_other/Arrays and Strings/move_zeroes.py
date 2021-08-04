'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Another more efficient approach
        simply save the non zero elements in a list
        loop through the original array and set i value to be the non zero element,
        so that the way the non zero elements keep their relative order
        fill the rest of the array with zeroes
        O(N) time but O(N) space
        '''
        
        non_zero = []
        ## save the non zero elements in a list, maintaining their relative order
        for i in range(len(nums)):
            if (nums[i] != 0):
                non_zero.append(nums[i])
        j = len(non_zero)
        ## fill the initial spots of the array with non zero elements
        for i in range(len(non_zero)):
            nums[i] = non_zero[i]
        ## fill the remainder of the array (starting from the last index of non-zero) with zeroes
        for k in range(j, len(nums)):
            nums[k] = 0

    ## Initial swapping approach, O(N)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        
        swapping zeroes
        
        [0,1,0,3,12]
        swap 1 with 0
        [1,0,0,3,12]
        swap 0 with 0
        [1,0,0,3,12]
        swap 3 with 0
        [1,0,3,0,12]
        swap 12 with 0
        [1,0,3,12,0]
        
        [1,3,0,12,0]
        swap 12 with 0
        [1,3,12,0,0]
        swap 0 with 0
        [1,3,12,0,0]
        
        what if we swapped non-zero elements instead of zeroes?
        
        [0,0,0,0,1]
        [1,0,0,0,0]
        
        [0,1,0,3,12]
        [1,0,0,3,12]
        [1,0,3,0,12]
        [1,3,0,0,12]
        [1,3,0,12,0]
        [1,3,12,0,0]
        
        Initial approach is we swap the non zero elements to the front, so that by definition
        after the non zero elements are swapped to go the front, then the zero elements would go to the back
        Time complexity: O(N), but because for an array with all non-zero elements except the first element (i.e 
        [1,2,3,4,5,0], you'd end up iterating backwards until i == placement to perform the swapping, so there's quite
        a few total operations still
        [2,1,3,4,5,0]
        [1,2,3,4,5,0]
        [1,3,2,4,5,0]
        [1,2,3,4,5,0]
        [1,2,4,3,5,0]
        [1,2,3,4,5,0]
        Space complexity is O(1))

        '''
        
        non_zero_elements = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                non_zero_elements+=1
        ## swap a non-zero element to the front
        i = 0
        placement = 0
        while (non_zero_elements > 0):
            if (nums[i] != 0):
                while (i != placement):
                    nums[i],nums[i-1] = nums[i-1], nums[i]
                    i-=1
                placement += 1
                non_zero_elements -= 1
            i+=1
        
        '''
        non_zero_elements = 3
        i = 0
        placement = 0
        i = 1
        placement = 0
        nums[1],nums[0] = nums[0],nums[1]
        [1,0,0,3,12]
        i = 0 placement = 0
        placement = 1
        non_zero_elements = 2
        i = 1
        nums[1] = 0, so increment i by 1
        i = 2
        nums[2] = 0, so increment i by 1
        i = 3
        nums[3] = 3
        placement = 1
        nums[3],nums[2] = nums[2],nums[3]
        [1,0,3,0,12]
        i -= 1 (i is now 2)
        nums[2], nums[1] = nums[1], nums[2]
        [1,3,0,0,12]
        ''' 

        
        
        