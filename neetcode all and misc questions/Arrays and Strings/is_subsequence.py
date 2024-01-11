"""
https://leetcode.com/problems/is-subsequence/
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        reverse thinking
        think about whether there are letters in T that match in S rather than the other way around
        
        1) seen refers to the index of the letter in S that we're currently looking for in T
        2) If the letter t[i] is in our string s, check if it also corresponds to the value at the index we're currently at within S, if so, increment seen. Since we're going through in T in order, that guarantees that we're encountering them in the order at which they appear in S.
        3) After iterating through, len(s) == seen indicates that we've seen all the letters 
        
        For example:
        s = "abc" t = "ahbgdc"
        
        seen = 0
        "a" at seen = 0, seen is now 1
        "b" at seen = 1, seen is now 2
        "c" at seen = 2, seen is now 3
        
        len(s) == 3, returns true
        
        s = "ab" t = "baab":
        "b", but at seen = 0, the value within S is "a", we don't increment seen in this case
        "a", at seen = 0, the value is also "a", seen = 1
        "a", at seen = 1, the value is "b", so don't increment seen in this case
        "b", at seen = 1, the value is "b", so increment seen in this case to 2
        
        len(s) == 2, returns true
        """
        seen = 0
        counter = set(s)
        for i in range(len(t)):
            if t[i] in counter and s[seen] == t[i]:
                seen += 1
        return seen == len(s)