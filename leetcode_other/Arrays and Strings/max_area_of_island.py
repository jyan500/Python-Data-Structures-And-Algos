"""
https://leetcode.com/problems/max-area-of-island/
Very similar to number of islands,
except keep track of area of each island.
The base case is when we're at an island of area 1 that has no neighbors, just return that area

Time complexity:
O((N+number of ones) * M) 

Space Complexity:
O(N*M) space
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inBounds(i,j, grid):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def dfs(i, j, grid):
            area = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in directions:
                x, y = d
                newX, newY = i + x, y + j
                if inBounds(newX, newY, grid) and grid[newX][newY] == 1 and (newX, newY) not in self.visited:
                    self.visited.add((newX, newY))
                    area += dfs(newX, newY, grid)
                    
            return area
        
        m = len(grid)
        n = len(grid[0])
        maxArea = float("-inf")
        self.visited = set()
        self.globalVisited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in self.globalVisited:
                    # perform DFS
                    self.visited.add((i,j))
                    maxArea = max(dfs(i, j, grid), maxArea)
                    self.globalVisited.update(self.visited)
                    self.visited = set()
        return maxArea if maxArea != float("-inf") else 0
        