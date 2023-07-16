'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

https://leetcode.com/problems/minimum-window-substring/
https://www.youtube.com/watch?v=jSto0O4AJbM&t=615s&ab_channel=NeetCode
'''

"""
revisited on 7-15-2023
same solution as below from neetcode, O(N) time and O(N) space
one slight difference is that the "need" variable is based off the length
of the string T instead of the length of the letterCount dictionary
as a result, when checking whether we need to increment the "have" variable, 
we increment only until we reach the amount of characters specified in letterCount,
thus the initSubstringLetterCount[s[i]] <= letterCount[s[i]]
"""
 
class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        letterCount = dict()
        initSubstringLetterCount = dict()
        for i in range(len(t)):
            if t[i] in letterCount:
                letterCount[t[i]] += 1
            else:
                letterCount[t[i]] = 1
                
        minStringStart = 0
        minStringEnd = 0
        minLength = float("inf")

        l = 0
        have = 0
        need = len(t)
        for i in range(len(s)):
            if s[i] in initSubstringLetterCount:
                initSubstringLetterCount[s[i]] += 1
            else:
                initSubstringLetterCount[s[i]] = 1

            if s[i] in letterCount and initSubstringLetterCount[s[i]] <= letterCount[s[i]]:
                have += 1    
            # if we have all necessary characters, try decreasing the window
            # from the left side to get a shorter string
            while (have == need):
                # if we have all necessary characters, check to see if we have the min length
                if (i - l + 1) < minLength:
                    minLength = i - l + 1
                    minStringStart = l
                    minStringEnd = i
                # decrease the count for the given letter when shrinking the window
                # from the left side
                initSubstringLetterCount[s[l]] -= 1
                # in the case where we have the same character in initSubstringLetterCount
                # multiple times, we only decrement our "have" if the amount of characters
                # is below the amount we need from letterCount. This is because even with
                # multiple characters, we still have the right amount of characters, up until
                # we dip below the amount specified in letterCount
                if s[l] in letterCount and initSubstringLetterCount[s[l]] < letterCount[s[l]]:
                    have -= 1
                l += 1

        # return the min string if we've found a substring, otherwise
        # return empty string
        return s[minStringStart:minStringEnd+1] if minLength != float("inf") else ""
                        
                    
                
                
                        
class BruteForce:
    def minWindow(self, s: str, t: str) -> str:
        # brute force O(N^2)
        # generate two dicts
        # one that holds all the letters of t and their respective counts
        # and another one that just holds the letters with init values of 0
        # this is because we want to fill in the latter dict to see if the 
        # counts of the letters within the substring match with t
        letterCount = dict()
        initSubstringLetterCount = dict()
        for i in range(len(t)):
            if t[i] in letterCount:
                letterCount[t[i]] += 1
            else:
                letterCount[t[i]] = 1
                initSubstringLetterCount[t[i]] = 0
                
        minString = []
        minLength = float("inf")
        curString = []
        # use the copy function to avoid substringLetterCount from being a reference
        substringLetterCount = initSubstringLetterCount.copy()
        for i in range(len(s)):
            curString.append(s[i])
            if s[i] in substringLetterCount and substringLetterCount[s[i]] < letterCount[s[i]]:
                substringLetterCount[s[i]] += 1
                # if this substring contains all the letters of t and
                # its length is less than the minString, update minString
                if substringLetterCount == letterCount:
                    if len(curString) < minLength:
                        minLength = len(curString)
                        minString = curString
                        # if the substring is found, break because 1 is the smallest
                        # length that can be found
                        break
          
            # start creating substrings from one index after i
            for j in range(i+1, len(s)):
                curString.append(s[j])
                # we want to fill in the substringLetterCount so it has the same count
                # for each letter as letterCount, so if we see the same character multiple times,
                # make sure it doesn't exceed the amount in letterCount
                if s[j] in substringLetterCount and substringLetterCount[s[j]] < letterCount[s[j]]:
                    substringLetterCount[s[j]] += 1
                # if this substring contains all the letters of t and
                # its length is less than the minString, update minString
                if substringLetterCount == letterCount:
                    if len(curString) < minLength:
                        minLength = len(curString)
                        minString = curString
                    # break out of the loop because any remaining substrings will meet this 
                    # condition but fail the length check
                    # since it's always going to be
                    # longer than the first substring we find
                    break
                # if the curString has already exceeded the length of the min string,
                # just break
                if len(curString) > minLength:
                    break

            # once the loop finishes, reset curString and substringLetterCount
            curString = []
            substringLetterCount = initSubstringLetterCount.copy()

        return "".join(minString)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = dict()
        for char in t:
            if (window.get(char) != None):
                window[char] += 1
            else:
                window[char] = 1
        have = 0
        minWindow = dict()
        need = len(window)

        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            cur = s[r]
            if (minWindow.get(cur) != None):
                minWindow[cur] += 1
            else:
                minWindow[cur] = 1
            ## check to see if the character from the right pointer is in the window and
            ## the count of that char is the same 
            if (cur in window and minWindow[cur] == window[cur]):
                have += 1
            while (have == need):
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of minWindow
                minWindow[s[l]] -= 1
                ## if we are at a character in the substring, subtract one more from the have variable
                ## in order to exit this while loop
                if (s[l] in window and minWindow[s[l]] < window[s[l]]):
                    have -= 1
                l += 1
        l = res[0]
        r = res[1]
        return s[l:r+1] if resLen != float("infinity") else ""
