'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''

# revisited solution on 7-6-2023
# https://www.youtube.com/watch?v=UuiTKBwPgAo&ab_channel=NeetCode
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        O(N^2) time where you take the given height
        and find all the areas with the widths after that point
        You take the min height since the container left and right points
        have to be the same height
        """
        # res = 0 
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         h = min(height[i], height[j])
        #         w = j - i
        #         res = max(h * w, res)
        # return res

        """
        O(N) time 
        The bottleneck is the height, we should avoid small heights 
        and find bigger heights to calculate the areas rather than
        remaining on the small heights
        
        set two pointers, one at the beginning of the array and one at the end,
        this way we maximize our width
        
        shift the pointer that has the smaller height between the two, calculate
        the area at this point, and keep track whether the max area has exceeded
        
        Note that if the heights are the same, we can just shift either the left or right,
        it doesn't matter because the pointers will eventually meet either way. For example:

        7|             |      |     |

        6|             |      |     |

		5|             |      |     |

        4|             |      |     |
  
        3| |           |      |     |     | 

        2| |     |     |      |     |     | 

        1|_|_   _|_   _|_    _|_   _|_   _|_
           1     2     3      4     5     6

        the max height here is 14
        with the pointers at 1 and 6
        with the code below, because left is not less than right (they're the same),
        we shift right by 1, pointing at 5, with the height of 7
        had we shifted left by 1 instead, left would be pointing at 2.
       	Eventually, we will find the height of 7, either on the left side or the right,
       	and get 14, either approaching from the left OR the right depending on which way
       	we shifted.

        once the left and right pointers meet, stop the iteration
        """
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            res = max(h * w, res)
            # if the height on the left is less than on the right,
            # we only shift the left to maintain the greater height on the right side
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

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
        