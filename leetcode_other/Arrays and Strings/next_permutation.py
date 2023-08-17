'''
https://leetcode.com/problems/next-permutation/
https://www.youtube.com/watch?v=4wlBBRo4tYY&ab_channel=SaiAnishMalla
'''

"""
Revisited on 8/17/2023
Re-wrote a solution based on my understanding of Sai Anish Malla's video

1) starting from the back of the array, find the first descending number
2) using the descending number, figure out the first number which is greater than
our descending number (this is our swap point)
3) swap these two numbers
4) starting from the index of our first descending number + 1, reverse the order of the list
to get the next permutation as the result.

There's an edge case where the numbers are in descending order,
which breaks steps 1), and 2)
(i.e [3, 2, 1]), we just need to reverse the list in place in that case

Time Complexity: O(3N), 3 separate one pass operations
Space Complexity: O(1)
"""
class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        descending = 0
        swap = 0
        # find the first descending number
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                descending = i
                break
        
        # find the swapping point, which is the first number that is greater than our
        # descending number
        for i in range(len(nums)-1,-1,-1):
            if nums[descending] < nums[i]:
                swap = i
                break

        # if the list is full descending order, just reverse the whole list
        if descending == 0 and swap == 0:
            l = 0
            r = len(nums)-1
            while (l <= r):
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        else:  
            # swap these numbers
            nums[descending],nums[swap]=nums[swap],nums[descending]
            # reverse the list in place one place after descending
            l = descending + 1
            r = len(nums)-1
            while (l <= r):
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        [1,2,3]
        [1,3,2]
        we've used up all possible combinations on idx 1 and idx 2
        [2,1,3]
        
        _1_    _2_    3__
        (23)   (3)    ()
        _1_    _3_    _2_
        (23)(3)(2)
        _2_    _1_    _3_
        (23)(3)(2)
        _2_    _3_    _1_
        (23)(3)()
        
        check what the max element is
        if our first element is the max, then we know that this will be around
        the ~last set of permutations that can be calculated
        
        if our first element is the min, then we know that ~first set of calculations
        
        1 2 3 4
        1 2 4 3
        first descending element swaps with next greater element
        reverse everything beyond the first descending element
        1 2 4 3 (note that reversing would actually sort it in this case)
        
        concept:
        Time complexity: O(N)
        space complexity: O(1)
        find the first decreasing element (start iterating from the end of the array) (call it d1)
        find the number just larger than the element (call it d2)
        swap these two elements (d1, d2 = d2, d1)
        reverse the elements right after the index where d1 was 
        
        '''
        
        length = len(nums)
        if (length <= 2):
            return nums.reverse()
        pointer = length - 2
        ## find the first descending element, by
        ## continuing the iteration
        ## until the nums[pointer] is no longer increasing
        while (pointer >= 0 and nums[pointer] >= nums[pointer+1]):
            pointer -= 1
        
        ## if the first decending element was not found
        ## such as in an example like this (i.e [4,3,2,1])
        ## we'd need to return the original permutation
        ## which would just be the reverse
        if (pointer < 0):
            return nums.reverse()
        first_descending_element = nums[pointer]
        ## find the next increasing element
        ## by iterating from the back again up
        ## to our first descending element
        for i in range(length-1, pointer, -1):
            if (first_descending_element < nums[i]):
                nums[pointer],nums[i]=nums[i], nums[pointer]
                break
        ## reverse everything beyond the index where our first descending element was
        nums[pointer+1: ] = reversed(nums[pointer+1:]) 
            
            
        
        
        
        
        
        
        