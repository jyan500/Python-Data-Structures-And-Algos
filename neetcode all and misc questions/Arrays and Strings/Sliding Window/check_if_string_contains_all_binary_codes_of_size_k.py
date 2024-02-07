class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """ 
        Neetcode:
        https://www.youtube.com/watch?v=qU32rTy_kOM
        https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

        2^1 = "0", "1" = 2 unique configurations
        2^2 = "00", "01", "11", "10" = 4 unique configurations
        2^3 = "000", "001", ... = 8 unique configurations

        Brute Force:
        The brute force method would be to generate all combinations of numbers,
        and then see if they exist in S. This would be O(2^K * N * K),
        where 2^K is the time needed to generate all possible combinations
        N * K is the amount of time needed to find all substrings and do a comparison
        
        Optimal:
        However, the optimal way of solving this is to realize that our string S 
        contains only "0" and "1". So rather than generating all combinations,
        we can just find all unique substrings of length K within our string S,
        and because the string only contains "0" and "1", each unique configuration
        will automatically match with a combination.
        
        Therefore, if we can find 2^K unique substrings within S, that means that 
        that string S contains all binary codes of size K, and we can return True
        
        We can simply store each substring of length K in a set and then count,
        this is a time complexity of O(N*K), since we need to generate the substring of length K
        at each index still
        
        """
        
        amt = 2**k
        unique = set()
        for i in range(len(s)):
            windowLength = i + k
            if windowLength <= len(s):
                unique.add(s[i:i+k])
        return len(unique) == amt