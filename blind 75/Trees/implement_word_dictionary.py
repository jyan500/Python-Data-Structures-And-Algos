"""
Revisited on 10/2/2024
I think this is similar to neetcode's solution, but for the "search" function,
I was able to solve it using recursive DFS, 
by passing in the current TrieNode, the current index of the word, and the total length of the word.

Base Case:
if i >= N, this means we've reached the end of the word.
Set a global variable to true if the current TrieNode is marked as "end of word"
without returning any boolean in the recursion. 

If a wildcard character is found, you would then run DFS on all the valid children nodes based on
the current TrieNode that you're at.
If not a wildcard, just call DFS on the child node at the non-wildcard character

Time Complexity: The depth of the Trie is based on the amount of characters in the longest word in the input,
in this case the length is bounded by 20 characters. Also within each child TrieNode, there can only be up to 26 different possible
characters since each character of the word must be lowercase english characters only. If we had 
word that consisted of 20 wildcard characters, we'd have to do 26 different searches per level, which would be O(26^N), in this
case, since the depth of the tree is bounded by 20, it'd be 26^20

Space: O(N), where the Trie is based on the depth of the longest word in the input

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class WordDictionary:

    def __init__(self):
        self.wordDict = Trie()

    def addWord(self, word: str) -> None:
        self.wordDict.insert(word)

    def search(self, word: str) -> bool:
        """
        the special case is if the word contains a dot.
        If so, we stop and call a DFS function instead.
        The dfs function will pass in the current TrieNode, and go character by character,
        if it reaches a *, it will loop through all children at that TrieNode
        and run DFS on them
        """
        self.dfsFound = False
        def dfs(cur, i, N):
            # if we've reached the length of the word,
            # check to see if the current TrieNode is at the endOfWord
            if i >= N:
                # if we've found the end of a word, mark the self.dfsFound flag to be true
                # and return out
                if cur.endOfWord:
                    self.dfsFound = True
                return
            if word[i] == ".":
                # if it's a wildcard, recur into all valid children at this TrieNode
                for c in cur.children:
                    dfs(cur.children[c], i+1, N)
            else:
                # if it's not an asterisk, check to see if the character is 
                # in the TrieNode's children
                if word[i] in cur.children:
                    dfs(cur.children[word[i]], i+1, N)

        cur = self.wordDict.root
        dfs(cur, 0, len(word))
        return self.dfsFound

'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/
https://www.youtube.com/watch?v=O5yxoFS_diY&ab_channel=SaiAnishMalla

The difference between this question and implement trie is that the words for the search can contain ".", which are wildcards
we need to make use of a stack to backtrack, in order to visit all the possibilities of that wildcard

Revisited on 7/21/2023
The iterative DFS solution below is still the most straight forward, from Sai Anish Malla's channel
Time complexity depends on how many wildcards are present in the word:
if theres no wildcard, then it's an O(N) search, where N is the length of the word,
 since it relies on hashmap for O(1) operations
If theres wildcard, we factor in an additional O(N*26^k), where k is the amount of wildcard characters

Space complexity is O(N), N is the amount of words in the word dictionary
'''
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if (c not in cur.children):
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        
        stack = [(self.root, word)]
        while (stack):
            node, word = stack.pop()
            ## if through our calls in the stack, since we pass word[1:], eventually we'll be left with None 
            if not word:
                ## if we're at the end of the word, return True
                ## else we'll keep going
                if node.is_end_of_word:
                    return True
            ## if the character in the word is a '.', we need to push all the children of the current node onto the stack
            ## to see if the rest of the characters after the '.' are found in our trie
            elif word[0] == '.':
                for child_node in node.children.values():
                    stack.append((child_node, word[1:]))
            ## if the character is found in our current trie node's children...
            elif word[0] in node.children:
                ## push the child node onto the stack
                child_node = node.children[word[0]]
                stack.append((child_node, word[1:]))
        return False
            
                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)