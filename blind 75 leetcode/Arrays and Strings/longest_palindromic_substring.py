'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''

def longestPalindrome(self, s: str) -> str:
        def longestAtIndex(s, left, right):
            ## starting from the left and right pointers, expand outwards <-- -->
            ## if at any point, the characters are not equal or you're out of bounds 
            ## of the string, break out of the loop
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            length = right - left + 1
            return (left, right, length)
        left = 0
        right = -1
        longest = 0
        substr = ''
        for i in range(len(s)):
            ## start the left and right pointers at the same index for odd number palindromes
            odd_l, odd_r, odd_length = longestAtIndex(s, i, i)
            if (odd_length > longest):
                longest = odd_length
                left = odd_l
                right = odd_r
            ## start the left and right pointers at i, i + 1 for even number palindromes
            even_l, even_r, even_length = longestAtIndex(s, i, i + 1)
            if (even_length > longest):
                longest = even_length
                left = even_l
                right = even_r
        ## return the substring
        return s[left: right+1]