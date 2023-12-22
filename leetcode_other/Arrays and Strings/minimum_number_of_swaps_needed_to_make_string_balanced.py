""" https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/submissions/ """
class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Note: This is a Leetcode Weekly Contest Problem, not sure if 
        it's realistic to show in an interview setting.
        
        balanced string conditions
        1) empty string (" ")
        2) []
        3) [[]]
        
        not balanced
        ][][
        
        ] ] ] [ [ [
        0 1 2 3 4 5
        
        swaps index 0 and index 4
        [ ] ] [ ] [
        0 1 2 3 4 5
        
        swaps index 1 and index 5
        [ [ ] [ ] ]
        0 1 2 3 4 5
        
        Brute Force solution:
        1) Find all balanced parenthesis combinations based on the length of s
        2) Taking a balanced version, and then counting the differences between the balanced and the current s, and then divide by 2 to get the number of swaps
        3) find the min
        """
        """
        n = len(s)
        self.parens = []
        def getBalancedParens(numLeft, numRight, cur, stack):
            if numLeft == 0 and numRight == 0:
                self.parens.append(cur)
            if numRight != 0:
                getBalancedParens(numLeft, numRight - 1, cur + "[", stack + ["["])
            if numLeft != 0 and len(stack) > 0:
                stack.pop()
                getBalancedParens(numLeft - 1, numRight, cur + "]", stack)
           
        getBalancedParens(n/2, n/2, "", [])
        minDiff = float("inf")
        for i in range(len(self.parens)):
            count = 0
            for j in range(len(self.parens[i])):
                if self.parens[i][j] != s[j]:
                    count += 1
            minDiff = min(count//2, minDiff)
        return minDiff
        """
        """
        Optimized Solution (Neetcode + Leetcode Discuss)
        First cancel out all the valid pairs, 
        then you will be left with something like ]]][[[ , and the answer will be ceil(m/2). Where m is the number of pairs left.
        
        The intuition is tricky. Would recommend revisiting the following two links for a better explanation
        https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1390319/How-to-reach-the-optimal-solution-or-Explained-with-Intuition-and-Diagram
        https://www.youtube.com/watch?v=3YDBT9ZrfaU&t=592s&ab_channel=NeetCode
        """
        
#         close, maxClose = 0, 0
#         for c in s:
#             if c == "[":
#                 close -= 1
#             else:
#                 close += 1
#             maxClose = max(close, maxClose)
        
#         return (maxClose+1)//2
    
        """
        Someone in the youtube comments of Neetcode had a nice solution which I'll display here
        by @YT.Nikolay
        
        'Basically, I count opened and closed, and when closed > opened, I do a swap AND decrease closed AND increase opened counters. Accepted! =)'
        
        example 1:
        s = "] [ ] [ "
        
        1st iteration
        closed = 1
        opened = 0
        2nd iteration 
        closed = 1
        opened = 1
        3rd iteration
        closed = 2
        opened = 1
        
        closed > opened, so this would require at least one "swap"
        increment swaps, swaps = 1
        decrement closed, closed = 1
        increment opened, opened = 2
        
        4th iteration
        closed = 1
        opened = 3
        
        returns 1
        
        s = "] ] ] [ [ [ [ ]"
        1st iteration
        closed = 1
        opened = 0
            
        closed > opened,
        closed -= 1, closed = 0
        opened += 1, opened = 1
        swaps += 1, swaps = 2
        
        2nd iteration
        closed = 1
        opened = 1
        
        3rd iteration
        closed = 2
        opened = 1
        
        closed > opened
        closed = 1
        opened = 2
        
        4th iteration
        closed = 1
        opened = 3
        
        5th iteration
        closed = 1
        opened = 4
        
        6th iteration
        closed = 1
        opened = 5
        
        7th iteration
        closed = 1
        opened = 6
        
        8th iteration
        closed = 2
        opened = 6
        
        returns swaps = 2
        
        """
        
        # opened, closed = 0, 0
        # swaps = 0
        # for c in s:
        #     if c == "[":
        #         opened += 1
        #     else:
        #         closed += 1
        #     if closed > opened:
        #         swaps += 1
        #         closed -= 1
        #         opened += 1
        # return swaps
        
        """ Here's another similar idea by someone leetcode discuss: 
        https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/3026899/Python-Simple-Greedy-Solution-or-TimeO(N)-SpaceO(1)
        
        To fix the string we simply need to ensure that every close bracket has an open bracket. We simply change invalid close brackets to open brackets.

**As the problem states there is an equal number of closing brackets and open brackets, we can assume that we will optimally swap a bad closed bracket with an open bracket later in the string. Note: we don't actually have to do the swaps, merely counting the required swaps is good enough!

        using example from above:
        s = "] ] ] [ [ [ [ ]"
        
        1st iteration
        current_open = 0, and it's a closing bracket,
        so apply fix here by changing to open bracket,
        increment fixes applied to 1
        increment current_open to 1
        
        2nd iteration
        current_open = 1, this is a closed bracket though, so we "spend" the open bracket
        to pair with the closing bracket
        decrement current_open to 0
        
        3rd iteration
        current_open = 0, this is a closed bracket, so apply fix here by
        changing to open bracket
        increment fixes applied to 2
        increment current_open to 1
        
        4th iteration
        this is an opening bracket, so increment current_open by 1
        current_open to 2
        
        ...
        
        you can see that there's no more fixes needed after the third iteration
        
        returns 2
        """
        
        fixes_applied = 0
        current_open = 0

        for c in s:
            if c == '[':            # Open is always considered OK
                current_open += 1

            elif current_open > 0:  # Valid Closings are OK
                current_open -= 1 # this "spends" one open bracket to pair with a closing bracket
                
            else:                   # Invalid Closings Require a Fix, meaning there's no opening bracket to pair with the closing bracket. So we "change" the invalid closed bracket to an open bracket
                fixes_applied += 1
                current_open += 1

        return fixes_applied