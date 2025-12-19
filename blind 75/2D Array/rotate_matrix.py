'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

https://leetcode.com/problems/rotate-image/

Solution explanation: https://www.youtube.com/watch?v=gCciKhaK2v8&ab_channel=FisherCoder

idea: transpose the diagonal items to create an intermediate state, then reverse the start and end of each item in the 
row to get the final result

Revisted 12/19/2025
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


"""
Revisited on 9/18/2023

1) reverse each row
2) iterate through the matrix diagonally starting from the top right corner
    - for each diagonal, swap the first and last elements of the diagonal
i.e you can also iterate through an inverted "L" shape, starting from the topmost "L",
performing a swap at each iteration

1 2 3
4 5 6
7 8 9

reverse each row

3 2 1
6 5 4
9 8 7 

If you do the L shaped iterations and swapping:

1 gets swapped with itself ( no effect )

the 2 and 4 get swapped 

3 4 1
6 5 2
9 8 7

The 3 and 7 get swapped

7 4 1 
6 5 2
9 8 3

The 6 and 8 get swapped

7 4 1
8 5 2
9 6 3

The 9 gets swapped with itself (no effect)

final answer is 

7 4 1
8 5 2
9 6 3

O(N^2) time
O(N^2) space

"""
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r = len(matrix)
        c = len(matrix[0])
                
        for i in range(r):
            matrix[i].reverse()
        
        # top right
        i = 0
        j = len(matrix[0])-2
        
        """
        w[0][3] (first iteration is done)
        w[0][2] swaps with w[1][3]
        w[0][1] swaps with w[2][3]
        w[0][0] swaps with w[3][3]
        """
        # get the "horizontal" portion of each L
        coords1 = []
        coords2 = []
        for i in range(r):
            for j in range(c-1-i,-1,-1):
                coords1.append((i,j))
       
        # get the "vertical" portion of each L
        offset = 0
        i = 0
        j = c-1 
        while (j >= 0):
            while (i < r):
                coords2.append((i,j))
                i+=1
            i = 0
            offset += 1
            i += offset
            j -= 1
        
        # perform zip, pairing up the coordinates and swapping
        for c1, c2 in zip(coords1, coords2):
            x1,y1 = c1
            x2,y2 = c2
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            
        
                
            
            
        
            
        