"""
https://leetcode.com/problems/island-perimeter/
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        1) If the cell is 1, count the neighbors. For each neighboring cell, if the neighboring cell is 0, or if 
            it's out of bounds, increment the perimeter
            
            0 1 0 0 
            1 1 1 0
            0 1 0 0
            1 1 0 0

            [0, 1] has a water cell to the left and right, and is out of bounds on the top, so increment by 3
            [1, 0] has a water cell above, below, and is out of bounds on the left side, so increment by 3
            [1, 1] is connected by islands cells all around it, so don't increment by anything
            [1, 2] is connected by water cells above, below and to the right, so increment by 3
            [2, 1] is connected by water cells to the left and to the right, increment by 2
            [3, 0] is connected by water cells above, and out bounds to the left and below, increment by 3
            [3, 1] is connected by water cells to the right, and out of bounds on the bottom, increment by 2
            3 + 3 + 3 + 2 + 3 + 2 = 16
                    
            O(N^2) Time 
        """
        def inBounds(i, j, grid):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for d in directions:
                        x, y = d
                        newX, newY = i + x, j + y
                        if inBounds(newX, newY, grid) and grid[newX][newY] == 0 or (not inBounds(newX, newY, grid)):
                            perimeter += 1
        return perimeter
                    