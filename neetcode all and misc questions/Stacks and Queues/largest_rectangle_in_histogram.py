class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Neetcode:
        https://neetcode.io/problems/largest-rectangle-in-histogram
        O(N) Time and O(N) Space Solution
        Stack that only holds strictly increasing elements. If we see an element
        that is smaller than the top of the stack, we have to pop from the stack.
        Whenever we pop from the stack, because the current height at (heights[i]) is less than the previous heights
        that we popped, we want to set the index (which will be used to calculate width) to be the LAST index
        that we popped off to represent the full width
        """
        maxArea = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while (len(stack) > 0 and heights[i] < stack[-1][1]):
                index, height = stack.pop()
                width = i - index
                area = (width * height)
                maxArea = max(maxArea, area)
                start = index
            stack.append((start, heights[i]))
        # if there are still elements on the stack, this indicates that their heights
        # could've been extended all the to the end of the histogram,
        # so for each element on the stack, you'd calculate the width by taking
        # the len(height) - index and then the height on the stack to calculate the remaining areas
        for i in range(len(stack)):
            index,height = stack[i]
            width = len(heights) - index
            area = width * height
            maxArea = max(area, maxArea)
        return maxArea
        """
        Brute Force
        similar idea to trapping rain water
        at a given bar at i, can we find another bar to the left
        and to the right where height[index] >= i, if so we continue to iterate in that direction
        and then subtract the r - l to find the width
        width * height[i] = area of that rectangle
        O(N^2) time O(1) space
        """
        """
        maxArea = 0
        for i in range(len(heights)):
            l = i
            r = i
            while (l > 0):
                if heights[l-1] >= heights[i]:
                    l -= 1
                else: 
                    break
            while (r < len(heights)-1):
                if heights[r+1] >= heights[i]:
                    r += 1
                else:
                    break
            area = (r - l + 1) * heights[i]
            maxArea = max(area, maxArea)
        return maxArea
        """