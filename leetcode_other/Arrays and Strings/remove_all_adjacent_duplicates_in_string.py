'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

concept:
time complexity: O(N)
space complexity: O(N)

use a stack
iterate through the string and push the characters to our stack
if the character at the top of our stack == current character
then we know this is an adjacent duplicate
pop off the stack
continue to iterate...

at the end, our stack should only contain the unique characters, so we just return our stack


maybe we can do better in space complexity?
(This ended up being an okay solution in terms of runtime, beat the two pointer solution)
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        for i in range(len(s)):
            if (len(stack) > 0 and stack[-1] == s[i]):
                stack.pop()
            else:    
                stack.append(s[i])
        return ''.join(stack)
        
        '''
        two pointers solution?
        prev, and cur
        whenever we find two adjacent characters, slice out the two adjacents in the string
        shift the previous and cur pointers back by 1 to adjust for the characters that were lost
        in the case that previous - 1 is out of bounds, we just set prev to be 0 and cur to be 1
        
        time complexity: O(N), but for each adjacent two characters, there's a slice operation
        space : O(1)
        
        s = "abbaca"
        prev = 0
        cur = 1
        
        
        
        second iteration
        prev = 1
        cur = 2
        s[prev] == s[cur], b == b
        s = s[:prev] + s[cur+1:]
        a + aca = aaca
        prev = a
        cur = 2
        
        s = "aaaaaaaa"
        s = "--aaaaaa"
        cur 
        
        azxxzy
        prev = 0
        cur = 1
        a != z
        prev = 1
        cur = 2
        z != x
        prev = 2
        cur = 3
        x == x
        s = s[:prev] = s[:2] = "az" + s[cur+1:] = s[4:] = zy
        s = azzy
        prev -= 1 = 1
        cur = 3-=1 = 2
        '''
#         prev = 0
#         cur = 1
#         N = len(s)
#         while (cur < N):
#             if (s[prev]==s[cur]):
#                 s = s[:prev] + s[cur+1:]
#                 N = len(s)
#                 if (prev - 1 <= 0):
#                     prev = 0
#                     cur = 1
#                 else:
#                     prev -= 1
#                     cur -= 1
                
#             else:
#                 prev = cur
#                 cur += 1
#         return s
            
        
        