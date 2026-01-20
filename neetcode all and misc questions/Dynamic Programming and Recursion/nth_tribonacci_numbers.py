class Solution:
    def tribonacci(self, n: int) -> int:
        """
        1/20/2026
        very similar to fibonacci numbers, except for fibonacci,
        we take the sum of previous two numbers (n-1) and (n-2) to
        build fibonacci number n
        but for tribonacci, we take the sum of the previous 3 numbers
        (n-1) + (n-2) + (n-3)

        the base cases:
        this means there aren't enough numbers to make a triplet,
        so we would treat both of these cases like normal fibonacci,
        0 1 1, so the 1st and 2nd fibonacci values are 1,
        and the 0th fibonacci is 0.

        Time: O(N)
        Space: O(N)
        
        """
        memo = {}
        def tribonacci(n):
            if n == 0:
                return 0
            if n == 2 or n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
            return memo[n]
        return tribonacci(n)
       