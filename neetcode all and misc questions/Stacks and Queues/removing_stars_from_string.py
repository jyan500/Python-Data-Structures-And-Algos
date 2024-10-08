"""
https://leetcode.com/problems/removing-stars-from-a-string/
Revisited 10/8/2024
"""
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "*":
                if len(stack) > 0:
                    stack.pop()
                continue
                    
            stack.append(s[i])
        return "".join(stack)