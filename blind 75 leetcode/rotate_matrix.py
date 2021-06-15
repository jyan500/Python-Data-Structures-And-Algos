'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

https://leetcode.com/problems/rotate-image/

Solution explanation: https://www.youtube.com/watch?v=gCciKhaK2v8&ab_channel=FisherCoder

idea: transpose the diagonal items to create an intermediate state, then reverse the start and end of each item in the 
row to get the final result

'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ## transpose to an intermediate state
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        ## swap the start and end of each row to get the final result
        for i in range(n):
            start = 0
            end = n - 1
            while (start < end):
                tmp = matrix[i][start]
                matrix[i][start] = matrix[i][end]
                matrix[i][end] = tmp
                start += 1
                end -= 1