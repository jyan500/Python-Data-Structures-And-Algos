class Solution:
    def clearDigits(self, s: str) -> str:
        """
		https://leetcode.com/problems/clear-digits/description/
        delete the first digit and the closest non digit character to its left
        operation cannot be performed if there's no digit that doesn't have any
        non-digit character to its left

        since we're looking for the closest non-digit character to the left
        , a stack makes sense here, since we just look at the top of the stack
        for example
        cb34
        deleting 3 and then "b"
        leaves c4

        and then deleting 4 and c, because c is now the first non-digit
        character to the left of 4

        """
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                top = stack[-1]
                if s[i].isdigit() and not top.isdigit():
                    stack.pop()
                    continue
            stack.append(s[i])
        return "".join(stack)

