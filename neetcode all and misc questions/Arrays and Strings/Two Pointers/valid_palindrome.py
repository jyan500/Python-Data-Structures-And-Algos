"""
https://leetcode.com/problems/valid-palindrome/
This is a slightly harder version of a classic problem,
where you can have strings with spaces and alphanumeric characters

Still use two pointers, but in the case one of the pointers is pointing at a 
non-alphanumeric character, you increment that one, and then if the other pointer
is pointing at a proper alphanumeric character, you would not increment it.

This way, you ensure that the pointers are only comparing alphanumeric characters

Also have to use .lower() since casing isn't considered here during comparison

Time: O(N)
Space: O(1)

2/25/2025
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l <= r):
            # if the left side is not alphanumeric but the right side is
            # only increment the left side
            if not s[l].isalnum() and s[r].isalnum():
                l += 1
            # if the right side is not alphanumeric but the left side is,
            # only increment the right side
            elif not s[r].isalnum() and s[l].isalnum():
                r -= 1
            # if neither side is alphanumeric, increment both sides
            elif not s[r].isalnum() and not s[l].isalnum():
                r -= 1
                l += 1
            # if they're both alphanumeric, compare them (and ignore casing)
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
           
        return True