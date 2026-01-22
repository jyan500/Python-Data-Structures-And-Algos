"""
https://leetcode.com/problems/surrounded-regions/
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        X O X X
        X O O X
        X X O X
        X O X X

        this example, the 4 cell region cannot be surrounded because the top most region cell 
        is on the edge, and therefore, cannot be 4-directionally surrounded by X cells

        Brute Force solution:
        Find all islands and store the indices of their cells, also map a boolean to check
        if any of the islands' cells is on the edge of the board

        go through all islands that don't have an edge on the board and convert them to X's

        This uses up O(N*M) Time and O(N*M) memory, so it's not as efficient as the solution below
        """

        N = len(board)

        def inBounds(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        
        def isOnEdge(i,j):
            return i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1

        islands = []
        directions = [(0,1), (0,-1), (1,0),(-1,0)]
        self.surrounded = True
        self.globalVisited = set()
        def dfs(i,j, visited):
            if isOnEdge(i,j):
                self.surrounded = False
            if (i,j) in visited:
                return
            visited.add((i,j))
            self.globalVisited.add((i,j))
            for x, y in directions:
                newX = x + i
                newY = y + j
                if inBounds(newX, newY) and board[newX][newY] == "O":
                    dfs(newX, newY, visited)
        k = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in self.globalVisited:
                    visited = set()
                    dfs(i,j, visited)
                    islands.append({"cells": visited, "isSurrounded": self.surrounded})
                    # reset the value
                    self.surrounded = True
                    k += 1
        for value in islands:
            if value["isSurrounded"]:
                # convert the surrounded islands to "X" values
                for x,y in value["cells"]:
                    board[x][y] = "X"

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
            
            
                    
        
        
        