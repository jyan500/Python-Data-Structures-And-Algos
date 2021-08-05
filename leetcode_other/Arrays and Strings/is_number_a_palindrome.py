'''

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Follow up: Could you solve it without converting the integer to a string?

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## reverse the digits of the number and compare the original to the reverse
        ## O(N) since we iterate through each digit
        ## O(1) space
        ## https://leetcode.com/problems/palindrome-number/discuss/1384093/Python%3A-Without-converting-into-string
        original = x
        reverse = 0
        if x == 0:
            return True
        else: 
            while x > 0:
                ## this gives us the last digit 
                remainder = x % 10
                ## build the reverse
                reverse = (reverse * 10 ) + remainder
                ## shrink x by removing the last digit via integer division
                x = x//10
            if original == reverse:
                return True
            else :
                return False
        
        '''
        test case 1221
        1st iteration
        remainder = 1221 % 10 = 1
        reverse = (0 * 10) + remainder = 1
        x = x // 10 = 1221 // 10 = 122
        
        2nd iteration
        remainder = 122 % 10 = 2
        reverse = (1 * 10) + remainder = 10 + 2 = 12
        x = x // 10 = 122 // 10 = 12
        
        3rd iteration
        remainder = 12 % 10 = 2
        reverse = (12 * 10) + remainder = 120 + 2 = 122
        x = x // 10 = 12/10=2
        
        4th iteration
        remainder = 2 % 10 = 1
        reverse = (122 * 10) + remainder = 1220 + 1 = 1221
        x = x // 10 = 2 // 10 = 0
        
        x is now 0, so the while loop is broken
        
        original == reverse, so we return True

        test case -121
        original = -121
        reverse = 0
        will not go into the iteration x > 0, since x is less than 0 

        original != reverse, return False

        
        '''
        
    
        