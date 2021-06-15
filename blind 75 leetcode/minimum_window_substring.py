'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

https://leetcode.com/problems/minimum-window-substring/
https://www.youtube.com/watch?v=jSto0O4AJbM&t=615s&ab_channel=NeetCode
'''

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
