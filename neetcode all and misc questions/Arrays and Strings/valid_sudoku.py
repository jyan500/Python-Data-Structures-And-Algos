"""
https://leetcode.com/problems/valid-sudoku/
https://www.youtube.com/watch?v=TjFXEUCMqI8&ab_channel=NeetCode

Key concepts:
1) The problem is simpler than it appears.

It only requires you to check whether duplicate number exist within a given row, given col, 
and given 3x3 square within the 9x9 grid. We don't need to worry about whether
we can actually "solve" the sudoku in the given state, just that the filled in numbers are not duplicated
(i.e filling in numbers 1-9 for each col, row, etc)

1 2 3 4 5 6 7 8 *
                2
                3
                4
                5
                6
                7
                8
                9

For example, convention would tell us that this sudoku state cannot be solved, because in
the first row, the empty spot should be a 9, but according to the last column, 
it should be a 1, so there's a
conflict. However, the problem is actually stating we only need to worry about whether 
it's valid BUT NOT necessarily solvable. So this above sudoku is technically valid because none of the 
numbers in each row/column are repeating.

To check for the 3x3 square you can convert the 9x9 indices into their 3x3 counterpart by 
taking the given i,j and converting to int(i/3), int(j/3)

i.e 

  0 1 2 3 4 5 6 7 8
0
1   x     x     x
2

3
4   x     x     x
5

6
7   x     x     x
8

Here each 3x3 square could be represented in (0,0), (1,0), (2,0), etc
for example, if in our 9x9, we had 1,1, we'd convert this to int(1/3), int(1/3),
to get 0,0 which is in our top left 3x3 square.

If we had (4,4) in our 9x9 square, we'd convert to int(4/3), int(4/3) to get (1,1),
which is our middle 3x3 square


Time complexity: O(N*M), where N = 9 and M = 9
Space complexity: O(N*M), where N = 9 and M =9 
"""
class Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1) hash set for finding duplicates per row
        2) hash set for finding duplicates per column
        3) create a "virtual" 3x3 grid by converting the 9x9 indices into
           their 3x3 counterpart doing row index/3, col index/3
        4) create a hashmap using the (row index/3, col index/3) as the key and
           a set as the value to check for duplicates within this 3x3 square
        """
        
        rows = dict()
        cols = dict()
        subGrids = dict()
        
        for i in range(len(board)):
            rows[i] = set()
        for j in range(len(board[0])):
            cols[j] = set()
        for k in range(3):
            for l in range(3):
                subGrids[(k, l)] = set()
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                convertI, convertJ = int(i/3), int(j/3)
                if board[i][j] in subGrids[(convertI, convertJ)]:
                    return False
                if board[i][j] in rows[i]:
                    return False
                if board[j][i] in cols[i]:
                    return False
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    subGrids[(convertI, convertJ)].add(board[i][j])
                if board[j][i] != ".":
                    cols[i].add(board[j][i])
            
        return True
                
  
            