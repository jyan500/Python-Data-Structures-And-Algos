class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-closed-islands/

        Time complexity: O(N*M)
        Space: O(N*M)

        1) find all islands that are interconnected by 0's
        2) Filter through the islands by checking if any of the islands exist on a boundary, 
        if so, this means it CANNOT be a closed island by definition, since a closed island must 
        be entirely surrounded by 1's. Note that implicitly by getting all interconnected 0's, we 
        can assume that every other element is a 1. So that means the only way for it to NOT be a closed island
        is if it sits on a boundary

        how to determine if a cell in the island is on the boundary?
        1) lowest X value = top boundary
        2) lowest Y value = left boundary
        3) highest X value = bottom boundary
        4) highest Y value = right boundary

        if the top boundary == 0 or top boundary == len(grid)-1 OR
        left boundary == 0 or left boundary == len(grid[0]) - 1 OR
        bottom boundary == 0 or bottom boundary == len(grid)-1 OR
        right boundary == 0 or right boundary == len(grid[0]) - 1,
        that means the boundary exists at the edge of the grid, so it cannot
        be enclosed by a "1" since there are no cells surrounding one of its directions.

        for example:
        grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

        0 0 1 0 0
        0 1 0 1 0
        0 1 1 1 0

        we can see that the island defined by grid[0][0], grid[0][1], grid[1][0], grid[2][0]
        is not an island because it sits on the boundary


        """
        # a grid with only 2 rows by default cannot have any enclosed islands, since 
        # any 0 would always be on a boundary
        if len(grid) <= 2:
            return 0

        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def dfs(i, j, visited):
            directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                newX = x + i
                newY = y + j
                if (newX, newY) not in visited and inBounds(newX, newY) and grid[newX][newY] == 0:
                    visited.add((newX, newY))
                    dfs(newX, newY, visited)
                    
        globalVisited = set()
        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in globalVisited and grid[i][j] == 0:
                    visited = set()
                    visited.add((i,j))
                    dfs(i,j,visited)
                    # take the union of all visited within this island with the global set
                    globalVisited.update(visited)
                    islands.append(visited)
        res = 0
        for island in islands:
            xValues = [cell[0] for cell in island]
            yValues = [cell[1] for cell in island]
            topBoundary = min(xValues)
            leftBoundary = min(yValues)
            bottomBoundary = max(xValues)
            rightBoundary = max(yValues)
            # note that if any of the boundaries have a value that is equal to 0
            # or the len(grid)-1, this is a corner and therefore is not an enclosed island
            # by definition, since it must be surrounded by 1's and cannot sit in the boundary.
            if topBoundary == 0 or topBoundary == len(grid)-1 or leftBoundary == 0 or leftBoundary == len(grid[0])-1 \
            or bottomBoundary == 0 or bottomBoundary == len(grid)-1 or rightBoundary == 0 or rightBoundary == len(grid[0]) - 1:
                continue
            res += 1
        return res
        
