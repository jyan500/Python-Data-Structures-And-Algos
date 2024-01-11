class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Elements must be removed in-place, hence the extra steps here

        O(N) Time, O(N) space
        
        Reverse Thinking:
        1) Find the amount of values == val within nums
        2) Using this amount, starting towards the back of the array
        from len(nums)-amt to len(nums), set the value to be equal to val (since we ignore these)
            -at the same time, store any values != val in a separate list
            -reverse this list
        3) From 0 ... len(nums)-amt, we then 
        set any values equal to val to be the value within our separate list that we stored
        
        0 1 2 2 3 0 4 2
        
        amount of values == 2 is 3
        
        set the last 3 values to be 2, and
        we also store the values != 2 here
    
        0 1 2 2 3 2 2 2,
        and [0, 4]
        
        reverse the list from [0, 4] to [4, 0]
        
        0 1 2 2 3 . . .
        
        Replace the two 2 values with 4 and 0
        
        0 1 4 0 3
        
        The final answer is just the total length minus the amount of 
        values == val that we found earlier.
        
        
        """
        amt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                amt += 1
        nonValNums = []
        for i in range(len(nums)-amt, len(nums)):
            if nums[i] != val:
                nonValNums.append(nums[i])
            nums[i] = val
        nonValNums.reverse()
        j = 0
        for i in range(0, len(nums)-amt):
            if nums[i] == val:
                nums[i] = nonValNums[j]
                j += 1
        return len(nums)-amt