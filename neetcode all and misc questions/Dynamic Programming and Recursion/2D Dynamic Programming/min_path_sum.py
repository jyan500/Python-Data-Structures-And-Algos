class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        2-D backtracking with memoization
        we want to save the minimum sum for any path that can be taken at a given (i,j)
        with memoization
        time: O(N*M)
        space: O(N*M)
        """
        def in_bounds(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        memo = {}
        directions = [[0,1], [1,0]]
        def dfs(i, j):
            # return the min sum at the bottom right position, which is just itself
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            min_sum = float("inf")
            for x, y in directions:
                new_x = x + i
                new_y = y + j
                if in_bounds(new_x, new_y):
                    min_sum = min(min_sum, grid[i][j] + dfs(new_x, new_y))
            memo[(i,j)] = min_sum
            return min_sum
        return dfs(0,0)
                
        
                    