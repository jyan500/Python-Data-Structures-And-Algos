"""
Approach: 
Prefix Sums
https://leetcode.com/problems/range-sum-query-2d-immutable/description/
In a similar manner to the range sum query immutable problem that involves a one-dimensional array,
we can store the cumulative sums for each row.
To figure out the range within that row, you would just take the right side (which is the cumulative sum up to this point),
subtracted from the cumulative sum of the (left - 1) element

For example in range sum query:
[1, 2, 3, 4, 5]

The prefix sum would be
[1,3,6,10,15]

If I wanted the range between indices 1 and 3,

I could see the cumulative sum up to index 3 is 10
and everything between 1 and 3 should add up to 9,
therefore we would have to subtract the cumulative sum up to index 0
(which is 1), so 10 - 1 = 9

For this problem, you would apply this same process to each row of the 2-D array, getting a "prefix matrix""

When getting the range based on the row1, row2 and col1, col2,

You would then perform a loop based on the difference between row1 and row2,
and then apply the same process of getting the cumulative sum range between the columns

Time Complexity: O(N^2) for creating the prefix matrix, but O(N) for the sumRegion function.

Optimal Solution:
Instead of storing the prefix for only each row, you can get the cumulative sum for an entire rectangular section, and then 
subtracking the outer parts of the rectangle that are not part of the range we're looking for.

Check out: https://www.youtube.com/watch?v=KE8MQuwE2yA&ab_channel=NeetCode
"""

# O(M) solution
# revisited using the O(M) solution on 2/19/2025 with an explanation:
"""
O(M) subregion instead of O(1)
    Using a prefix matrix, we can get the cumulative sums inside a 
    specific region based on the upper left hand corner
    and the bottom right hand corner of the region

    3 0 1 4 2
    5 6 3 2 1
    1 2 0 1 5
    4 1 0 1 7
    1 0 3 0 5

    The first thing is to calculate the prefix matrix for the whole matrix,
    so each row contains the cumulative sum 

    3 3  4  8  10
    5 11 14 16 17
    1 3  3  4  9
    4 5  5  6  13
    1 1  4  4  9

    For example, if the subregion parameter listed is
    2 1 4 3

    this means the upper left hand corner is 2, 1
    and the bottom right hand corner is 4, 3,
    which is denoted by this subregion

    2 0 1 
    1 0 1
    0 3 0

    in the prefix matrix, this translates over to:

    3 3 4
    5 5 6
    1 4 4

    therefore, we can identify that the sums of each row
    of this subregion should be the rightmost element of each row,
    4 
    6
    4

    However, because this is a CUMULATIVE sum of the WHOLE row,
    we have to account for any previous numbers that were included in 
    the sum that are NOT part of the subregion, so they need to be
    subtracted out.

    Thankfully, it's easy to tell what this is because the sum
    we need to remove is just one column to the left
    |
    v
    1  3 3 4
    4  5 5 6
    1  1 4 4

    so to get the true cumulative sum of each row in the subregion,
    it would be 
    4 - 1 = 3
    6 - 4 = 2
    4 - 1 = 3

    You can see that matches up with the original:

    2 0 1, cumulative sum = 3
    1 0 1, cumulative sum = 2
    0 3 0, cumulative sum = 3
    
    Note that there is an edge case where if there is NO column to the left
    of the subregion (i.e col1 - 1 < 0), you don't need to subtract
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixMatrix = [row for row in matrix]
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefixMatrix[i][j] = self.prefixMatrix[i][j-1] + self.prefixMatrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            if col1 - 1 >= 0:
                res += self.prefixMatrix[i][col2] - self.prefixMatrix[i][col1 - 1]
            else:
                res += self.prefixMatrix[i][col2]
        
        return res

# Optimized Solution
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        # in order to handle the edge case where you find a rectangle
        # that's at the border, you have to pad an extra row and column 
        # that has values of 0 
        self.prefixMatrix = [[0] * (self.cols+1) for i in range(self.rows+1)]
        for i in range(self.rows):
            prefix = 0
            for j in range(self.cols):
                prefix += self.matrix[i][j]
                # you want to add the cumulative sum from the col above
                # to the current col, since the goal is to store the sum of the rectangle
                # in 
                above = self.prefixMatrix[i][j+1]
                # because our prefix matrix has an extra row and col padded to it,
                # have to add back + 1 onto the index
                self.prefixMatrix[i+1][j+1] = prefix + above



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # have to add back + 1 since the matrix has an extra row and col padded to it
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        bottomRight = self.prefixMatrix[r2][c2]
        # the "above" is the indices that stores the cumulative sum of the row directly above the rectangle
        above = self.prefixMatrix[r1-1][c2]
        # the "left" is the indices that stores the cumulative sum of everything to the left of the rectangle
        left = self.prefixMatrix[r2][c1-1]
        # we need to add the top left value back in because subtracting
        # the above and left portions would cause an overlap where top left value is getting
        # subtracted twice, so you have to add it back in 
        topLeft = self.prefixMatrix[r1-1][c1-1]
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)