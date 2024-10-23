"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
Approach:
Same as valid parenthesis, except the trick is that the max depth of the parenthesis occurs
when you continually add opening braces, and then as soon as you see a closing brace,
you check the length of the stack, as this tells you the depth based on the amount of opening braces. As you
see closing braces, these will pop out the opening braces on the stack.
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == "(" and s[i] == ")":
                    maxDepth = max(len(stack), maxDepth)
                    stack.pop()
                    continue
            if s[i] == "(":
                stack.append(s[i])
        return maxDepth