'''
https://www.youtube.com/watch?v=sSno9rV8Rhg
Without memoization: O(2^n) time because for each character in the string we're checking 2 possible subproblems, with another 2 possible subproblems, etc
With memoization: O(M*N), because we're calculating only for the number of distinct subproblems, which would be M*N
'''
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