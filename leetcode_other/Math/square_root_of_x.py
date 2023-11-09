'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

https://leetcode.com/problems/sqrtx/

Concept:
Time complexity: O(LogN)
Space : O(1)

Apply binary search
at current midpoint, multiply midpoint * midpoint
if midpoint * midpoint is less than x, than we need to search right half 
if midpoint * midpoint is greater than x, we need to search left half
if midpoint * midpoint == x, then we just return the midpoint

however, if our square root is a decimal number, once the while loop breaks
we just return the value of right, because when the while loop breaks,
left would be now greater than right. Since we want to truncate the decimal, we return the smaller
number
(i.e x = 8, sqrt(x) = 2.8, so in our binary search, at the end left = 3, right = 2, return 2)


'''

# revisited on 11/9/2023 with about the same solution
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        binary search from 0 to x, x is the right bound here because we know that 
        any number greater than x would produce a square value that's greater than x ** 2
        
        if the mid**2 value is less than the target, we need to search the right half
        else, search the left half
        
        at the end, if we left exceeded right, that means we're one number off the target which 
        is greater than the target,
        so we need to subtract one to get the "floor"
        
        if x is less than or equal to 1,
        than 0 or 1 is the only answer
        """
        left = 0
        right = x
        
        if (x <= 1):
            return x
        while (left < right):
            mid = left + (right-left)//2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid
        return left-1

class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        x = 36
        Apply binary search
        at current midpoint, multiply midpoint * midpoint
        if midpoint * midpoint is less than x, than we need to search right half 
        if midpoint * midpoint is greater than x, we need to search left half
        if ()
        
        left = 0
        right = 35
        mid = (0 + 35) // 2 = 17 = 17^2 > 36
        right is now (17//2)=8
               
        left = 0
        right = 8
        mid = (0 + 8) // 2 = 4, 4^2 < 36
 
        '''
        left = 0
        right = x
        ## if x == 1 or x == 0, (and we know its positive ints only)
        ## no need to perform any binary search, just return itself
        if (x <= 1):
            return x
        while (left <= right):
            mid = (left+right)//2
            res = mid * mid
            if (res == x):
                return mid
            elif (res < x):
                left = mid + 1
            elif (res > x):
                right = mid - 1
                
        ## when binary search ends, left value will be equal or exceed right value
        ## in that case, we would've narrowed down our number between left (bigger num) and right (smaller num)
        ## since we truncate the decimal, return the smallest number
        return right
        
        '''
        in that the square root of the number is decimal (i.e x = 8)
        left = 0 
        right = 8
        mid = 4, 4^2 > 8, decrease right by 1
        
        left = 0
        right = 7
        mid = 7//2=3, 3^2 = 9 > 8, decrease right by 1
        
        left = 0
        right = 6
        mid = 6//2=3, 3^2 = 9 > 8, decrease right by 1
        
        left = 0
        right = 5
        mid = 5//2=2, 2^2 = 4 < 8, increase left by 1
        
        left = 1
        right = 5
        mid = 6//2=3, 3^2 = 9 > 8, decrease right by 1
        
        left = 1
        right = 4
        mid = 5//2=2, 2^2 = 4 < 8, increase left by 1
        
        left = 2
        right = 4
        mid = 6//2 = 3, 3^2 = 9 > 8, decrease right by 1
        
        left = 2
        right = 3
        mid = 2+3//2 = 2, 2^2 = 4 < 8, increase left by 1
        
        left = 3
        right = 3
        mid = 3+3//2 = 3, 3^2 = 9 > 8, decrease right by 1
        
        left = 3
        right = 2
        
        while loop stops because right is now less than left, (so left <= right) condition is not met
        
        return right because we know the actual decimal square root is 2.8 (between 2 and 3) but because we're truncating,
        return the smaller value
        
        
        '''
        
        
        