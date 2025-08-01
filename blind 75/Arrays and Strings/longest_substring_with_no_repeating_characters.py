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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Revisited 7/30/2025
        Revisited 2/28/2025
        sliding window
        keep a hashmap since there's no repeating characters,
        the count of each character must be 1
        as soon as we see a character is in the hashmap more than once,
        we shrink the window until the value is back to 1

        O(N) Time
        O(N) Space
        """
        from collections import defaultdict
        l = 0
        counter = defaultdict(int)
        res = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while (counter[s[r]] > 1):
                counter[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Revisited on 9/25/2024
        https://neetcode.io/problems/longest-substring-without-duplicates
        'abacde'
        'abacfcghi'
        'abbcdef'
        O(N) Time O(N) Space solution
        """
        seen = set()
        l = 0
        r = 0
        maxLength = 0
        currentLength = 0
        while (r < len(s)):
            if (s[r] in seen):
                """
                if the character at the right pointer is already seen,
                remove the character represented at the left pointer from the set,
                and then shift the left pointer by one. And decrease current length
                """
                maxLength = max(currentLength, maxLength)
                seen.remove(s[l])
                currentLength-=1
                l += 1
            else:
                """
                if you see a non-duplicated character, then increase the current length
                add the current character to the set
                re-calculate the current length
                increment right pointer
                """
                currentLength += 1
                maxLength = max(currentLength, maxLength)
                seen.add(s[r])
                r += 1
        return maxLength

class Solution:
	"""
	Revisited on 7-6-2023
	Concept is when iterating through the string,
	keep track of a dictionary that maps the character to its index
	if character is already in dict, that means it's repeating,
	so we start keeping track of a new substring starting at the 
	first instance of the repeating character + 1

	i.e dvdffefgh
	i = 0 and i = 1:
	charMap = {d: 0, v: 1} so far, longest so far is 2

	i = 2:
	when reaching index 2, d is already found,
	so start the new substring at "v"
    
    i = 1 again, does two more iterations to i = 3	
	{v: 1, d: 2, f: 3}
	longest so far is 3, update longest to 3

	i = 4
	f is already in the dict, so we go back to the first instance of the repeating
	char + 1 to start a new substring (i = 4)

	i = 4, i = 5
	{f: 4, e: 5}

	i = 6,
	f is already in the dict, go back to the first instance of the repeating
	char + 1 to start a new substring (i = 5)

	{e: 5}

	i = 6 to i = 8
	{e: 5, f: 6, g:7, h:8}, this is greater than
	the longest we've found, update to 4

	4 is our answer

	"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charMap = dict()
        i = 0
        while i < len(s):
            # if repeating character is found in the substring, 
            # set the index back to the first instance of the repeating character + 1
            # to start the new substring
            if s[i] in charMap:
                i = charMap[s[i]] + 1
                charMap = dict()
            else:
                charMap[s[i]] = i
                i += 1
            # keep track of the longest substring
            longest = max(longest, len(charMap))
        return longest

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