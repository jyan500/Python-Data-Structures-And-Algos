"""
https://leetcode.com/problems/unique-paths/
Time Complexity: O(N*M)
Space Complexity: O(N*M)

Concept:
1) We can use DFS to find the number of ways to get to a path from a given cell,
and use memoization to store the amount of ways per cell, so that if we reach
this cell again, we don't need to recalculate the amount of paths
2) By the time of DFS goes back to (0, 0), it would be the sum of the num paths stored
for the cell directly to the right and down

"""
class Solution2:
    def inBounds(self, i, j, m, n):
        return 0 <= i < m and 0 <= j < n
    def uniquePaths(self, m: int, n: int) -> int:
        # DFS
        # can only go right and down 
        directions = [(0, 1), (1, 0)]
        self.memo = dict()
        def dfs(i, j, m, n):
            if (i,j) in self.memo:
                return self.memo[(i,j)]
            # reached the end
            if i == m - 1 and j == n - 1:
                return 1
            count = 0
            for d in directions:
                x, y = d
                newX, newY = i + x, j + y
                if self.inBounds(newX, newY, m, n) and (newX, newY) not in self.visited:
                    count += dfs(newX, newY, m, n)
            # for a given cell, save the amount of ways to get to the finish,
            # and re-use this in subsequent calls so we don't need to recalculate
            # the amount of paths for a given cell
            self.memo[(i, j)] = count
            return self.memo[(i, j)]
     
        count = dfs(0, 0, m, n)
        return count
        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    	## m = num of rows
    	## n = num of columns
        dp = []

        ## initialize m x n matrix with zeroes
        for i in range(n):
            inner = []
            for j in range(m):
                inner.append(0)
            dp.append(inner)
        ## fill first row with 1's since there is only 1 way to reach each value on the first row
        for i in range(m):
            dp[0][i] = 1
        ## fill the first column value of each resulting row with 1 since there is only 1 way to reach the first value on each row
        for j in range(n):
            dp[j][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                ## add the values of the indices directly to the top and left
                ## to get the number of paths to indices i,j 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        ## the bottom right hand corner will contain the number of paths that lead to the
        ## bottom right hand corner
        return dp[n-1][m-1]


    ## Top Down Memoize Solution
     def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()
        return self.search(0,0,m,n,memo)
    def search(self, i, j, m, n, memo) -> int:
        ## if we've hit the finish point, we've reached a possible path, return 1 in this case
        ## print('i,j: ', (i,j))
        ## print('memo: ', memo)
        
        if ((i,j) in memo):
            return memo[(i,j)]
        if (i == m-1 and j == n-1):
            ## print('reached finish')
            return 1
        
        res_right = 0
        res_down = 0
        if (0 <= i < m and 0 <= j+1 < n):
            res_right = self.search(i, j+1, m, n, memo)
        if (0 <= i+1 < m and 0 <= j < n):
            res_down = self.search(i+1, j, m, n, memo)
        ## go down until we hit the boundaries
        ## mark as not visited

        memo[(i,j)] = res_right + res_down
        return res_right + res_down
