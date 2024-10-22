class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        """
        https://leetcode.com/problems/maximum-odd-binary-number/
        the max odd number that can be created means there must be a "one"
        at the last position (1 * 2^0)
        
        you would then move all other "one" values as close to the front as possible,
        to create the biggest number possible,
        and the very last "one" would get swapped to the back
        """
        # initialize with zeroes
        res = ["0"] * len(s)
        # track a pointer within res and then whenever we see a "one" in string s,
        # set res[k] = 1
        k = 0
        for i in range(len(s)):
            if s[i] == "1" and k < len(s):
                res[k] = "1"
                k += 1
        # k will be the first occurrence of "zero" in res, 
        # so k - 1 is the last occurrence of "one".
        # swap the last "one" with the back so that the back value becomes "one", creating the odd number
        res[k-1], res[-1] = res[-1], res[k-1]
        return "".join(res)