class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Brute Force:
        1) make every combination of parenthesis based on the asterisk 
        (this adds three new options, "(", ")" or "")
        2) check if the created combination is valid
        
        Time limit exceeded because we keep track of every combination
        O(3^N), for each asterisk we try 3 different values
        
        Optimizations
        -------------
        https://www.youtube.com/watch?v=QhPdNS143Qg&ab_channel=NeetCode
        https://github.com/neetcode-gh/leetcode/blob/main/python%2F0678-valid-parenthesis-string.py

        Instead of keeping a stack in memory, we can just keep track of the number
        of "left" parenthesis that are remaining. 
        
        if we see a "left" parenthesis, we increment he left parenthesis amount by one
        
        if we see a "right" parenthesis, we decrement the left parenthesis amount by one

        That allows us to use memoization
        to track at every i, see how many left parenthesis are remaining and if we can 
        create a valid parenthesis string starting from i. There are cases where repeated work is done
        at a given i, there might be the same amount of left parens. We can track whether a valid string
        can be created given the rest of the string, and the amount of left parens remaining.
        
        If there are no left parenthesis at the end, that means this parenthesis string
        is valid.
        
        Using memoization, the time complexity is reduced to O(N^3), but it takes O(N^2) space to 
        store the memoization
        
        """
        # we put a dummy entry in the memo where if i is equal to the
        # len(string), and there are no left parens, this is valid
        self.memo = {(len(s), 0): True}
        def helper(i, left):
            if (i, left) in self.memo:
                return self.memo[(i, left)]
            """
                the left < 0, return false
                condition accounts for the following edge case where you have a right paren followed by a left paren like these: 
                "(*)(", ")("

                The reason why this causes it to fail without it is because
                left can be 0 when we reach the end of the string, but it's not valid because
                it creates this combination right before:
                ()), left would become -1, and then adds the final string ( to make ())(
                this would get re-incremented such that left becomes 0, but this is not a valid string
                because )( is not valid
            """
            if left < 0:
                return False
            if i == len(s):
                return left == 0
            if s[i] == "(":
                self.memo[(i, left)] = helper(i+1, left+1)
            elif s[i] == ")":
                self.memo[(i, left)] = helper(i+1, left-1)
            # if asterisk, either add a left paren, add a right paren (which reduces left), or ignore
            else:
                self.memo[(i, left)] = helper(i+1, left+1) or helper(i+1, left) or helper(i+1, left-1)
            return self.memo[(i, left)]
        return helper(0, 0)
        

            
        