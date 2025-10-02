class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        Brute Force method:
        use nested for loops
        O(N^2)
        """
        # res = 0
        # for i in range(len(nums)):
        #     width = 0
        #     for j in range(i, len(nums)):
        #         if nums[i] <= nums[j]:
        #             width = max(width, j - i)
        #     res = max(width, res)
        # return res
        """
        Neetcode: https://youtu.be/3pTEJ1vzgSI
        How do we optimize the brute force solution?
        Bottlenecks:
        1) whenever we do a nested for loop, we end up repeating a lot of work
        because we start at a given index i, and then loop to the end and perform the j - i calculations
        and then increase the index i by one, and loop to the end again.
        2) Also if we were to find a given window in our calculation, 
        say [6,0,8,2,1,5], we find the window from index 1 to index 5, there wouldn't be any point
        in looping any more because we know that there's not going to be a window between 1 and 5 
        that exceeds the width.

        How to optimize the brute force solution?
        Sliding window + prefix/suffix pre-processing

        In order to determine at a given element, if there's an element in the future that has 
        a value that is greater, we can do suffix pre-processing by starting
        at the end of the array, and asking ourselves what the biggest element we've encountered so far? 
        And then inputting that value into a new array. This is very similar to the problem "trapping rain water"
        for example: [6, 0, 8, 2, 1, 5]
        starting from the back,
        the biggest element we've seen so far is 5
        [_ _ _ _ _ 5]
        the next biggest element we've seen so far is 5
        [_ _ _ _ 5 5]
        we continue until we see that the biggest element becomes 8
        [_ _ 8 5 5 5]
        and this continues until:
        [8 8 8 5 5 5]

        what this tell us is that at a given index i, for example 0
        the value is 6, since 6 < 8, we know that there is a window we can find in the future
        that is valid, so this tells us we can continue our calculations.

        The second aspect to this problem is the sliding window portion. So continuing on,

        6 0 8 2 1 5
        we use two pointers L = 0, R = 0, and we increment R first until the window no longer
        meets our conditions, then increment L

        starting from 0, we reference the pre-processed array which tells us we can continue expanding our window,
        since 6 < 8
        L = 0
        R = 1, max width so far is 0
        At R = 1, we see that we can still continue on, since the max value so far is 8 here
        L = 0
        R = 2 (width of 2)
        we can still continue on because the max value is still 8
        L = 0
        R = 3, now at this value we can see that the value at 0 (6), is NO longer less than
        than the value at the pre processed array (pre processed[3], which is 5)
        therefore, the window is no longer valid since there's no point in expanding this window any further,
        since you won't find a value greater than 6 anymore, so increment L by 1
        L = 1
        R = 3
        in this particular example, you can continue to increment R until the end, 
        which gives the max width by default

        there might be cases though where you need to increment L multiple times until it becomes valid
        [6, 9, 8, 2, 1, 5]
        the pre processed version would look like this
        [9  9  8  5  5  5]
        you can see that initially, the window would be 0 to 2, but increment L to 1 is not valid either,
        because the R value < L value, so we need to increment to L = 2

        """
        maxSoFar = nums.copy()
        for i in range(len(maxSoFar)-2, -1, -1):
            maxSoFar[i] = max(maxSoFar[i], maxSoFar[i+1])
        l = 0
        maxWidth = 0
        for r in range(len(nums)):
            # if the window is no longer valid
            while (nums[l] > maxSoFar[r]):
                l += 1
            if nums[l] <= maxSoFar[r]:
                maxWidth = max(r - l, maxWidth)
        return maxWidth
        