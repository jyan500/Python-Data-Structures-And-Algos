class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        fisherman can only move on cells with value >= 1,
        find the max amount of fish the fisherman can catch

        On first glance, it seems that this is similar to number of islands,
        where a DFS would work, traversing only cells with value >= 1
        
        and then storing the current sum of that DFS call and saving it, and then
        taking the max of all sums afterwards

        Time Complexity: O(N * (N + M))
        Space: O(N * M)
        """
        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            currentSum = 0
            for x, y in directions:
                newX = i + x
                newY = j + y
                if inBounds(newX, newY) and (newX, newY) not in visited and grid[newX][newY] >= 1:
                    visited.add((newX, newY))
                    currentSum += (grid[newX][newY] + dfs(newX, newY))
            return currentSum
        
        allSums = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >= 1 and (i,j) not in visited:
                    visited.add((i,j))
                    # get the sum of all surrounding values plus the value at the starting cell
                    # for the total fish caught
                    curSum = grid[i][j] + dfs(i, j)
                    allSums.append(curSum)
        return max(allSums) if len(allSums) > 0 else 0

            
            