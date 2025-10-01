class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        10/1/2025
        https://leetcode.com/problems/count-servers-that-communicate/
        This is similar algorithm to the othello game that I wrote back in college.
        global visited = set()
        for each row
            for each col
                if the cell's value is 1 and hasn't been visited:
                    perform the search mentioned below and keep a visited set only for the search.
                    Add the starting point to this set
                        check continually down all 4 directions to see if another value with 1 exists,
                        if so add to the visited set within this search.
                    update the global visited set if the visited set found more than one element (not including
                    the original cell)
                    
        return len of global visited

        Time: O(N*M)
        Space: O(N*M), because the visited set could contain every cell in the grid if they were all 1
        """
        self.visited = set()
        res = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def search(i, j, visited):
            for x, y in directions:
                newX = x + i
                newY = y + j
                while inBounds(newX, newY):
                    if (grid[newX][newY] == 1):
                        visited.add((newX, newY))
                    newX += x
                    newY += y
       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited and grid[i][j] == 1:
                    visited = set()
                    visited.add((i,j))
                    search(i, j, visited)
                    if len(visited) > 1:
                        self.visited.update(visited)
        return len(self.visited)

