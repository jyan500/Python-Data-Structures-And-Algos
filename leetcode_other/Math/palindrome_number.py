"""
https://leetcode.com/problems/palindrome-number/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # get the digits of x
        quotient = x
        digits = []
        while quotient != 0:
            digits.append(quotient % 10)
            quotient = quotient // 10
        left = 0
        right = len(digits) - 1
        while (left <= right):
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1
        return True
