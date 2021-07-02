'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

https://leetcode.com/problems/design-add-and-search-words-data-structure/
https://www.youtube.com/watch?v=O5yxoFS_diY&ab_channel=SaiAnishMalla

The difference between this question and implement trie is that the words for the search can contain ".", which are wildcards
we need to make use of a stack to backtrack, in order to visit all the possibilities of that wildcard
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