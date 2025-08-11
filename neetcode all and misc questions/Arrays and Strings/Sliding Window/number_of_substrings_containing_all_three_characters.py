"""
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        can use a dictionary to keep track of character counts, and then use a sliding window
        to track the substrings.

        Whenever we reach an instance where there is at least one of each ("a" "b" "c"), 
        since we know our window contains the other
        necessary characters, the key is we figure out how many possible substrings we could make if we 
        were to extend the window further to the right.

        "abcbbac"
        for example, if we have a window L = 0 R = 2,
         we see the first three characters are valid and contan all three. Therefore,
        we know that if we were to shift the right pointer further (for example, abcb, abcbb, etc),
        these would ALL be valid strings, because we already meet the requirements of having at least one of
        "abc" from our window. Therefore, the possible amount of substrings while extending to the right
        is bounded by the length of the string, so we'd count len(s) - R + 1
        "abc" "bbac"
              ^    ^
              additional 4 possible substrings using the first three characters 
              (i.e abcb, abcbb, abcbba, abcbbac), so 7 - (2 + 1) = 

        and then we shift the left pointer until our window is no longer valid.

        O(N) Time
        O(1) Space
        """
        from collections import defaultdict
        d = defaultdict(int)
        l = 0
        res = 0
        N = len(s)
        for r in range(N):
            d[s[r]] += 1
            while d["a"] >= 1 and d["b"] >= 1 and d["c"] >= 1:
                res += 1
                # also count the additional substrings that could be created by extending the right pointer
                # to the end of the string
                res += (N - (r+1))
                d[s[l]] -= 1
                l += 1
        return res

