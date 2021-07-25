'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

https://leetcode.com/problems/valid-palindrome-ii/
'''
class Solution:
    '''
    Time complexity is O(N) overall, with two additional
    passes that may go through the rest of the string (its not O(N^2) because its always 
    an additional two iterations to check when we move past either the left or right character, independent of the length of the string
    Space complexity is O(1) for the constant variables '''
    def validPalindrome(self, s: str) -> bool:
        ## remove the current character
        ## check if our string is a palindrome
        l = 0
        r = len(s)-1
        delete_left = False
        delete_right = False
        backtrack_left = 0
        backtrack_right = 0
        while (l < r):
            if (s[l] != s[r]):
                ## if we get to a spot where our characters are not the same, try deleting one of the characters
                ## and continuing the iteration
                ## if we have already backtracked and tried deleting the right (after deleting the left)
                ## and we are still meeting a case where l and r aren't the same, then its not a palindrome
                ## after removing one char
                if (delete_left and delete_right):
                    return False
                ## try incrementing l once more to ignore the left hand side character to
                ## see if the string is still a palindrome
                elif (not delete_left):
                    ## try ignoring the left character
                    backtrack_left = l
                    backtrack_right = r
                    delete_left = True
                    l += 1
                    continue
                ## if deleting the left hand side character did not make a palindrome
                ## try backtracking to the position where we originally had the non-matching chars
                ## and decrement r one more and continue the iteration
                elif (delete_left):
                    delete_right = True
                    l = backtrack_left
                    r = backtrack_right
                    r -= 1
                    continue             

            l+=1
            r-=1
        return True
    '''
    test cases
    
    abc
    l = 0
    r = 2
    ac are not equal, try incrementing l + 1
    bc, still not equal, try backtracking to l = 0, r = 2, try decrementing r - 1 to move past it
    ab, still not equal
    
    abad
    a and d are not equal, try incrementing l + 1 once more to ignore a
    l = 1 
    r = 0
    b not equal to d, try backtracking to l = 0 r = 3, decrementing r - 1 to move past the d onto the a
    l = 0
    r = 2
    a = a, l = 1, r = 1, breaks out the loop and returns True
    
    abcdba
    l = 0, r = 5
    l = 1, r = 4
    l = 2, r = 3, not equal, try incrementing l once more
    l = 3, r = 3, breaks out and returns True
    
    
    
    '''

    ## O(N^2) time complexity solution, can we do better?
    def validPalindrome(self, s: str) -> bool:
        ## remove the current character
        ## check if our string is a palindrome
        N = len(s)
        if (N == 1):
            return True
        for i in range(N):
            remainder = ''
            if (i == 0):
                remainder = s[i+1:]
            elif (i == N-1):
                remainder = s[:i]
            else:
                remainder = s[:i] + s[i+1:]          
                if (self.isPalindrome(remainder)):
                    return True
                
        return False
    
    def isPalindrome(self, s: str)->bool:
        l = 0
        r = len(s)-1
        while (l < r):
            if (s[l] != s[r]):
                return False
            l+=1
            r-=1
        return True
    
    
    ''' test cases
    s = "aba"
    i = 0
    remainder = "ba"
    l = 0
    r = 1
    returns False, continue and remove the next str
    s = "aba"
    i = 1
    remainder = "aa"
    l = 0
    r = 1, s[1] == s[r] so far
    l = 1
    r = 0
    breaks out of the loop and returns True
    
    #2 
    s = "abca"
    i = 0
    remainder = s[i+1:] = s[1:] = "bca"
    l = 0
    r = 2
    
    time complexity: O(N^2), because for each character, we're looping through
    the remainder of the string minus that character
    
    '''