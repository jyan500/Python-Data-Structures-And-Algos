'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

https://leetcode.com/problems/number-of-islands/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        all_ones = []
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = []
        for i in range(rows):
            visited.append([])
            for j in range(cols):
                visited[i].append('U')
        ## keep o(n^2) space to keep track of unvisited coordinates, where "U" stands for unvisited
        frontier = []
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == "1" and visited[i][j] != "V"):
                    visited[i][j] = 'V'
                    frontier.append((i,j))
                    num_islands += 1
                    while (len(frontier) > 0):
                        coords = frontier.pop()
                        x = coords[0]
                        y = coords[1]
                        for k in directions:
                            next_x = x + k[0]
                            next_y = y + k[1]
                            if (next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols and visited[next_x][next_y] != 'V'):
                                next_grid = grid[next_x][next_y]
                                if (next_grid == "1"):
                                    frontier.append((next_x, next_y))
                                    visited[next_x][next_y] = 'V'
                    
        return num_islands
                                    
                            
                        