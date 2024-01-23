"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
O(N*K), where K is the length of the needle and N is the length of the haystack
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1