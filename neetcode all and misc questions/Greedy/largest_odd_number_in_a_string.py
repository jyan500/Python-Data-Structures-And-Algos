class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        https://leetcode.com/problems/largest-odd-number-in-string/description/

        greedy 
        the last digit of any odd number is always an odd number,
        so we can iterate starting from the back, and then check if
        the digit is an odd number. As soon as we find an odd number,
        we can slice from 0: i to form this odd number and return it,
        since we start at the back, this would mean we get the biggest
        odd number
        example:
        35427, if we start at the back, we get digit of 7, which means
        the entire number is an odd number
        35438, 
        i = 4, digit is 8
        i = 3, digit is 3, so this is an odd number, we slice from 0 to i = 3
        to get 3543

        Time: O(N), since the slice happens at most once
        Space: O(K), where K is the length of the slice

         """
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""