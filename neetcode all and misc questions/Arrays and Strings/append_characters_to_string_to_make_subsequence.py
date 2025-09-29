class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
        
        first check if t is already a subsequence of s
        for example
        t = coding
        s = coaching

        you can check for the subsequence by building a string t by checking if the 
        characters exist in the same relative order within s, do this by keeping track
        of a pointer that points to the index in string t.

        pointer to t = 0
        result = []
        for char in s:
            if the current char is in t and the current pointer to t matches the char:
                append the character to result
                increment the pointer to t
        
        If the result is the same as t, that means t is already a subsequence of s, so we return 0
        otherwise, in order to make t a subsequence, we can check to see what characters have already
        been added to our result so far. Then, we'd just take the remaining characters of t and add
        it to s. Since we only care about the number, this would translate to the length of string T - length
        of the result.

        O(N) Time
        O(N) Space
        """

        """
        Cleaner version by neetcode:
        The difference here is that if the characters are not the same, it will continue
        iterating down S, while the pointer at T remains the same. This saves memory
        
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j
        """

        tCounter = set(t)
        c = []
        k = 0
        for i in range(len(s)):
            if k == len(t):
                break
            if s[i] in tCounter and t[k] == s[i]:
                c.append(s[i])
                k += 1
        if list(t) == c:
            return 0
        return len(t) - len(c)

        