'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

https://leetcode.com/problems/unique-paths-ii/

https://www.youtube.com/watch?v=ZqMX18ygGWw&list=PLJjp1UcO5B7d7Fm3e45xO74UBf0QiN-wn&index=21&ab_channel=TimothyHChang
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = []
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        for i in range(rows):
            inner = []
            for j in range(cols):
                inner.append(0)
            dp.append(inner)
        for i in range(cols):
            if (obstacleGrid[0][i] != 1):
                dp[0][i] = 1
            else:
                ## if we encounter an obstacle, do not continue to traverse right
                ## as we won't be able to reach anything to the right of the obstacle
                break
        for j in range(rows):
            if (obstacleGrid[j][0] != 1):
                ## if we encounter an obstacle, do not continue to traverse down
                ## as we won't be able to reach below the obstacle
                dp[j][0] = 1
            else:
                break
        for i in range(1, rows):
            for j in range(1, cols):
                ## if we find an obstacle, set the amount of paths to 0 for this indices
                if (obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                else:
                    ## when adding together the top and left, if either the top/left value is 
                    ## zero, then the path won't be added
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[rows-1][cols-1]