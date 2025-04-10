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
"""
Revisited on 4/10/2025 with similar solution as above
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = float("-inf")
        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def dfs(i,j):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            area = 1
            for x, y in directions:
                newX = x + i
                newY = y + j
                if inBounds(newX, newY) and (newX, newY) not in visited and grid[newX][newY] == 1:
                    visited.add((newX, newY))
                    area += dfs(newX, newY)
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    maxArea = max(dfs(i,j), maxArea)
        return maxArea if maxArea != float("-inf") else 0


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
        