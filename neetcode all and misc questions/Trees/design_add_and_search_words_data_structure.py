"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Time: O(26) to insert, 
With wildcards: O(O(26) x 26) to search (since there are only up to 26 possibilities for letters in the case every letter
is a wildcard)
"""
class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True        

    def search(self, word: str) -> bool:
        self.wordFound = False
        current = self.root
        # perform DFS, stepping through each character in the word and progressively going deeper
        # into each level of the trie.
        # if we find an asterisk, loop through all the children at that level within the trie
        def dfs(cur, i, word):
            if i >= len(word):
                if cur.isEndOfWord:
                    self.wordFound = True
                return
            if word[i] == ".":
                # if its a wildcard, recur into all children at this level
                for c in cur.children:
                    dfs(cur.children[c], i+1, word)
            else:
                if word[i] in cur.children:
                    dfs(cur.children[word[i]], i + 1, word)
        dfs(current, 0, word)
        return self.wordFound


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)