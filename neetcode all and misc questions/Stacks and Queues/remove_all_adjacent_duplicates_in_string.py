class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        using a stack, check if the top of the stack == current char,
        this means it's 2 consecutive letters that are the same. We can
        pop the top of the stack here and move onto the next character
        """
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == s[i]:
                    stack.pop()
                    continue
            stack.append(s[i])
        return "".join(stack)