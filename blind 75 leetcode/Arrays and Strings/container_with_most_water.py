'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''
def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height)-1
    area = 0
    prev_height_left = 0
    prev_height_right = 0
    while (left < right):
    	## note that in order to make a greater area, the height must increase
    	## therefore, if the height does not increase, we don't need to re-calculate the area
        if (height[left] < prev_height_left):
            left += 1
            continue
        elif (height[right] < prev_height_right):
            right -= 1
            continue
        heights = min(height[left], height[right])
        widths = right - left
        area = max(heights * widths, area)
        ## if the height of the left side of the container is less than the right, continue to iterate
        ## on the left side by incrementing
        if (height[left] < height[right]):
            prev_height_left = height[left]
            left += 1
        ## if the height of the right side of the container is less than the left, continue to iterate
        ## on the right side by decrementing 
        else:
            prev_height_right = height[right]
            right -= 1
    return area
        