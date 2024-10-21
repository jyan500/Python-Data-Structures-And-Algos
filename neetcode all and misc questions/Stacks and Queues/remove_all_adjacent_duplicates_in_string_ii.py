class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Optimized Solution
        Add characters to stack, but also keep track of the count of the last character within a tuple
        if the top of the stack == character, we increment the count
        If the top of the stack character frequency == k, we pop out that record from the stack
        
        This is allows us to know the count of the previous character without having to loop backwards like in the previous solution.
        It also solves the issue with using a hashmap, as we're interested in knowing the PREVIOUS characters' count within the stack,
        and not necessarily the counts across the entirety of the string s.
        
        O(N) Time
        O(N) Space
        """
        stack = []
        for i in range(len(s)):
            if (len(stack) > 0):
                char, frequency = stack[-1]
                if char == s[i]:
                    frequency+=1
                    stack[-1] = (char, frequency)
                    if frequency == k:
                        stack.pop()
                    continue
            stack.append((s[i], 1))
         
        res = ""
        for i in range(len(stack)):
            res += (stack[i][0] * stack[i][1])
        return res
        """
        Brute Force Solution:
        Add characters to stack
        At each k, look backwards k characters and see if all characters are the same, if so pop from the stack
        O(N*k)
        """
        # from collections import defaultdict
        # stack = []
        # for r in range(len(s)):
        #     stack.append(s[r])
        #     if (len(stack) >= k):
        #         allSame = True
        #         for i in range(len(stack)-1,len(stack)-k-1,-1):
        #             if s[r] != stack[i]:
        #                 allSame = False
        #                 break
        #         if allSame:
        #             for i in range(k):
        #                 if len(stack) > 0:
        #                     stack.pop()
        #                 else:
        #                     break
        # return "".join(stack)