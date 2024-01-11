'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

https://leetcode.com/problems/set-matrix-zeroes/
https://www.youtube.com/watch?v=T41rL0L3Pnw&ab_channel=NeetCode
'''

class Solution3:
    """
    9/25/2023
    O(M*N) time
    O(1) space
    See the comments, by iwccsbfb
    https://leetcode.com/problems/set-matrix-zeroes/discuss/26026/O(1)-space-solution-in-Python

    1) Instead of storing the original zeroes, when we find an original zero at (i, j),
    we can pre-emptively mark the cell values within the matrix 
    for the non-zero values in the four directions starting from (i, j)
    2) On a second pass, we can then change those "marked" cell values to zeroes

    """

    def inBounds(m, n, i, j):
        return 0 <= i < m and 0 <= j < n
    
    m = len(matrix)
    n = len(matrix[0])
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                for d in directions:
                    x, y = d
                    newX, newY = x + i, y + j
                    if inBounds(m, n, newX, newY):
                        while inBounds(m, n, newX, newY):
                            if matrix[newX][newY] != 0:
                                matrix[newX][newY] = "mark as zero"
                            newX, newY = x + newX, y + newY
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "mark as zero":
                matrix[i][j] = 0

class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    """
    9/25/2023
    1) initial pass to figure out where the "original" zeroes are so that
    we don't interpret any newly set zeroes as "original" zeroes and perform operations in the four directions for those.
    2) second pass to perform the set zero operations on the "original" zeroes

    Uses additional space to store the original zeroes
    O(M*N) time
    O(m+n) space
    """
    
    def inBounds(m, n, i, j):
        return 0 <= i < m and 0 <= j < n
    
    m = len(matrix)
    n = len(matrix[0])
    
    zeroes = set()
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeroes.add((i,j))
    for i in range(m):
        for j in range(n):
            if (i,j) in zeroes:
                # perform operation
                for d in directions:
                    x, y = d
                    newX, newY = x + i, y + j
                    if inBounds(m, n, newX, newY):
                        while inBounds(m, n, newX, newY):
                            matrix[newX][newY] = 0
                            newX, newY = x + newX, y + newY
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = dict()
        zero_cols = dict()
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        ## O(M + N) space solution, O(N*M) Time Complexity
        ## loop through the matrix and find the rows/cols that have to be set to zero
        for i in range(num_rows):
            for j in range(num_cols):
                if (matrix[i][j] == 0):
                    zero_rows[i] = 'set to zero'
                    zero_cols[j] = 'set to zero'
        ## loop through each row and set the rows to zero if the row is found in the zero_rows dict
        for i in range(num_rows):
            if (zero_rows.get(i) != None):
                for j in range(num_cols):
                    matrix[i][j] = 0
        ## loop through each column and set the column to zero if the col is found in the zero_cols dict
        for j in range(num_cols):
            if (zero_cols.get(j) != None):
                for i in range(num_rows):
                    matrix[i][j] = 0;
                    
        