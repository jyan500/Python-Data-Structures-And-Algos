'''
https://leetcode.com/problems/trapping-rain-water/
https://www.youtube.com/watch?v=ZkrXxi5ay80&ab_channel=SaiAnishMalla
'''
class Solution:
    def trap(self, height: List[int]) -> int:
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
        
        
        
                