'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''
def lengthOfLongestSubstring(s: str) -> int:
        ## map the character to its index position in the string
        d = dict()
        ## start of the current substring
        start = 0
        ## length of current substring
        current_length = 0
        ## length of longest substring
        longest = 0
        
        for i, letter in enumerate(s):
            ## if the letter has been seen (meaning a repeating char is found) and its within our current substring
            ## note that <= to handle successive repeating characters (like 'bb')
            if letter in d and start <= d[letter]:
                ## update the start of the substring to be where the first occurence of the duplicate character was found, plus one
                start = d[letter] + 1
                
                ## update current length of the substring by subtracting the current index with
                ## the last occurence of the duplicate character
                current_length = i - d[letter]
                ## update the index position of the first occurence of the duplicate character
                d[letter] = i
            else:
                d[letter] = i
                current_length += 1
                if (current_length > longest):
                    longest = current_length
        return longest

print(lengthOfLongestSubstring('bb'))