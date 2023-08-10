'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

"""
8/10/2023
An alternate solution using recursion:
Concept:
1) Start by establishing the search space, which is a list of lists containing
all the different letters that are mapped to a given digit
i.e 
for "234", search space = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

2) We iterate through the search space using DFS, pass in the first letter,
and then recur into the next list, making the search space smaller by taking everything past 0th index 
(via searchSpace[1:])

3) In our base case, we eventually run out of search space, so we just return the individual letter within the list

4) In our backtracking, this will generate new combinations, and we add the letter that we pass in to each of these combinations
to form new ones, and then those will get passed up into the previous calls to generate all combinations.

Time Complexity: the problem states that there can only be 4 digits, but hypothetically N digits,
N^max number of possibilities for a given digit, so N^M

Space Complexity: O(N^M)

Example:

digit = "234" 
searchSpace = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

Recursive Calls
1) 
letters[0] = ["a", "b", "c"]
letter = ""
combinations = dfs("a", [["d,"e",f"], ["g","h","i"]])

2) 
letters[0] = ["d", "e", "f"]
letter = "a"
combinations = dfs("d", [["g", "h", "i"]])

3)
letters[0] = ["g", "h", "i"]
letter = "d"
combinations = dfs("g", [])

4) base case is reached, because search space is now empty
return [g]

Back to 3)
letters[0] = ["g", "h", "i"]
letter = "d"
newCombinations will append "d" + "g" to form "dg"

in the loop, we now do
combinations = dfs("h", [])

5) base case is reached, because search space is now empty
return ["h"]

Back to 3)
letters[0] = ["g", "h", "i"]
letter = "d"
newCombinations will append "d" + "h" to form "dh"

... repeat this process to form "di"

After the loop in case 3) is finished, we return the following new combinations up to case 2):
["dg", "dh", "di"]

Back to 2)
in our combinations = dfs ..., this will now equal ["dg", "dh", "di"]

with letter "a", in the loop we add "a" to each of the combinations to form
"adg", "adh", "adi", and then append to new combinations
["adg", "adh", "adi"]

In the next iteration within 2), we now do

combinations = dfs("e", ["g", "h", "i"])

6) Note that this is a new recursive call, so newCombinations = [],
but if we repeat the process above, we'll eventually append "eg", "eh", "ei" to newCombinations,
go back upwards to case 2) again

"a" + "eg", "a" + "eh", "a" + "ei", because we're back at call 2), our newCombinations array is still intact
with the combinations we had previously ["adh", "adg", "adi"], so we append our new combinations to form
["adg", "adh", "adi", "aeg", "aeh", aei"],

... we do eventually bubble back to case 1) where our new combinations array should be 
[["adg", "adh", "adi", "aeg", "aeh", aei", "afg", "afh", "afi"],
we pass in 
combinations = dfs("b", [["d", "e", "f"], ["g", "h", "i"]]) and the process repeats 



"""
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if digits == "":
            return []
        searchSpace = []
        for d in digits:
            searchSpace.append(digitMap[d])
        def dfs(letter, letters):
            # if we've run out of search space, just return the letter in a list
            if len(letters) == 0:
                return [letter]
            newCombinations = []
            for j in range(len(letters[0])):
                # for each combination, we gradually decrease the search space
                combinations = dfs(letters[0][j], letters[1:])
                # with the combinations that we get, add the previous letter to each
                # combination to form new combinations,
                # and then use these to continually form combinations through each recursive call
                for c in combinations:
                    newCombinations.append(letter + c)
            return newCombinations
                
        return dfs("", searchSpace)


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
                
        
        
        
        
                    
            