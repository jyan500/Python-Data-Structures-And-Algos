'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

https://leetcode.com/problems/word-search-ii/

time limit exceeded solution (but does pass every other case): 
https://www.youtube.com/watch?v=ZoMJbbYTWUo&t=839s&ab_channel=TECHDOSETECHDOSE


'''
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            if (c not in cur.children):
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end_of_word = True
        
    def search(self, word):
        cur = self.root
        for c in word:
            if (c not in cur.children):
                return False
            cur = cur.children[c]
        return cur.is_end_of_word
    
    def startsWith(self, word):
        cur = self.root
        for c in word:
            if (c not in cur.children):
                return False
            cur = cur.children[c]
        return True
   
## the following solution gets time limited exceeded on Leetcode, but it passes every other test case 
## see below for a more optimized and "clever" solution on how to solve the search/unique characters issue without
## resorting to extra memory
class Solution:
    def __init__(self):
        self.result = []
        self.unique_set = set()
        self.trie = Trie()
        self.board = []
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        ## add list of words into the trie
        ## keep track of the words that we have found to return them
        rows = len(self.board)
        cols = len(self.board[0])
        for word in words:
            self.trie.insert(word)
        for i in range(rows):
            for j in range(cols):
                if (self.trie.startsWith(board[i][j])):
                    self.dfs(i, j, rows, cols, '')
        return self.result

    def dfs(self, i, j, rows, cols, store):
        ## check the boundaries to make sure we're not out of bounds
        if (i < 0 or i >= rows or j < 0 or j >= cols):
            return
        ## exit out of visited
        if (self.board[i][j] == '0'):
            return 
        ## if the word we are building is not within our trie, we don't need to continue
        if (not self.trie.startsWith(store)):
            return
        store += self.board[i][j]
        ## if we search for the string we've built in store
        ## and it matches as a word (meaning it has reached the 'end of word' within the trie node, and we haven't already seen this word (since the same letter cell can't be used more than once)...
        if (self.trie.search(store) and not store in self.unique_set):
            ## 
            self.result.append(store)
            self.unique_set.add(store)
        ## save the value of the position before modifying it to visited
        ## so that in the backtracking, we can restore the board position's original value
        temp = self.board[i][j]
        ## mark the board position as visited by setting to '0'
        self.board[i][j] = '0'
        
        ## perform dfs in 4 directions
        self.dfs(i, j+1, rows, cols, store)
        self.dfs(i, j-1, rows, cols, store)
        self.dfs(i+1, j, rows, cols, store)
        self.dfs(i-1, j, rows, cols, store)
        
        self.board[i][j] = temp

## link to the more optimized solution: 
## https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
## 
class OptimizedSolution:
	def __init__(self):
		self.result = []

	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ## add list of words into the trie
        ## keep track of the words that we have found to return them
        rows = len(self.board)
        cols = len(self.board[0])
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        for i in range(rows):
            for j in range(cols):
                if (trie.startsWith(board[i][j])):
                	## 1st improvement, pass in the root of the trie
                    self.dfs(i, j, node, rows, cols, '')
        return self.result 
        
    def dfs(self, i, j, node, rows, cols, store):
    	## if we search for the string we've built in store
        ## and it matches as a word (meaning it has reached the 'end of word' within the trie node, and we haven't already seen this word (since the same letter cell can't be used more than once)...
        if (node.is_end_of_word):
            ## 
            self.result.append(store)
            ## 2nd improvement
            ## once we've found the word, we can mark the "is_end_of_word" to be false, so this will no longer be considered
            ## a word in the trie, so if we come across the word again it won't get added in
            node.is_end_of_word = False
        ## check the boundaries to make sure we're not out of bounds
        if (i < 0 or i >= rows or j < 0 or j >= cols):
            return

        ## if the current character is not found in the trie node's children
        ## we don't need to continue the recursion (this is essentially in place of using startsWith)
        node = node.children.get(self.board[i][j])
        if (not node):
            return
        
        ## save the value of the position before modifying it to visited
        ## so that in the backtracking, we can restore the board position's original value
        temp = self.board[i][j]
        ## mark the board position as visited by setting to '0'
        self.board[i][j] = '0'
        
        ## perform dfs in 4 directions
        self.dfs(i, j+1, rows, cols, node, store + temp)
        self.dfs(i, j-1, rows, cols, node, store + temp)
        self.dfs(i+1, j, rows, cols, node, store + temp)
        self.dfs(i-1, j, rows, cols, node, store + temp)
        
        self.board[i][j] = temp
        
        
        