'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
https://leetcode.com/problems/powx-n/
Explanation:
https://www.youtube.com/watch?v=sImaLW6qrJw&ab_channel=SaiAnishMalla

Time complexity : O(LogN)
space complexity : O(LogN) recursive stack

'''

""" 
9/20/2023
Same solution as below, just rewritten slightly
"""
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n % 2 == 0:
            temp = self.myPow(x, n/2)
            return temp * temp
        if n > 0:
            return x * self.myPow(x, n - 1)
        elif n < 0:
            return (1 / x) * self.myPow(x, n + 1)

class Solution:
    import math
    def myPow(self, x: float, n: int) -> float:
        ## for negative numbers, we want to convert x to be a decimal, and then
        ## convert the power (n) to a positive number
        if (n < 0):
            x = 1/x
            n *= -1
        return self.pow(x,n)
    def pow(self, x, n):
        if n == 0:
            return 1
        ## key trick here:
        ## since in our recursion, we're decreasing the value of n (which is the power)
        ## if n is an even number
        ## then we can evaluate this exponent to be the same as 
        ## x^n = x^(n/2) * x^(n/2)
        # i.e x^4 = x^2 * x^2
        ## so we can make a big improvement since we'll be cutting the amount of recursive calls in half
        ## since every other number will be even, we don't need to do recursion here
        if (n % 2 == 0):
            temp = self.pow(x, n/2)
            return temp * temp
        else:
            return x * self.pow(x, n-1)
        
    '''
    sample test case
    2^11
    #1 call
    n is odd (11)
    return 2 * self.pow(2, 11-1 = 10)
    
    #2 call
    n is even (10)
    temp = self.pow(2, 10/2) = self.pow(2, 5)
    
    #3 call
    n is odd
    return 2 * self.pow(2, 5-1 = 4)
    
    #4 call
    n is even
    temp = self.pow(2, 4/2) = self.pow(2, 2)
    
    #5 call
    n is even
    temp = self.pow(2, 2/2) = self.pow(2,1)
    
    #6 call
    n is odd
    return 2 * self.pow(2, 1-1 = 0)
    
    #7 call
    base case is reached! since any number to the power of 0 is 1, return 1
    returns 1
    
    backtracks to #6 call
    return 2 * 1
    
    backtracks to #5 call
    temp = 2
    return 2 * 2 = 4
    
    backtracks to #4 call
    temp = 4
    return 4 * 4 = 16
    
    backtracks to #3 call
    return 2 * 16 = 32
    
    backtracks to #2 call
    temp = 32
    return 32 * 32 = 1024
    
    backtracks to #1 call
    return 2 * 1024 = 2048
    
    answer, 2^11 = 2048
    
    only 6 recursive calls were actually made, without the trick
    of splitting even number powers into two separate results and multiplying
    we would get an O(N) time, where N is the power
    but because we're splitting the total calls in half (similar to binary), we get O(LogN) time
    

    '''