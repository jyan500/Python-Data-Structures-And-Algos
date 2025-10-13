class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Time: O(N)
        Space: O(26)
        aabaa = valid string
        aabca = not valid string

        sliding window, keep shifting the window as long as there are at most
        2 distinct characters in the window. 

        To keep track of distinct characters, should use a hashset to keep track
        of the counts of each character. As long as the amount of keys (which represents the
        distinct amount of characters found so far) is <= 2, we can continue expanding the window.

        eceba
        l = 0
        r = 0
        e, only one distinct character
        ec, two distinct characters
        ece two distinct characters
        eceb, X no longer valid, reduce the window until there are only 2 distinct characters left
        -> eceb to eb, where l = 2 and b = 3
        eba not valid

        longest is 3
        """
        from collections import defaultdict
        counter = defaultdict(int)
        l = 0
        maxLen = 0 
        for r in range(len(s)):
            counter[s[r]] += 1
            while len(counter.keys()) > 2:
                counter[s[l]] -= 1
                if (counter[s[l]] == 0):
                    del counter[s[l]]
                l += 1
            maxLen = max(r - l + 1, maxLen)
        return maxLen
            