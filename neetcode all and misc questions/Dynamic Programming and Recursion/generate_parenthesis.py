'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Backtracking:
        n = 3
        ((())) first case
        backtracks to ...
        (( openingCount = 2 and closingCount = 3
        as long as there are more closing than opening,
        we can choose closing as an option here. 
        (()
        this next call, we can go back to choosing an opening brace by default
        since opening braces always come before closing
        """
        res = []
        def search(openingCount: int, closingCount: int, cur: str) -> None:
            # base case: no more braces to choose here
            if openingCount == 0 and closingCount == 0:
                res.append(cur)
                return
            # default to choose opening brace before closing
            if openingCount > 0:
                search(openingCount - 1, closingCount, cur + "(")
            # if we're out of opening braces and there are 
            # still closing braces, choose closing brace
            # also if we have more closing braces than opening,
            # we can also choose a closing brace
            if (openingCount == 0 and closingCount > 0) or (closingCount > openingCount):
                search(openingCount, closingCount - 1, cur + ")")

        search(n,n,"")
        return res

"""
Revisited on 9/26/2024, still same solution in 2^n time
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def search(leftCount, rightCount, cur, res):
            if (leftCount == n and rightCount == n):
                res.append(cur)
                return
            if (leftCount < n):
                search(leftCount+1, rightCount, cur + "(", res)
            """ 
            as long as there are more left parens then right parens, we can use a right parens,
            this prevents us from choosing a right parens before a left parens, which would
            create an invalid combination
            """
            if (leftCount > rightCount and rightCount < n):
                search(leftCount, rightCount+1, cur + ")", res)
        valid = []
        search(0, 0, "", valid)
        return valid
"""
Revisited on 9/8/2023
Time: O(2^n), for a given index there can be two combinations here, so 2 * 2 * 2 ... n which is 2^n
Space: O(2^n)
1) The concept is that we start with one opening brace, and then 
we can continually pick an opening brace until the number of opening braces is equal to our n
2) Then, we can continually pick closing braces
3) To make sure we don't accidentally pick a closing brace and then an opening brace,
we check that the amount of opening braces is greater than our amount of closing braces,
so we ensure that we always pick opening braces before closing braces in our recursion
4) If our number of openings and number of closings are both equal to n, we have found formed a
combination with all the pairs, so save into the global array
5) return the global array
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def dfs(numOpening, numClosing, curr):
            # if the number of openings == n and number of closing parens == n,
            # save current combination to our result and stop
            if numOpening == n and numClosing == n:
                self.res.append(curr)
                return
            # if we can continue picking opening brackets, keep picking opening brackets
            if numOpening < n:
                dfs(numOpening + 1, numClosing, curr + "(")
            """
            if we have more opening braces than closing braces and we can
            pick closing braces still, pick the closing brace. This is to prevent us 
            from picking a closing brace and then an opening brace if there are an
            equal amount of opening and closing braces, thus forming
            an invalid combination 
            Example: (i.e  "())(" )
            if n = 2, after creating (())
            the recursion backtracks to (, and then adds a closing brace to form (),
            which then creates ()(). 
            After backtracking on this case, it'd get to the single pair of braces (),
            where numOpening == numClosing.
            The numOpening > numClosing condition prevents us from choosing a closing brace
            here like so: ())
            """
            if numOpening > numClosing and numClosing < n:
                dfs(numOpening, numClosing + 1, curr + ")")
        # we always start with one opening brace, so numOpening starts at 1
        dfs(1, 0, "(")
        return self.res

class Solution:
    ## Concept: brute force, generate every possible combination of parenthesis, but only accept
    ## the ones that create a valid parenthesis structure
    ## Time complexity: O(2^2n * n), generate 2^2n sequences, the extra 2n since there's two characters for the set of parens, multiplied by an additional N to check for a valid parenthesis
    ## Space complexity: O(2^2n * n) to hold every valid sequence
    def __init__(self):
        self.combinations = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(float(n), '')
        return list(self.combinations)
    def generate(self, n: float, cur: str):
        if (n == 0):
            if (self.isValidParenthesis(cur)):
                self.combinations.append(cur)
        else:
            self.generate(n-.5, cur + '(')
            self.generate(n-.5, cur + ')')
                
            
    def isValidParenthesis(self,cur):
        i = 0
        j = len(cur)
        s = []
        for i in range(len(cur)): 
            if (len(s) > 0):
                if (cur[i] == ')' and s[-1] == '('):
                    s.pop()
                    continue
            s.append(cur[i])
        return len(s) == 0
        