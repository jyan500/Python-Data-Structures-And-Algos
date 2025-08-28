class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
        8/28/2025 
        
        s = "(ed(et(oc))el)"
        oc -> co
        etco -> octe
        edocteel -> leetcode

        if we kept a stack, we can apply the valid parenthesis logic to pop
        off the stack when seeing a valid parenthesis pair.

        Also if we kept another stack of only the string elements, each time we pop a parenthesis,
        we can also pop off the stack with only the string elements, since we know these will be the elements
        we need to reverse as they are inside the last pair of parenthesis we're currently looking at.

        We then pop off, reverse it, and concatenate to the current top of the stack

        The key is that we add to an existing "string" on the elements list, and when we see a "(", we know
        that this is the start of a new string, so we just append an empty string to the elements list, and continue
        adding onto it (i.e elements[-1] += s[i])
        
        stack = [(]
        elements = [ed]

        stack = [(, (]
        elements = [ed, et]
        
        stack = [(, (, (]
        elements = [ed, et, oc]

        here we see the first closing brace
        stack = [(, (]
        elements = [ed, et]
        pop off oc and reverse it, and then concatenate to the top of the stack
        elements = [ed, etco]

        here we see the 2nd closing brace
        stack = [(]
        elements = [ed, etco], pops off etoc and reverses it, and concatenates to ed
        elements = [edocte]

        stack = [(]
        elements = [edocteel]

        sees the last closing brace
        stack = []
        elements = [edocteel], pops off edocteel, reverses it
        edocte, le, concatenates
        stack = [leetcode]
        finally, retrieves element[0] and returns it
        leetcode

        Time Complexity: O(N^2), because of string concatenation
        Space Complexity: O(N)

        **** More optimal solution ****
        According to claude, a more efficient (but similar idea) is to only store a single stack of nested lists,
        and simplifying the logic so that we don't actually keep a stack of parenthesis. 

        using this new logic, we just append to the nested list if our current s[i] is not a "(" and ")"
        and then whenever we see a "(", we append a new list inside the stack (instead of a new string)

        The optimized solution is O(N) since now we do minimal O(M+K) work inside the loop to reverse one of the inner lists,
        but it doesn't change the overall time complexity like string concatenation does.

        """
        stack = [[]]
        for i in range(len(s)):
            if s[i] != "(" and s[i] != ")":
                stack[-1] += s[i]
            elif s[i] == "(":
                stack.append([])
            if len(stack) > 0:
                if s[i] == ")":
                    inner = stack.pop()
                    inner.reverse()
                    stack[-1].extend(inner)
        return "".join(stack[0])

        # Original Solution below:
        # curString = ""
        # parens = [] 
        # elements = []
        # for i in range(len(s)):
        #     if s[i] != "(" and s[i] != ")":
        #         if len(elements) == 0:
        #             elements.append(s[i])
        #         # if we're still inside an opening brace, we continue adding characters to the existing string
        #         # at the top of the stack
        #         else:
        #             elements[-1] += s[i]
        #     else:
        #         # once we hit another opening brace, we start a "new" string by appending an empty string
        #         # at the top of the elements list, so future characters will be added to this string instead
        #         # of the previous one
        #         if s[i] == "(":
        #             elements.append("")
        #         parens.append(s[i])

        #     if len(parens) > 0 and len(elements) > 0:
        #         if parens[-1] == ")":
        #             parens.pop()
        #             cur = list(elements.pop())
        #             cur.reverse()
        #             if len(elements) > 0:
        #                 elements[-1] = elements[-1] + "".join(cur)
        #             else:
        #                 elements.append("".join(cur))
        # return "".join(elements[0])