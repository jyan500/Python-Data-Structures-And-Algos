'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the strin

Problem: https://leetcode.com/problems/palindromic-substrings/

O(N^2) Time, O(N^2) Space DP Solution
Explanation: https://www.youtube.com/watch?v=EIf9zFqufbU&ab_channel=AlexanderLe

O(N^2) time, O(1) space "Expand around the center" solution:
https://www.youtube.com/watch?v=4RACzI5-du8&ab_channel=NeetCodeNeetCode
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Revisited 6/9/2025
        Brute Force solution:
        1) writing a separate isPalindrome function that applies the two pointer strategy
        starting from the beginning and end
        2) applying nested loops, find every substring in S, and then apply the isPalindrome function
        to all of those substrings

        More optimized:
        loop through each letter
            at each letter, apply start two pointers at the current index
            of the letter, and then going outwards, check if they are the same
            letter. If so, this is a palindromic substring, increment our result by one

        apply the algorithm twice, once where the two pointers start at the same index,
        and one where the pointers start at (index, index+1), to account for
        even length palindromes
        i.e 
        "acaa"
           ^
           aa would be an even length palindrome here
        """
        res = 0
        # get all odd-numbered length palindromes
        for i in range(len(s)):
            l = i
            r = i
            while (l >= 0 and r <= len(s) - 1):
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1
        # get all even numbered length palindromes
        for i in range(len(s) - 1):
            l = i
            r = i + 1
            while (l >= 0 and r <= len(s) - 1):
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1
        return res

# Revisited on 7-14-2023
class Solution2:
    # def isPalindrome(self, s: str) -> int:
    #     left = 0
    #     right = len(s) - 1
    #     while (left <= right):
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
    
    def countSubstrings(self, s: str) -> int:
        """
        Brute Force
        O(N^3), creating substrings i to j, including itself, which is O(N^2) and for each
        substring, check if its a palindrome, which is O(N)
        O(N^2 * N)
        """
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if self.isPalindrome(s[i:j+1]):
        #             count += 1
        # return count
        """
        Optimal Solution
        Check palindrome by having two pointers that start together
        at i, but move outwards
        Finding odd numbered length substrings i.e s = A A A, where i = 1 here
        left = 1, right = 1
        S[1] == S[1], this is a palindrome
        move outwards by checking left -= 1, right += 1
        left = 0, right = 2, s[0] == s[2], so this is a palindrome
        
        We need to check for even numbered length substrings as well, s = A A A,
        such as "A A"
        we can do this by setting left = i, right = left + 1
        A A A, where i = 1
        left = 1 right = 2
        s[1] == s[2], this is a palindrome
        
        Time complexity:
        O(2(N^2)), for each character, iterates through the whole substring by moving both pointers outward
        performs the same N^2 operation twice for odd and even length substrings
        Space complexity: O(1) no additional space
        """
        count = 0
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
            left = i
            right = left + 1
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
        return count

class Solution:
    def printMatrix(self, matrix):
        s = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s += str(matrix[i][j]) + ' '
            print(s)
            s = ''
    def countSubstringsDP(self, s: str) -> int:
        ## represent the string s as a 2-D array
        dp = []
        counter = 0
        for i in range(len(s)):
            inner = []
            for j in range(len(s)):
                ## at the diagonal, it will be referring to just one letter, which is considered a valid palindrome
                ## so it will be marked as 1
                if (i == j):
                    inner.append(1)
                    counter += 1
                else:
                    inner.append(0)
            dp.append(inner)
        ## loop through the dp array in a way
        ## where we only look at the cells i, j past the "diagonal" of 1's that we inserted
        ## in a way where we loop through each column of the dp array, rather than through the rows like norma
        ## since if we looked at cells before, these would be "mirrors", it would be double counting.
        ## self.printMatrix(dp)
        
        ## the way this loop works is that we skip the 1st column (since that would be (0,0)), we already know that value is 1
        ## then, hold j constant, and increase i so that we go further down the column
        ## then once i == j (we hit the diagonal of the matrix), go back to the next column
        for j in range(1, len(dp[0])) :
            for i in range(j):
                ## if the string is 2 characters long, and the first and last character are equal, its a palindrome
                ## we can actually check if the string is 2 characters long exactly if the cell below it is
                ## on the diagonal, since any character on the diagonal is length of 1
                is_bottom_cell_on_diagonal = i == j - 1 
                lower_left_cell = dp[i+1][j-1]  
                if (is_bottom_cell_on_diagonal and s[i] == s[j]):
                    counter += 1
                    dp[i][j] = 1
                ## if the string length is greater than 2 characters, check to see if the inner substring within this string
                ## is a palindrome by checking the lower left cell's value, since the lower left cell represents 
                ## the substring within this current string we're looking at, and we can see whether that is a palindrome or not      
                ## if the inner substring is a palindrome, then just check the first and last characters in the string
                ## to see if they're equal
                elif lower_left_cell == 1 and s[i] == s[j]:
                    counter += 1
                    dp[i][j] = 1
        ## self.printMatrix(dp)
        return counter
                    

    def countSubstringsExpandAroundCenter(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            left_pointer = i
            right_pointer = i
            ## expand around the center, count all odd numbered palindromes
            counter += self.countPalindromes(s, left_pointer, right_pointer)
            ## expand around the center, count all even numbered palindromes
            counter += self.countPalindromes(s, left_pointer, right_pointer + 1)
            
        return counter

    def countPalindromes(self, s: str, left_pointer : int, right_pointer : int) -> int:
    	counter = 0
    	while (left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]):
	        counter += 1
	        left_pointer -= 1
	        right_pointer += 1
	    return counter
