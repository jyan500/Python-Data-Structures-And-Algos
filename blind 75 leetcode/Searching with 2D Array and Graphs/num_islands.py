'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

https://leetcode.com/problems/number-of-islands/
'''
class Solution2:
    """
    Revisited on 7/8/2023
    O(N^2 * O(N+M)) time, where M is the amount of nodes starting from our start point during DFS?
    O(N^2) space (we could hold every grid element one time theoretically since we don't add repeats)
    1) perform a DFS at a given element if it's value is 1 and the value hasn't been visited yet
    2) During the DFS, we go left, right, up and down from the given value if the value is "1",
       and continue in that direction until there's no more 1's to visit. At each step, we add each "1" to our visited set
    3) Once the DFS finishes, we should've visited all adjacent 1's, which would be an island. 
    4) If our visited set returns at least one element, that would've indicated we've visited the whole island
       and can increment our count
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # brute force, DFS
        visited = set()
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    newVisited = self.dfs(grid, i, j, set())
                    # if we've manage to visit some new nodes, this must be an island
                    if len(newVisited) > 0:
                        islandCount += 1
                        visited.update(newVisited)
             
        return islandCount
                    
    def inBounds(self, grid: [[str]], i: int, j: int) -> bool:
        return i >= 0 and j >= 0 and i <= len(grid) - 1 and j <= len(grid[i]) - 1
    
    def dfs(self, grid: [[str]], i:int, j:int, visited: Set) -> int:
        visited.add((i,j))
        leftCoord = (i, j+1)
        rightCoord = (i, j-1)
        upCoord = (i-1, j)
        downCoord = (i+1, j)
        rightX, rightY = rightCoord
        leftX, leftY = leftCoord
        upX, upY = upCoord
        downX, downY = downCoord
        if self.inBounds(grid, rightX, rightY) and rightCoord not in visited:
            if grid[rightX][rightY] == "1":
                self.dfs(grid, rightX, rightY, visited)
        if self.inBounds(grid, leftX, leftY) and leftCoord not in visited:
            if grid[leftX][leftY] == "1":
                self.dfs(grid, leftX, leftY, visited)
        if self.inBounds(grid, upX, upY) and upCoord not in visited:
            if grid[upX][upY] == "1":
                self.dfs(grid, upX, upY, visited)
        if self.inBounds(grid, downX, downY) and downCoord not in visited:
            if grid[downX][downY] == "1":
                self.dfs(grid, downX, downY, visited)
        return visited



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
                                    
                            
                        