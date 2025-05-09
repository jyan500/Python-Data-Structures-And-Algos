class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Revisited 5/9/2025 with a different solution than my first attempt, which tracks two
        indices.

        recursion + memoization

        Time Complexity: Without memoization, O(2^N)
        With memoization, O(N^3) potentially amortized ~ O(N^2)
            -> because we perform a slice within each recursive call which is O(N)
            -> and then using memoization, there are N^2 unique "currentIndexes, newWordIndex" that we can store

        However the amortized analysis is saying that we're not actually slicing across the whole length of the string
        each time, since current index is always being incremented. So it's not actually a full "O(N)" to perform the slice
        within the recursion each time.

        The detailed amortized analysis is from claude that I've pasted at the bottom of the page:
        
        1) Keep track of two things in the recursion, the current index, and the
        index of the beginning of a new word that we've just segmented. Initially starting at
        (0,0)
        Base Case:
        If currentIndex === len(s):
            we've made it to the end, so we just need to check if the 
            newWordIndex == currentIndex, which means we've segmented the last word.
            Note that because the problem states that we need to segment s into words,
            getting to this point and returning true will mean we've segmented the word succesfully.

            For example, if we found a word earlier in s, but then the middle part does not segment into anything, once we reach this base case, it will return False.


        Recurrence:
        as we recur, we slice s[newWordIndex: currentIndex+1] to see if we've made a new word
            if so, we now have two choices:
                match this word, increment currentIndex, and update the newWordIndex to be the same as currentIndex
                OR
                don't match this word, only increment currentIndex

        
        for example:
        
        pineappleberry, word dict = [pine, pineapple, berry]

        once we hit the "e" in pine, we see that we've matched "pine", we can now update the new word index to "a" and current index to "a" as well. 
        Although you'll notice that if we do this, we can't segment the next word "appleberry", since it doesn't exist in the dict.

        However, if you were to keep the newWordIndex at "p" (index 0), and kept going, you could
        match "pineapple" instead, which is the right answer here, since we can match "berry" right after.
        

        """
        N = len(s)
        memo = {}
        def search(currentIndex, newWordIndex):
            # if we were able to make it to the end,
            # and the last word index == current index, which means
            # we segmented a word right before the end of the string,
            # that means we should've segmented every word successfully
            if (currentIndex, newWordIndex) in memo:
                return memo[(currentIndex, newWordIndex)]
            if currentIndex == N:
                memo[(currentIndex, newWordIndex)] = newWordIndex == currentIndex        
                return memo[(currentIndex, newWordIndex)]
            currentWord = s[newWordIndex: currentIndex+1]
            match = False
            if currentWord in wordDict:
                match = search(currentIndex+1, currentIndex+1)
            withoutMatch = search(currentIndex+1, newWordIndex)
            memo[(currentIndex, newWordIndex)] = match or withoutMatch 
            return memo[(currentIndex, newWordIndex)]
        return search(0, 0)

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

"""
Analysis of my 5/9/2025 solution from claude:
This performs string slicing, which generally has a time complexity of O(k) where k is the length of the substring being extracted. If we were to pessimistically analyze this, we might say that k could be as large as n (the full string length) in the worst case, which would make each state computation O(n) and the overall time complexity O(n³).
However, looking at how your recursion works:

In every recursive call, currentIndex is incremented by 1:

This means that for any state (currentIndex, newWordIndex), the substring s[newWordIndex: currentIndex+1] has a length of at most currentIndex - newWordIndex + 1.

Since you're examining each state exactly once due to memoization, and you're essentially moving forward one character at a time, the total amount of characters processed across all string slicing operations becomes O(n²) rather than O(n³).

To illustrate this more concretely:

    When newWordIndex = 0, you'll slice substrings of lengths 1, 2, 3, ..., n (total: n(n+1)/2 characters)
    When newWordIndex = 1, you'll slice substrings of lengths 1, 2, 3, ..., n-1
    And so on...

This forms an arithmetic series that sums up to O(n²) total characters processed across all slicing operations, making the overall time complexity O(n²) rather than O(n³).
"""


