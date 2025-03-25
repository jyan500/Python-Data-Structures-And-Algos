'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

https://leetcode.com/problems/minimum-window-substring/
https://www.youtube.com/watch?v=jSto0O4AJbM&t=615s&ab_channel=NeetCode
'''

"""
Revisited on 3/25/2025
Brute Force Solution, doesn't pass on leetcode, but passes on Neetcode
The logic is about the same the previous solution from 9/2024 but it's cleaner than before though.
Placed the "window calculation" logic inside the while loop to prevent the strange "overshoot by one"
edge case as mentioned. 
Time: O(N*(N+M))
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        from collections import defaultdict

        # compare the counter of char t, 
        # check if every character exists from t in s
        # check that the counts in t are at least the same as the counts in s
        def containsAllChars(d1, d2):
            for key in d2:
                if key not in d1:
                    return False
                if key in d1 and d2[key] > d1[key]:
                    return False
            return True

        c = Counter(t)
        counter = defaultdict(int)
        l = 0
        minLength = float("inf")
        window = []
        minLengthWindow = ""
        for r in range(len(s)):
            counter[s[r]] += 1
            window.append(s[r])
            while (containsAllChars(counter, c)):
                # if we've found a candidate that contains all the characters,
                # calculate the window
                if (r - l + 1 < minLength):
                    minLength = r - l + 1
                    minLengthWindow = s[l:r+1]
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1

        return minLengthWindow

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Revisited again on 9/25/2024 with Brute Force
        Note this wouldn't pass on Leetcode, but it does pass on Neetcode
        https://neetcode.io/problems/minimum-window-with-characters

        Keep increasing a window until you find what you're looking for,
        and then see how much you can shrink the window since we're looking for the 
        minimum window size

        The containsAllChars function determines whether all the characters in counter c1 exists in c2,
        and also if c2 contains at least all the counts of each characters in c1 (so c1[key] <= c2[key])

        The solution uses a while (containsAllChars) to determine whether we can keep shrinking
        the substring after finding a suitable substring with all chars. The while loop does overshoot
        by one character on the left, so we have to add that character back after the while loop breaks out,
        and then check what the substring by slicing based on the left and right pointers.

        t = "CABC"
        s = "EABCECECFBACC"
        first window we find is "EABCEC", where all characters in T are found in this substring
        we can then try shrinking the left side until this condition is no longer met,
        in this case, "ABCEC" is the most we can shrink

        Time Complexity would be O(N * (N+M)), the additional N+M is for checking the dictionaries every iteration
        Space: O(N+M)

        """
        from collections import Counter
        from collections import defaultdict
        if (len(t) > len(s)):
            return ""
        counter1 = Counter(t)
        def containsAllChars(c1, c2):
            for key in c1:
                # as long as the frequency in c1 is <= frequency in c2 (since sometimes c2 can contain more characters than necessary)
                # this meets the condition. So the inverse of these conditions would return false
                if not (key in c2 and c1[key] <= c2[key]):
                    return False
            return True
        l = 0
        r = 0
        counter2 = defaultdict(int)
        shortest = ""
        while r < len(s):
            counter2[s[r]] += 1
            if containsAllChars(counter1, counter2):
                # as long as we have all the characters needed in counter2, continue shrinking the substring
                # by incrementing the left pointer
                while containsAllChars(counter1, counter2):
                    counter2[s[l]] -= 1
                    if (counter2[s[l]] == 0):
                        del counter2[s[l]]
                    l+=1
                # once the while loop breaks, we actually overshoot by one on the left,
                # so we have to add that back in
                l-=1
                counter2[s[l]] += 1
                cur = s[l:r+1]
                if (shortest == ""):
                    shortest = cur
                elif (len(cur) < len(shortest)):
                    shortest = cur
            r+=1
        return shortest

"""
Revisited on 1/24/2024
This approach is O(N*(N+M)), not as efficient as the O(N+M) solution
from neetcode but easier to remember.

The main bottleneck is the isSubsetOf method, which is O(N) to compare
the keys and values between the dictionaries
"""
class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        """
        Brute Force:
        the minimum length substring found in S must be 
        at least length of string T
        
        start with substrings of length T
        and then find all substrings of length T + 1
        T + 2 ,etc
        
        Time Complexity: O(N*M*N) (two inner loops, size N and M, and isSubsetOf is O(N), so O(N * N * M))
        
        Another Approach:
        Keep lengthening the size of the window until you've found a substring with all the characters
        present
        Use a while loop to decrease the size of the window until the string is no longer valid
        
        Time Complexity: O(N*N) if we keep the isSubsetOf function the same
        Note we do have a while loop that shortens the string, but that will always be a constant size 
        shorter than string N so it can be ignored
        """
        # parent must contain all the same keys as the child,
        # and for each value, must have >= child's value
        def isSubsetOf(child, parent):
            for key in child:
                if key in parent:
                    if parent[key] < child[key]: 
                        return False
                    else:
                        continue
                else:
                    return False
            return True
                        
        from collections import Counter
        from collections import defaultdict
        chars = Counter(t)
        m = len(s)
        n = len(t)
        # O(N^3 solution involves the two loops below)
        # for k in range(m):
        #     for i in range(m):
        #         substringLen = i + n + k
        #         if substringLen - 1 < m:
        #             substring = s[i:substringLen]
        #             substringMap = Counter(substring)
        #             if isSubsetOf(chars, substringMap):
        #                 return substring
        substringMap = defaultdict()
        cur = []
        res = []
        resLen = float("inf")
        # O(N*M) solution involves only one loop
        for k in range(m):
            cur.append(s[k])
            if s[k] in substringMap:
                substringMap[s[k]] += 1
            else:
                substringMap[s[k]] = 1
            if isSubsetOf(chars, substringMap):
                # here we continue to shorten the string until the Counter of that substring no longer represents
                # a subset of the substring T.
                # after we've shortened the string (if we've done any shortening), we can
                # update res if the length of our current substring is less than the length of res
                while (cur):
                    c = cur[0]
                    # we need to make a copy of the dictionary to apply our changes
                    # and see if we still have a valid Counter before we apply the actual changes
                    copy = substringMap.copy()
                    if c in copy and copy[c] > 0:
                        copy[c] -= 1
                    else:
                        del copy[c]
                    if not isSubsetOf(chars, copy):
                        break
                    else:
                        substringMap = copy
                        cur.pop(0)
                if len(cur) < resLen:
                    res = cur.copy()
                    resLen = len(cur)

        return "" if resLen == float("inf") else "".join(res)
                
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
