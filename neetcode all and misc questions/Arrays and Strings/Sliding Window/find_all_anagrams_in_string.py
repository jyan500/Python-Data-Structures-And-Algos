"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
class Solution:

            

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
                # when preparing to shift l, since we're removing this from our substring
                # we also need to lower the count
                if potentialAnagram[s[i]] > 1:
                    potentialAnagram[s[i]] -= 1
                else:
                    del potentialAnagram[s[i]]
                # once we modified our potential anagram dict to account for removing the leftmost
                # element, we shift the leftmost by one
                curLen -= 1
                i+=1
            j+=1

        return res
    """
	Shorter Solution (easier to remember), but Slower than the one above,
	because we have to construct slices of length(p) every iteration
	O(N) time but with O(N) space
	1) Store the characters and their amounts in hashmap for string p
	2) Loop through string s, and starting from i = 0, slice the string from i ... i + len(p),
	since we know that for anagrams, the strings need to be the same length
	3) Get the character amounts within the string slice, and see if it's equal to the hashmap of p
		if so it's an anagram, so store the starting index i in res
	4) return res
	"""
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        charMap = Counter(p)
        n = len(p)
        # since this is an anagram, we know that
        # we can look for specifically length(p) substrings
        # since the lengths of both strings have to be the same
        r = 0
        res = []
        while (r < len(s)):
            # get the substring from the current index to current index so it's the same
            # as the length of p and see if it contains the same characters, w/ the same
            # amount of characters as p, if so append the starting index
            amtMap = Counter(s[r:r+n])
            if charMap == amtMap:
                res.append(r)    
            r += 1
        return res
                