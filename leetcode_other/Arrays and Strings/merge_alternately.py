"""
Similar concept as merge two sorted arrays, except you strictly alternate 
instead of checking whether the element is less than the other and continually
adding on one side sometimes like in merge sorted arrays

https://leetcode.com/problems/merge-strings-alternately/
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        m = len(word1)
        n = len(word2)
        i = 0
        while (i < m and i < n):
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        # if i is equal to the end of word1, that means word2 was longer,
        # so append the rest of word2
        if i == m:
            res += list(word2[i: ])
        # vice versa for word1
        elif i == n:
            res += list(word1[i: ])
        return "".join(res)