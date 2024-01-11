"""
https://leetcode.com/problems/happy-number/
https://leetcode.com/problems/happy-number/discuss/56915/My-Python-Solution
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        if the squares of the digits doesn't add up to
        1, 10, 100, 1000, etc it cannot be a happy number (i.e n mod 10 == 0)
        
        Key concept is recognizing that at some point, the square sum of each digit will
        loop back around to a sum that we've already calculated, for example 2:
        2
        2^2 = 4
        4^2 = 16
        1^2 + 6^2 = 37
        3^2 + 7^2 = 58
        5^2 + 8^2 = 89
        8^2 + 9^2 = 145
        1^2 + 4^2 + 5^2 = 42
        4^2 + 2^2 = 20
        2^2 + 0^2 = 2
        
        Note that 2 was reached twice, therefore, this cannot be a happy number
        
        we can cache the results of each sum in a set and see if it ever loops around
        
        """
        mem = set()
        mem.add(n)
        while (True):
            n = str(n)
            s = 0
            for i in range(len(n)):
                s += int(n[i])**2
            if s == 1:
                return True
            elif s in mem:
                return False
            n = s
            mem.add(n)