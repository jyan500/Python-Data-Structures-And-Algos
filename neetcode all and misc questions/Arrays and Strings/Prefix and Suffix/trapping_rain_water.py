'''
https://leetcode.com/problems/trapping-rain-water/
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Revisited 4/23/2025
        prefix and suffix sums
        1) When looking at the bars, the amount of water is bounded by the minimum between the max height on the left
        and max height on the right, subtracted by the height at that cell:

        min(max(left), max(right)) - height(current cell)

        (Note that you can't trap water between the first element and the boundary,
        and the last element and the boundary)

        height = [0,2,0,3,1,0,1,3,2,1]
                
        so between i = 1 and i = 3, the max height is 2 on the left, and 3 on the right,
        and the minimum between these two values is 2, so the amount of water that can be trapped
        is 2

        between i = 3 and i = 4, the min between the max height on left and max height on right is 3
        subtracted from the current cell height (of 1) is 2

        The brute force solution would be continuously calculate these values for each cell
        
        """
        # Brute Force
        # O(N^2)
        # note that we start 1, len(heights)-1, since there's no right most max element on the right bounds,
        # and no left most max element
        """
        areas = [0] * len(height)
        for i in range(1, len(height)-1):
            # find the max of each element on the left
            maxLeft = max(height[:i])
            # find the max of each element on the right
            maxRight = max(height[i:])
            # find the min between these two which is the bounds for how much water
            # can be contained, subtracted by the current cell height. But only if 
            # the cell height is less than the boundaries, otherwise that cell
            # can't contain water
            if height[i] <= min(maxLeft, maxRight):
                areas[i] = min(maxLeft, maxRight) - height[i]
        return sum(areas)
        """

        # optimal solution
        # O(N) Time O(N) Space
        areas = [0] * len(height)
        
        # this time, we pre-calculate the max values on the left as prefix
        # max values on the right as suffix, so we can instantly know what the max height
        # on the left and right is by referencing prefix[i] and suffix[i] respectively
        prefix = [h for h in height]
        suffix = [h for h in height]

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i])
        for i in range(len(height)-2, -1,-1):
            suffix[i] = max(suffix[i+1], height[i])
        for i in range(1, len(height)-1):
            maxLeft = prefix[i]
            maxRight = suffix[i]
            if height[i] <= min(maxLeft, maxRight):
                areas[i] = min(maxLeft, maxRight) - height[i]
        return sum(areas)

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        9/25/2024
        https://neetcode.io/problems/trapping-rain-water
        Brute Force: O(N^2) Time O(1) Space
        in order for water to be trapped, you need to have 3 indices where
        the the middle height is less than both the height on the left and height on the right,
        and the amount of water trapped is bounded by the min(height on left, height on right).
        my approach would be to go column by column, iterate to the left and right to see
        what the max height is on both sides. And then take the min between between these two values.
        this value, which is min(max on left, max right) subtracted from the current height at this column i,
        would be the max amount of water you can store at this column. 

        the bottleneck is that you repeatedly calculate the max height on both the left and right side
        of a given i, which could probably be stored in memory to further optimize the solution. You can see
        this in the solutions below, which can be optimized from O(N^2) to O(3N)
        """
        total = 0
        for i in range(len(height)):
            l = i-1
            r = i+1
            maxHeightLeft = 0
            maxHeightRight = 0
            """
            find the maximum height on the left and maximum height on the right
            when optimized, this can actually be pre-calculated to avoid having to repeat this work
            """
            while l >= 0:
                maxHeightLeft = max(height[l], maxHeightLeft)
                l -= 1
            while r < len(height):
                maxHeightRight = max(height[r], maxHeightRight)
                r += 1
            """
            the container is bounded by the minimum height between the left and right,
            so find the minimum height, and then subtract the current height to give
            the max amount of water that can be stored in this column.
            However, in cases where the min(max height left, max height right) < height[i], this is not a valid
            container, so we don't include this calculation. The container height must be greater than height[i]
            in order to store water.
            """
            containerHeight = min(maxHeightLeft, maxHeightRight)
            if (containerHeight > height[i]):
                total += (containerHeight - height[i])
        return total

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        O(N) Time O(N) Space solution by Neetcode:
        https://www.youtube.com/watch?v=ZI2z5pq0TqA&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=MjM4NTE&feature=emb_title&ab_channel=NeetCode
        Concepts:
        Pre-calculating and storing results using Prefix and Suffix calculations,
        and then using those results in final calculation to avoid repeated work.
        
        1) When looking at each index i in height,
        we can tell how much water can be trapped by examining 
        the min(max height to the left of i, max height to the right of i) - height at i
        
        roughly: min(max(left of i), max(right of i)) - h[i]
        
        For example:
        
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        
        Between i = 1, i = 3,
        we can see there's a height difference of 1. at i =2 specifically,
        we can trap one unit of rain water because:
        
        max height to the left of i = 2, is 1
        max height to the right of i = 2, is 2
        
        min(2, 1) = 1, since i = 2 has a height of 0, 1 - 0 = 1, one unit of rain water
        
        2) We can use the prefix and suffix calculations to calculate all the max heights
        to the left of a given index and store that into an array, and all max heights
        to the right of a given index respectively.
            
            first, set prefix and suffix to be copies of height.
            
            left side, looping starting from the front
            - max(current height at i, previous max height that we stored in prefix, which is prefix[i-1])
            right side, looping starting from the back
            - max(current height at i, previous max height that we stored in suffix, which suffix[i+1])
            
        3) We can then iterate through heights again, and simply index into both of our
        precalculated arrays, calculate the min and subtract off of h[i] to find the
        amount of trapped rain water
        
        4) Note that if the calculation results in a negative number, that means
        we can't trap any rain water at this height i, so we'd just put 0 in that case
        since it doesn't make sense to trap negative units of water.
        
        """
        n = len(height)
        suffix = height.copy()
        prefix = height.copy()
        res = [0 for i in range(n)]
        # we skip the first element since it's out of bounds technically, so the max height
        # is just 0
        # we find the max height between the current element
        # and the previous max height that we stored
        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i-1])
        for i in range(n-2,-1,-1):
            suffix[i] = max(height[i], suffix[i+1])
        for i in range(n):
            amt = min(prefix[i], suffix[i]) - height[i]
            if amt > 0:
                res[i] = amt
        # return the sum to get the total amount of rain water
        return sum(res)
            
class Solution:
    def trap(self, height: List[int]) -> int:

    	# https://www.youtube.com/watch?v=ZkrXxi5ay80&ab_channel=SaiAnishMalla
        ## Concept:
        ## Time complexity: O(3N), three individual for loops
        ## Space complexity: O(N), to hold the leftmost, rightmost maxes and res lists
        ## the idea is that for any given celx, as that will l, we want to calculate the
        ## leftmost max and the rightmost madefine the wall of the container
        ## and then we woul want to calculate the water level as "columns" on each cell based
        ## on the smaller value between the leftmost and rightmost max, as we can only hold
        ## water based on the minimum height
        
        ## for example between indices 3 and 7 in the example
        ## at 5 (which is the lowest point), the water level would be 2 because
        ## the leftmost max is 2, rightmost max is 3, so the min between those two is 2
        ## at 4, the water level would be 1, it'd start out at 2 (from the leftmost/rightmost calculation)
        ## we'd need to subtract the actual elevation at that cell, 2-1 = 1
        
        leftmost_max = [0] * len(height)
        ## calculate the left most max based on the element directly to the left
        ## since there can't be a leftmost max at index 0, we start at 1
        for i in range(1, len(height)):
            leftmost_max[i] = max(leftmost_max[i-1], height[i-1])
        rightmost_max = [0] * len(height)
        ## calculate the rightmost max
        ## we start at len(height)-2, since there would be no rightmost element at len(height)-1
        for i in range(len(height)-2, -1,-1):
            rightmost_max[i] = max(rightmost_max[i+1], height[i+1])
        
        res = [0]*len(height)
        for i in range(len(height)):
            ## the water level will be the minimum between the leftmost max and the rightmost max
            ## at this cell, since the minimum defines the barrier of the container that will hold the water
            ## then we subtract the height at the current cell to get the water level
            water_level = min(leftmost_max[i], rightmost_max[i])
            ## edge case, we need to make sure the water level is above the height defined at the current cell
            ## otherwise we'd end up with a negative water level
            if (water_level > height[i]):
                res[i] = water_level - height[i]
        return sum(res)
        
        
        
                