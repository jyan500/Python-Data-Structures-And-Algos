'''
https://www.youtube.com/watch?v=sSno9rV8Rhg
Without memoization: O(2^n) time because for each character in the string we're checking 2 possible subproblems, with another 2 possible subproblems, etc
With memoization: O(M*N), because we're calculating only for the number of distinct subproblems, which would be M*N
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1/2/2026
        Revisited with a similar top-down solution as below
        2-D Dynamic Programming, since you need the ability
        to backtrack here
        abcde
        acbdef

        the longest would be 4 (abde)

        need to track two pointers in the recursion

        knapsack relation
        we can either choose both characters if the values are equal
        to each other and add to the current result OR if they aren't equal:
        increment only one of the indices and keep the other the same

        Brute Force solution finds all the different possibilities,
        Use memoization by storing the individual states at (i,j)

        """
        M = len(text1)
        N = len(text2)
        self.memo = {}
        def dfs(i,j):
            curLen = 0
            # base case, if we're at the end of one of the strings,
            # the longest common subsequence would be 0,
            # and the previous recursive calls will then "build" up
            # the result by adding 1 if the two values are the same
            if i >= M or j >= N:
                return 0
            if (i,j) in self.memo:
                return self.memo[(i,j)]
            # if both strings are the same,
            # that means we increment both indices, and also add 
            # 1 to the total result
            if text1[i] == text2[j]:
                curLen = max(curLen, 1 + dfs(i+1,j+1))
                self.memo[(i,j)] = curLen
            else:
                # pick one but keep the other value the same
                skipLeft = dfs(i+1, j)
                skipRight = dfs(i, j+1)
                curLen = max(curLen, skipLeft, skipRight)
                self.memo[(i,j)] = curLen
            return self.memo[(i,j)]
        return dfs(0,0)

class Solution:
    ## TLE solution, this O(2^n) because for each character in the string we're checking 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)
        memo = dict()
        return self.search(text1, text2, N1, N2, 0, 0, memo)
    ## the idea behind this recursion is that 
    ## we continously search one of the strings, incrementing the index until we find a matching character with the other string
    ## then we increment both indices and add one to the result
    ## when one of the strings is fully traversed, we try doing the same for the other string
    def search(self, text1: str, text2: str, N1: int, N2: int, i: int, j: int, memo : dict):  
        if (memo.get((i,j)) != None):
            return memo[(i,j)]
        elif (i == N1 or j == N2):
            memo[(i,j)] = 0
            return 0
        elif (text1[i] == text2[j]):
            res = 1 + self.search(text1, text2, N1, N2, i+1,j+1, memo)
            memo[(i,j)] = res
            return res
        
        else:
            res = max(self.search(text1,text2,N1,N2,i+1,j,memo), self.search(text1,text2,N1,N2,i,j+1,memo))
            memo[(i,j)]=res
            return res