'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

## Time complexity is O(2N), one iteration through the string, and one iteration through the stack
## Space complexity is O(N) because there might be cases where the string is just a bunch of 
## invalid parenthesis and would store that on the stack.

## Approach: 
## keep a stack of tuples, containing the opening parenthesis so far and its index,
## if we see a closing brace, if the top of our stack contains
## an opening brace we pop off since that would be a valid of set of braces
## however, if the top of stack does not contain a closing brace, we just append the closing brace and 
## its corresponding index to our stack

## at the end, if our stack is not empty, that means we had an invalid amount of parenthesis, and those would still be on the stack
## so we just iterate through the stack and get the index that we stored for each invalid parenthesis, and simply
## slice out the parenthesis from the original string
## after that, all invalid parenthesis will be removed to get our result

'''

# Revisited on 1/17/2024
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Approach:
        1) use a stack and push a tuple containing the parenthesis and index
        2) iterate s, as we push, if the top of our stack and the current element
        make a valid set, we remove the top of stack
        
        3) At the end, only the invalid parenthesis are left
        4) Iterate through the stack and then get the indices, remove these indices from the string
        and return
        """
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == ")":
                if len(stack) > 0:
                    paren, index = stack[-1]
                    if paren == "(" and s[i] == ")":
                        stack.pop()
                        continue
                stack.append((s[i], i))
        res = []
        iSet = set()
        for item in stack:
            paren, i = item
            iSet.add(i)
        res = [s[i] for i in range(len(s)) if i not in iSet]
        return "".join(res)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if (s[i] ==  '('):
                stack.append((s[i],i))
            if (s[i] == ')'):
                if (stack):
                    brace, index = stack[-1]
                    if (brace == '('):
                        stack.pop()
                        continue
                stack.append((s[i],i))
        if (stack):
            while (stack):
                paren, i = stack.pop()
                s = s[:i] + s[i+1:]
        return s
            