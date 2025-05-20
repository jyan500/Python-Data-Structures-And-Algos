class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        5/20/2025
        https://leetcode.com/problems/count-vowel-strings-in-ranges/
        https://neetcode.io/solutions/count-vowel-strings-in-ranges
        Brute Force
        iterate through the queries array
            take the slices of the words array based on the ranges in each query
            iterate through each slice to figure out which words start and end with vowel and keep count
            store count
        O(N^2) solution

        Optimize?
        The bottleneck is that we're potentially checking ranges that we've already checked in previous 
        calls. 

        I think the key is that within a given range, we only care about the amount of valid vowel strings
        so we could possibly precalculate these values ahead of time using a prefix array. So we always
        know how many values previously have been valid strings up to this point. Then when
        we're given a range query L, R, the amount of vowels in the range is just
        prefix[R] - prefix[L]

        Note that one important detail is that you need a sentinel value that exists in order
        to define the range between i = 0 ... r, since before index 0, technically there's no
        valid string that exists before this. 

        Therefore, instead of doing prefix[R] - prefix[L], we actually need to do
        prefix[R+1] - prefix[L] to account for the presence of the sentinel value.
        This also fixes edge cases where R and L are the same value, since if we didn't,
        the value would always be 0.

        for example:
        ["aba", "bcb", "ece", "aa", "e"]
        [[0, 2], [1, 4], [1, 1]]
        prefix = [0, 1, 1, 2, 3, 4]
        

        when looking at the queries ranges,
        0, 2 -> prefix[2+1] - prefix[0] = 2
        1, 4 -> prefix[4+1] - prefix[1] = 4 - 1 = 3
        1, 1 -> prefix[1+1] - prefix[1] = 0

        O(N) Time O(N) Space

        """
        def isVowel(word: str) -> bool:
            vowels = set(["a", "e", "i", "o", "u"])
            return word[0] in vowels and word[-1] in vowels
        prefix = [0] * (len(words)+1)
        # we have to track a separate index for prefix since it starts at one index above
        # due to the sentinel value at prefix[0]
        k = 1
        for i in range(len(words)):
            # if the current word is a vowel, we increment the count of vowels up to this point
            if isVowel(words[i]):
                prefix[k] = prefix[k-1] + 1
            # otherwise, the count of vowels up to this point remains the same as before
            else:
                prefix[k] = prefix[k-1]
            k += 1
        res = []
        for l, r in queries:
            res.append(prefix[r+1] - prefix[l])
        return res