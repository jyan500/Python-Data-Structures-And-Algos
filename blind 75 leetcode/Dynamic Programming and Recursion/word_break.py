'''
https://leetcode.com/problems/word-break/

Revisited on 8/8/2023
Time complexity of the memoized solution O(N^3), N^2 for the recursion, and N for the split method on the string each time
Space complexity is O(N) for the memoization, where N is the length of the input string

Key Concept:
1) Pick a word in our word dict and then shorten our input string if the first n characters of our input string match the word
2) In our memoization, we store whether the given input string in the recursive call can be split or not
based on the result of self.dfs(),
3) we usually put the call to memoization outside
the loop (where the base case is normally) so we can prevent additional loops

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## include cache to store repeated subproblems
        memo = dict()
        return self.dfs(s, wordDict, memo)
    def dfs(self, s, wordDict, memo):
        ## our base case is for an empty string
        ## if we've sliced the string until it becomes length of zero
        ## then we've split our current subproblem perfectly into words
        if (s == ''):
            return True
        elif (memo.get(s) != None):
            return memo[s]
        for word in wordDict:
            prefix = s[0:len(word)]
            result = False
            if (prefix == word and self.dfs(s[len(word):], wordDict, memo)):
                ## for the current string s in our recursive call
                ## store the result of whether it can be split into words in our wordDict
                memo[s] = True
                return True
                
        ## if after looping through all words and we cannot find a match
        ## for the existing string that is passed in for the call,
        ## return False
        ## also save in our memo dict so that we know that this current string s cannot be split further
        memo[s] = False
        return False