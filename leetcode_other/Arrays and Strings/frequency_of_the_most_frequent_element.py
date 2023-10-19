class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Time Complexity:
        O(NLogN)
        Space:
        O(1)

        https://www.youtube.com/watch?v=vgBrQ0NM5vE&t=440s&ab_channel=NeetCode
        
        Concepts:
        Sort + Sliding Window
        1) Sort because for our sliding window, we need the elements on the right side to always be greater than the previous elements since the previous elements will be incrementing to equal the greatest element in our window
        2) Sliding Window:
            sort nums
            while (windowSize * nums[r] <= total + k):
                increase total by nums[r]
                expand our window
            # if our window is not valid
            decrement total by the value at the left pointer
            increment left pointer
        
        1 1 1 2 2 4, k = 2
        
        the length of the window represents the frequency of the elements within it. Our k 
        represents the "budget" on how many elements within our window that can be incremented
        to equal our biggest element (nums[r])
        
        for example:
        
        1 1 1 = windowSize of 3, where r = 2
        nums[r] = 1
        3 * 1 <= (1 + 1 + 1) + 2 = 3 <= 5, True
        
        1 1 1 2 however is invalid, meaning we can't set each of the elements in this window to 2 because:
        1 1 1 2, windowSize of 4, where r = 3
        nums[r] = 2
        4 * 2 <= (1 + 1 + 1 + 2) + 2 = 8 <= 7, False
        
        This makes sense because we can only increment two of the "1's" to become 2 before
        we run out of budget
        
        As a result, we need to shrink the size of our window by incrementing the left side.
        We also need to shrink the total by removing the value of the leftmost index
        
        1 1 2, this is now valid
        
        1 1 2 2, also valid (max window size is now 4)
        
        1 1 2 2 4 (not valid, because we can't set every element to 4)
        
        1 2 2 4 (not valid, because we can't set every element to 4)
        
        2 2 4 (not valid, for the same reason)
        
        2 4 (valid, window size of 2)
        
        Our final answer here is 4
        """
        nums.sort()
        total, res = 0, 0
        l, r = 0, 0
        
        while (r < len(nums)):   
            while (r < len(nums) and (r - l + 1) * nums[r] <= total + nums[r] + k):    
                total += nums[r]
                res = max(res, r - l + 1)
                r += 1
            total -= nums[l]
            l += 1
        return res
            