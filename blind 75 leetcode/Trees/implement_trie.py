'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

https://leetcode.com/problems/implement-trie-prefix-tree/
https://www.youtube.com/watch?v=oobqoCJlHA0&ab_channel=NeetCode
'''
class TrieNode:
	def __init__(self):
		self.children = dict()
		self.is_end_of_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
        	if (c not in cur.children):
        		cur.children[c] = TrieNode()
        	cur = cur.children[c]
        cur.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
        	if (c not in cur.children):
        		return False
        	cur = cur.children[c]
        return cur.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
        	if (c not in cur.children):
        		return False
        	cur = cur.children[c]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)