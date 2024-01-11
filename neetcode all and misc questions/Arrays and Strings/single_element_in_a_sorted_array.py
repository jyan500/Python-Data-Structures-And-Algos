class Solution:
    """
    https://www.youtube.com/watch?v=HGtqdzyUJ3k&t=623s&ab_channel=NeetCodeIO
    Key Concepts:
    1) When looking for the single element in the midst of the pairs of elements, we check
    whether the left neighbor and the right neighbor are different elements. Because this is a sorted array, if this was a single element, both neighbors would have different elements. If we were looking at a pair of elements, either the left or right neighbor would have the same value.
    
    1 1 2 3 3 4 4 8 8
        ^
    
    Notice that 1 and 3 are the neighbors of 2, which are different values to 2,
    but 3 for example, would have 3 and 2 as neighbors
    
    2) To apply binary search, we need to figure out which half to search if we haven't found
    our single element. The key is that if the side that contains the single element will always
    have an ODD amount of values on that side. So after splitting down our mid point, we continually
    find the side that has the odd amount of values and go down that side.
    
    We just need to find the amount of values on one side (in this case the left side for this solution), and then if that side has an odd amount, we search this side, otherwise search the other side.
    
    Example:
    mid = (0 + 7)//2 = 3, nums[3] = 3
    1 1 2 3 3 4 4 8
          ^
    Here because the left side has an odd amount of values (1 1 2)
    we search the left half, continue binary searching down this path
    
    Another Example:
    1 1 2 2 3 3 4 4 5
            ^
    mid = (0 + 8)//2 = 4
    here, because the left size is even, we search the right half, 
    
    left = 5, right = 8
    mid = (5 + 8)//2 = 6
    
    1 1 2 2 3 3 4 4 5
                ^
                mid
    here, the left size is even (6), search the right half
    
    mid = (6 + 8)// 2 = 7
    1 1 2 2 3 3 4 4 5
                  ^
    here, the left side is still 6, because the element directly to the left
    of mid is the same as the value of mid, so we don't count this element. Continue searching the right half
    
    mid = (8+8)//2 = 8
    arrives mid = 8, here the left side is different, but there's no right side, hence the
    mid + 1 == len(nums) condition. Therefore, the answer is 5
    
    
    
    
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        
        def binarySearch(left, right, nums):
            mid = left + (right-left)//2
            # when we look at the left and right neighbors of mid, we also need to check
            # whether the left and right neighbors are in-bounds in the array
            if (mid - 1 < 0 or nums[mid-1] != nums[mid]) and (mid + 1 == len(nums) or nums[mid+1] != nums[mid]):
                return nums[mid]
            # the size of the left side, if the element to the left is the same
            # as the mid's value, the left size will not include this duplicate value
            # in the search space
            leftSize = mid-1 if nums[mid-1] == nums[mid] else mid
            # if the left side is even numbered, we search the right half
            if leftSize % 2 == 0:
                return binarySearch(mid+1,right,nums)
            # else we search the left half
            else:
                return binarySearch(left,mid, nums)
        
        return binarySearch(l, r, nums)
            
            