"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        Revisited 4/18/2025
        1) Remember to use the concept N = N // 2 to split into quadrants, and then
        pass in to start from the top left corner of each of these quadrants

        loop i ... N
           loop j ... N
              use grid[i+row][j+col] to compare elements directly in that quadrant

        top left: row, col
        top right: row, col + N
        bottom left: row + N ,col
        bottom right: row+N, col+N
        

        Neetcode: https://www.youtube.com/watch?v=UQ-1sBMV0v4&ab_channel=NeetCodeIO
        Time Complexity: O(N^2LogN), there are LogN levels in the tree, and at each level,
        you're performing N^2 work (nested loop) to figure out whether all the values 
        in the quadrant are the same.
        Note it's logN because ..., 
        if N = 4, there would be at most 2 levels, assuming that every value was different
        if N = 8, there would be at most 3 levels, assuming that every value was different

        Approach:
        1) Perform DFS, where you initially begin at the top left corner (0, 0). 
            In the quadrant, in order to properly determine the indices of each quadrant, 
            you will need to recognize that:
            a) at each quadrant, the length that you iterate get's halved every time 
                N = N // 2
            b) the rows and cols attribute will change depending on which quadrant you're in, see the diagram below.

        For example in a 4 x 4 matrix
            you initially start from 0, 0 (top left), comparing every value in the entire matrix to the top left
            If you see a different value ...
            
            If you need to halve the N value first (So from 4 to 2)
            Recur down the top left
            Recur down the top right
            Recur down the bottom left
            Recur down the bottom right

            r,c  r, c + N//2,  
            0 1 | 0 1
            0 1 | 0 1
         r+N//2,c r + N//2, c+N//2  
           ____ ____
            0 1 | 0 1
            0 1 | 0 1

            You can see based on the math above, that initially, the reference point is the top left corner, but then
            you add the N//2 "modifier" to get it to the proper quadrant.

            For example, if you wanted to iterate on the bottom right quadrant here of the 4 x 4:
            for i in range(2):
                for j in range(2):
                    ...
                    i goes from 0 to 1
                    j goes from 0 to 1
                    grid[2 + 0][2 + 0] = grid[2][2] = 0
                    grid[2 + 0][2 + 1] = grid[2][3] = 1
                    grid[2 + 1][2 + 0] = grid[3][2] = 0
                    grid[2 + 1][2 + 1] = grid[3][3] = 1
    
        """ 
        def construct(N, row, col): 
            isSame = True
            # to find out whether all values are the same in the quadrant,
            # pick one corner (in this case the topleft of that quadrant)
            # and compare every value to it.
            topLeft = grid[row][col]
            for i in range(N):
                for j in range(N):
                    if topLeft != grid[i+row][j+col]:
                        isSame = False
                        break
            if isSame:
                return Node(val=topLeft, isLeaf=True)
            
            N = N//2
            topLeft = construct(N, row, col)
            topRight = construct(N, row, col + N)
            bottomLeft = construct(N, row + N, col)
            bottomRight = construct(N, row + N, col + N)
        
            return Node(val=0, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)

        return construct(len(grid), 0, 0)
        

                

