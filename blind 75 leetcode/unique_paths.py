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