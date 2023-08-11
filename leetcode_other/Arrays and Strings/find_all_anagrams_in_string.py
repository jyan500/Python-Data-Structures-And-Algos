"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Brute Force:
        O(N^2)
        check whether a given letter s[i], is in the anagram p
        using a hashmap,
        if so continue the substring until all letters match
        get the index where the anagram begins, store in result
        shift the left by one and set the right back to left
        33/65 test cases passed, TLE
        
        Optimizations:
        We can change the solution above slightly by:
        we can just remove the ith element from the dict, and leaving the other
        elements intact. 
        This way, we're automatically checking the substring from i to j since we already
        have the characters in the dict
        This is essentially
        a sliding window strategy so that we only need to iterate through
        the string once.

        Example:
        s = cbaebabacd, p = "abc"
        once we've found "cba", we can remove "c", and move our pointer
        to e and check "bae", where i = 1, j = 3
        """
        anagram = dict()
        for i in range(len(p)):
            if p[i] in anagram:
                anagram[p[i]] += 1
            else:
                anagram[p[i]] = 1
        potentialAnagram = dict()
        curLen = 0
        anagramLen = len(p)
        res = []      
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] in potentialAnagram:
                potentialAnagram[s[j]] += 1
            else:
                potentialAnagram[s[j]] = 1
            curLen += 1
            if curLen == anagramLen:
                if potentialAnagram == anagram:
                    res.append(i)
                if potentialAnagram[s[i]] > 1:
                    potentialAnagram[s[i]] -= 1
                else:
                    del potentialAnagram[s[i]]
                curLen -= 1
                i+=1
            j+=1

        return res
                