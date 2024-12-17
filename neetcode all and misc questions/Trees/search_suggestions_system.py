"""
12/17/2024
Approach:
1) Use a Trie
2) Write a function that retrieves all the words you can get from a given prefix
    similar to "Implement trie" leetcode problem, you'd implement the isStartsWith function similarly
    where you iterate through each character of the prefix and see if it exists, and then set the next
    TreeNode if so.

    However, after this, you'd then run DFS on the remaining tree starting from the TreeNode where
    the last character of the prefix is, getting all the words that start with this prefix.

3) Then, for each character of the searchWord, you would run the function to retrive all words from the prefix.
    Sorting the results, and getting only the first 3 from the results and storing into a nested list.

Time Complexity:    
adding each product word to the trie is O(N), where N is the length of the string
getting all words from a prefix is also O(N), since there's only 26 characters, we can limit the time complexity to a constant where
it'd normally be exponential.
sorting each list of words is O(NLogN)

Because we have to go through the search word N times, it'd be O(N^2 * MLogM), where M is the length of the search results, and N is the length
of the search word

Space:
O(N), where N is the length of the products

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def getWordsFromPrefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            # if the character in the prefix does not exist, just return [] since there's no words that can be formed
            # from this prefix
            else:
                return []
        self.list = []
        def dfs(curr, word):
            if curr.endOfWord:
                self.list.append(word)
            for letter in curr.children:
                dfs(curr.children[letter], word + letter)
        dfs(cur, prefix)
        return self.list
            
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.addWord(p)
        res = []
        for i in range(len(searchWord)):
            words = trie.getWordsFromPrefix(searchWord[0:i+1])
            # sort by lexicographical order and get only the top 3
            words.sort()
            current = []
            for k in range(len(words)):
                if k < 3:
                    current.append(words[k])
            res.append(current)
        return res