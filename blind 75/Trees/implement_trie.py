'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

A Trie data structure consists of a series of trie nodes. A Trie Node contains a dictionary mapping a character to another TrieNode
and a boolean flag determining if that character marks the end of a word.

When we insert a word into a Trie, we iterate through the word to check if the character already exists as a key in our
root level TrieNode, if not, we create this TrieNode and map it to the character in the root level children dictionary.
We then continue to traverse down the Trie, by marking cur = cur.children[c], since cur.children[c] evaluates to another TrieNode

The startsWith and search are similar concepts, for search, we are iterating through the word and checking if at each level of 
our Trie, if the children dict contains the character. If it doesn't, then that means the word doesn't exists in our trie.
However, if we reach the end of our word and all the characters have been found, we still need to check if the last character
has been marked as an "end of a word," otherwise it would not actually be considered a word that we have stored in our Trie

For the startswith method, it will do something similar to search, except if at any point the character is not found in our TrieNode's children dict,
then we'll just return False. If we iterated through the whole word, then the prefix was found, so it must be true.


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

""" 
Revisited on 7/20/2023 
I visualized the trie as a series of nested dictionaries,
where you'd store increasingly large prefixes, and managed to 
get an accepted solution out of it. The above method is still the best
way to do this though.
"""

class Trie2:
    def __init__(self):
        self.words = dict()
        self.trie = dict()

    def insert(self, word: str) -> None:
        if word not in self.words:
            self.words[word] = 1
        if not self.startsWith(word):
            self.trie = self.insertHelper(self.trie.copy(), word, 0, len(word)-1)
    
    def insertHelper(self, trie: dict, word: str, index: int, wordLen: int) -> dict:
        # as we progressively increase the prefix, set the prefix as the key and the value
        # as a nested dictionary containing prefixes starting from that prefix
        # i.e {"a": {"aa": {"aaa": {}}}}
        # on the last prefix, which should be the whole word,
        # return an empty dict with the prefix as the key
        if index == wordLen:
            return {**trie, word[:index+1]: {}}
        elif index < wordLen:
            prefix = word[:index+1]
            if prefix in trie:
                # ** spreads the existing key - value pairs of the trie into the new dict that
                # is being returned
                return {**trie, prefix: self.insertHelper(trie[prefix], word, index + 1, wordLen)}
            else:
                return {**trie, prefix: self.insertHelper({}, word, index + 1, wordLen)}

 

    def search(self, word: str) -> bool:
        return word in self.words
      
    def startsWithHelper(self, trie: dict, word: str, index: int, wordLen: int):
        if index == wordLen:
            prefix = word[:index+1]
            if prefix in trie:
                return True
            return False
        elif index < wordLen:
            prefix = word[:index+1]
            if prefix in trie:
                return self.startsWithHelper(trie[prefix], word, index + 1, wordLen)
            else:
                return False
        
    def startsWith(self, prefix: str) -> bool:
        return self.startsWithHelper(self.trie.copy(), prefix, 0, len(prefix)-1)

