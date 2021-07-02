'''
https://leetcode.com/problems/word-break/

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