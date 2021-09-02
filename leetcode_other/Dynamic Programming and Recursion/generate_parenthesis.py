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
        