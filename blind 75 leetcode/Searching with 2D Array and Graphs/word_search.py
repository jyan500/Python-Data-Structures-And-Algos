'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

https://leetcode.com/problems/word-search/

Test Cases
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"

[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCB"

[["a"]]
"a"

[["a","a"]]
"aaa"

[["a","b"],["c","d"]]
"abcd"

[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
"ABCESEEEFS"
'''

"""
Revisited on 8/10/2023

Concept:
1) DFS within grid
2) when we go down a given path starting from a cell, we want to keep track of the cells we've already visited so that
we don't go back into a cell we've already been to. However, after the path exploration is done for that cell, we want to 
pop off all the cells we visited so that we can take into account other paths that may visit these same cells. Hence the 
visited.remove((i,j)) in the case we're returning False from dfs because no letters could be found.
3) We start by initially finding a starting point where the first letter of our word is found, and then gradually increase
the index as we find more characters, until our index == len(word), which means there are no more characters to be found,
so we've found the whole string and can return True 

Time Complexity: O(M^N * (4^K)), where M is the number of rows and N is the number of columns, and then 4^K states
that we can go in four directions, and then for each direction,
we can go another 4 and so on, up to the length of the word K

Space Complexity: O(N*M), for the additional visited set which could hold every cell in the grid at some point

"""
class Solution2:
    def inBounds(self, i, j, board):
        return 0 <= i < len(board) and 0 <= j < len(board[0])
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited = set()
        def dfs(i, j, board, curIndex, word):
            self.visited.add((i, j))
            if curIndex == len(word):
                return True
            for d in directions:
                x, y = d
                newX, newY = i+x, j+y

                if self.inBounds(newX, newY, board) and word[curIndex] == board[newX][newY] and (newX, newY) not in self.visited:
                    if dfs(newX, newY, board, curIndex + 1, word):
                        return True
            self.visited.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):      
                if board[i][j] == word[0]:
                    if dfs(i, j, board, 1, word):
                        return True
        return False

'''
not a working solution, but somewhere I went wrong when figuring out when to reset the visited variable
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        to_check = []
        rows = len(board)
        cols = len(board[0])
        if (cols == 1 and rows == 1):
            return word == board[0][0]
        ## find the first letter of the word in the board
        first_letter = word[0]
        for i in range(rows):
            for j in range(cols):
                ## if first letter is found
                if (board[i][j] == first_letter):
                    ## append coordinates to the frontier
                    to_check.append((i,j))
        ## run a depth first search on the frontier
        return self.helper(word, board, to_check, rows, cols)
    def helper(self,word, board, to_check, rows, cols):
        frontier = []
        visited = []
        directions = {'right' : (0, 1), 'bottom' : (1, 0), 'top' : (-1, 0), 'left' : (0, -1)}
        ## if the word is less than two characters, check if the the word
        ## was already found in the to_check array since this contains the first letter
        if (len(word) < 2):
            return len(to_check) > 0
        word_index = 1
        print(to_check)
        for i in range(len(to_check)):
            frontier.append(to_check[i])
            visited.append(to_check[i])
            print(frontier)
            while (len(frontier) > 0):
                cur = frontier.pop()
                ## prune visited
                if (len(frontier) > 0):
                    visited_index = visited.index(cur)
                    print('visited index: ', visited_index)
                    visited = visited[0:visited_index]
                found = False
                for key in directions:
                    
                    ## calculate the indices after moving in that direction
                    spot_x = cur[0] + directions[key][0]
                    spot_y = cur[1] + directions[key][1]
                    print('visiting ' + key)
                    print('frontier: ', frontier)
                    print('visited: ', visited)
                    if (spot_x >= 0 and spot_x < rows and spot_y >= 0 and spot_y < cols):
                        ## if character is found
                        if (board[spot_x][spot_y] == word[word_index] and (spot_x, spot_y) not in visited):
                            print('found: ', board[spot_x][spot_y])
                            found = True
                            frontier.append((spot_x, spot_y))
                            visited.append((spot_x, spot_y))
                    
                            print('updated frontier: ', frontier)
                            print('updated visited: ', visited)
                            ## if the word index reaches the len of the word, we've found our word so no need to continue the loop
                            print('word index: ', word_index)
                            if (word_index == len(word)-1):
                                return True
                ## increment to show that within our word param, we've found the character at this index
                if (found):
                    word_index += 1
        return False
                       
''' 

''' 
working iterative solution: https://leetcode.com/problems/word-search/discuss/131327/Iterative-Python-Solution

## as I had thought, you have to find someway to remove the visited nodes in case you go down the wrong path and need
to reset to the last item in the frontier, this solution implements that via a backtracking node

class Solution(object):
    def neighbors(self, board, r, c):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        nbs = []
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if (0 <= nr < len(board)) and (0 <= nc < len(board[nr])):
                nbs.append((nr, nc))
        return nbs
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        q = list()
				
        for r in range(len(board)): # find starting points
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    q.append((r, c))
                    
        for (r, c) in q:
            visited = set()
            stack = list()
            stack.append((r, c, 0, False)) # regular forward moving node
            while stack:
                cr, cc, i, backtrack = stack.pop()
                if backtrack:
                    visited.remove((cr, cc))
                    continue
                    
                visited.add((cr, cc))
                stack.append((cr, cc, i, True)) # add backtracking node
                if i == (len(word) - 1):
                    return True
            
                for nr, nc in self.neighbors(board, cr, cc):
                    if (nr, nc) in visited:
                        continue
                    if board[nr][nc] == word[i + 1]:
                        stack.append((nr, nc, i + 1, False)) # forward-moving node
            
        return False
'''


''' recursive DFS solution 
https://www.youtube.com/watch?v=vYYNp0Jrdv0&ab_channel=KevinNaughtonJr.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        to_check = []
        rows = len(board)
        cols = len(board[0])
        if (cols == 1 and rows == 1):
            return word == board[0][0]
        ## find the first letter of the word in the board
        first_letter = word[0]
        for i in range(rows):
            for j in range(cols):
                ## if first letter is found, run DFS on this position
                if (board[i][j] == first_letter and self.dfs(word, board, rows, cols, i, j, 0)):
                    return True
        return False

    def dfs(self,word, board, rows, cols, i, j, count):
        ## base case #1, if the count of characters found equals the length of the word, we're done searching
        if (count == len(word)):
            return True
        ## base case #2, if we go out of bounds, or the current character is not equal to the
        ## character that we are currently on within the word param, return false
        if (i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[count]):
            return False
        ## mark the current i,j as "visited" by modifying the board element in place
        ## but save the current element and reset it in case we go down the wrong path
        temp = board[i][j]
        board[i][j] = ""
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ## perform DFS in all 4 directions
        found = self.dfs(word, board, rows, cols, i+1, j, count + 1) or self.dfs(word, board, rows, cols, i, j+1, count + 1) or self.dfs(word, board, rows, cols, i-1, j, count + 1) or self.dfs(word, board, rows, cols, i, j-1, count + 1)
        ## reset the current board coordinate in case we go down the wrong path, this will backtrack
        ## until we find the right path to go on, and then we'll start turning the board coordinate into an empty string again
        board[i][j] = temp
        return found

        ## alternative last bit of code to refactor into directions and loop through
        ## have to save the results of each DFS in a list and find if any of the results is True
        '''
        res = []
        for k in directions:
            res.append(self.dfs(word, board, rows, cols, i+k[0], j+k[1], count+1))
        found = False
        for r in res:
            if (r):
                found = True
        board[i][j] = temp
        return found
        '''

