"""
https://leetcode.com/problems/permutation-in-string/
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        https://neetcode.io/problems/permutation-string
        s1=abc
        s2=lecadbac
        l is not in s1
        e is not in s1
        c is in s1,
        a is in s1
        d is not in s1
        keep a counter for s1
        when iterating s2, keep track of a sliding window using left and right pointer starting at 0,
        track a separate hashmap for s2 that counts the frequency of chars in the substring so far.
        when the length of the substring (R - L + 1) reaches the length of s1, if the counters for s1 and s2
        are the same, that means this is a permutation. Otherwise, we shift the left character by one
        and decrement the frequency of the left character by one. If the frequency becomes 0, we also
        delete that key from the hashmap for s2

        O(26N) Time (since you need to compare the two dictionaries) and O(N) Space
        """
        from collections import defaultdict
        counter = defaultdict(int)
        for c in s1:
            counter[c] += 1
        l = 0
        r = 0
        counter2 = defaultdict(int)
        while r < len(s2):
            counter2[s2[r]] += 1
            if r - l + 1 == len(s1):
                if counter == counter2:
                    return True
                else:
                    counter2[s2[l]] -= 1
                    if (counter2[s2[l]] == 0):
                        del counter2[s2[l]]
                    l += 1
            r+=1
        return False

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
        
                
                
                
            