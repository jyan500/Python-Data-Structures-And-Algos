class Solution:
    """
    https://neetcode.io/problems/validate-parentheses
    revisited 9/26/2024
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) > 0:
                top = stack[-1]
                if ((top == "[" and c == "]") or 
                   (top == "(" and c == ")") or 
                   (top == "{" and c == "}")):
                   stack.pop()
                   continue
            stack.append(c)
        return len(stack) == 0
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

def isValid(self, s: str) -> bool:
    stack = []
    if (len(s) > 0):
        for char in s:
            if (len(stack) > 0):
                top = stack[-1]
                if ((top == '(' and char == ')') or (top == '{' and char == '}') or (top == '[' and char == ']')):
                    stack.pop()
                    continue
            stack.append(char)
    return len(stack) == 0

