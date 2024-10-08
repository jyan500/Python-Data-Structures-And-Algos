"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Key Concept:
1) Calculate the amount of vowels for the first window of length K
2) We then iterate by incrementing the boundaries of the window (l and r) by one
3) Whenever we move the boundary, we need to check whether the leftmost element was a vowel since
this value will no longer be part of our window after we move it, if so decrement the amount of vowels

This saves some time because we don't need to figure out what characters are actually in the window,
just if the newest character is a vowel or not

Time complexity:
O(N)

Space:
O(1)

"""
class Solution:
    # revisited on 10/7/2024, same solution as below but simpler code
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a","e","i","o","u"])
        l = 0
        maxCount = 0
        count = 0
        for r in range(len(s)):
            # if the right most character is a vowel, increment count
            if s[r] in vowels:
                count += 1
                maxCount = max(count, maxCount)
            # if we've reached the threshold of k, remove the leftmost character. If it's a vowel,
            # also decrement the count of vowels, and then increment left pointer to shift window
            if r - l + 1 == k:
                if s[l] in vowels:
                    count -= 1
                l += 1
        return maxCount

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        from collections import Counter
        vowels = set(["a", "e", "i", "o", "u"])
        l = 0
        r = k - 1
        numVowels = 0
        res = 0
        
        # calculate the amount of vowels in the first window of length k
        for char in s[l:r+1]:
            if char in vowels:
                numVowels += 1
        res = max(numVowels, res)
        
        # because we are shifting the window one to the left, figure out
        # if the leftmost was a vowel, if so decrement
        if s[l] in vowels:  
            numVowels -= 1
        l += 1
        r += 1
        # after the first window, we only need to check if the rightmost element
        # is a vowel, if so add it to numVowels
        # if the leftmost value was a vowel, decrement it
        while r < len(s):      
            if s[r] in vowels:
                numVowels += 1
            res = max(numVowels, res)
            if s[l] in vowels:
                numVowels -= 1           
            l += 1
            r += 1
        return res