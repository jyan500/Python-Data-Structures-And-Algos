"""
https://leetcode.com/problems/permutation-in-string/
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Carlos Carrillo's youtube comment
        https://www.youtube.com/watch?v=UbyhOgBN834&ab_channel=NeetCode

        O(26N) Time, where the 26 is due to the dictionary comparison
        O(N) space
        
        1) keep a window that's the same length as the shorter string s1
        2) Iterate through s2, if character count of window in s2 is the same 
        as s1:
            return True
            else:
            increment the window by 1 on both ends

        You can condense the code needed to count the hashable objects via collections.Counter

        for c in string:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        ...
        can just be

        collections.Counter(string)
        
        """
        from collections import Counter
        # window of length s1
        l = 0
        r = len(s1)
        s1Map = Counter(s1)
        while (r <= len(s2)):
            window = s2[l:r]
            s2Map = Counter(window)
            if s2Map == s1Map:
                return True
            l += 1
            r += 1
        return False
        
                
                
                
            