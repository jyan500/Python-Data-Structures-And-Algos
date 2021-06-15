'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

https://leetcode.com/problems/set-matrix-zeroes/
https://www.youtube.com/watch?v=T41rL0L3Pnw&ab_channel=NeetCode
'''
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
                    
        