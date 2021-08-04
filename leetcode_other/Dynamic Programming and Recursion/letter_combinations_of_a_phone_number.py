class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            if (char not in cur.children):
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_word = True
    
class Solution:
    ## Time complexity?
    ## exponential time ~ O(4^9), where 9 is the max amount of digits (assuming you have 777777777 or 999999999)
    ## since as you increase the digit, its another exponent increase
    ## Space Complexity
    ## O(4^9) to store every combination in the Trie
    
    def __init__(self):
        self.trie = Trie()
        self.digit_map = {'2' : 'abc','3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9': 'wxyz'}
        self.combinations = []
        
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        "23"
        abc
        def
        a
        def
        b
        def
        c
        def
        9 possible
        "234"
        a
        def
        ghi
        27 possible
        
        exponential time ~ 4^9, where 9 is the max amount of digits (assuming you have 777777777 or 999999999)
        
        Trie
        store prefixes, and that way, we're not recalculating certain combinations

        use the already calculated combination just add on a new char
        and then store that in the trie
        
        "23"
        dict = {"a" : {"d": {}, "e": {}, "f" : {}}, "b" : {"d": {}, "e" : {}, "f": {}, "c"}
        "234"
        dict = "{"a" : {"d" : {"g", "h", "i"}, "e" : {"g", "h","i"}}}"
        '''
        
        self.search(digits, 0, '')
        cur = self.trie.root
        self.getCombinations(cur, '')
        return self.combinations
        
        
    def getCombinations(self, cur, word):
        if (cur.children):
            for c in cur.children:
                ## print('word + c: ', word+c)
                
                w = self.getCombinations(cur.children[c], word + c)
                if (w != None):
                    ## in the case that we finish this loop, we're not going to return anything
                    ## so we need to make sure that we don't append this to our result
                    self.combinations.append(w)
        else:
            return word
            
    def search(self, digits: str, i : int, word: str):
        if (i >= len(digits)):
            return ''
        if (digits[i] in self.digit_map):
            options = self.digit_map[digits[i]]
            for char in options:
                so_far = word + char
                self.trie.insert(so_far)
                self.search(digits, i+1, word + char) 
        
        '''
        2
        options = 'abc'
        word = ''
        word = 'a'
        self.search(digits, 1, 'a')
        
        trie = {'a' : {}}
        3
        options = 'def'
        word = 'a'
        self.search(digits, 2, 'ad')
        
        trie = {'a' : {'d' : {}}}
        
        base case is reached
        word = 'a'
        self.search(digits, 2, 'ae')
        
        trie = {'a' : {'d' : {}, 'e' : {}}}
        '''
                
        
        
        
        
                    
            