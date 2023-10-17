"""
https://leetcode.com/problems/surrounded-regions/
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        https://www.youtube.com/watch?v=9z2BunfoZ5Y&ab_channel=NeetCode
        Reverse thinking concept:
        Instead of getting all surrounded regions of O's, try to find out
        which regions are unsurrounded regions of O's, meaning the O's that are
        connected to a border like so:
        
        O X X X
        X O O X
        X O X O
        X X X O
        
        The two regions on the border are not flipped to "X" because they are unsurrounded
        But the L shaped region in the middle are all flipped to "X"
        
        1) Do a nested for loop on the border of the 2D array to find any O's.
        2) Then, use DFS to find out all regions of interconnected O's to this border "O", and change
        these values within the array in place to be a placeholder (i.e "T")
        3) Use a nested for loop to figure out any remaining O's, these are changed to "X" because
        by definition, these are surrounded regions. Note that because we changed the unsurrouded regions to "T", we'll leave these alone for now and won't change them to "X".
        4) Do another nested for loop to change the "T" back into "O"
        
        Time Complexity:
        O(N^2)
        O(1) space
        """
        
        m = len(board)
        n = len(board[0])
        
        def inBounds(i, j, width, height):
            return 0 <= i < width and 0 <= j < height
        def dfs(i, j):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            board[i][j] = "T"
            for d in directions:
                x, y = d
                newX, newY = x + i, y + j
                if inBounds(newX, newY, m, n) and board[newX][newY] == "O":
                    dfs(newX, newY)
        # Check the border for "O" elements and change any interconnected
        # "O" elements to "T" using DFS
        for i in range(m):
            # if the top or bottom border row
            if i == 0 or i == m - 1:
                for j in range(n):
                    if board[i][j] == "O":
                        dfs(i, j)
            # check only the left and right element of each row since we
            # we only want the border elements 
            else:
                if board[i][0] == "O":
                    dfs(i, 0)
                if board[i][n-1] == "O":
                    dfs(i, n-1)
        
        # Use a double for loop to find any remaining O's and change to X's
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # change any remaining "T"s back to "O"s
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
            
            
                    
        
        
        