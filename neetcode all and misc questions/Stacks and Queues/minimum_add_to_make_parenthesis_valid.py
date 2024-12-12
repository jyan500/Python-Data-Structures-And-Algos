class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        in order for a parenthesis string to be valid, there must be the same amount
        of opening and closing braces
        
        we can evaluate how many proper parens are present similar to the valid parenthesis problem
        using a stack, and then based on the amount of parenthesis left on the stack, the amount of braces left determine
        the amount that would be required to make it valid.    
        """
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                    continue
            stack.append(s[i])
        return len(stack)