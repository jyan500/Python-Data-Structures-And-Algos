"""
https://leetcode.com/problems/backspace-string-compare/
O(N) time and O(N) space solution
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == "#":
                if len(stack1) != 0:
                    stack1.pop()
                continue
            stack1.append(s[i])
        for i in range(len(t)):
            if t[i] == "#":
                if len(stack2) != 0:
                    stack2.pop()
                continue
            stack2.append(t[i])
        return stack1 == stack2