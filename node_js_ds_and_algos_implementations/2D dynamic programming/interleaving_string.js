class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """ 
        backtracking using three pointers
        since we need to maintain the relative order, we can go index by index
        on each string
        if two strings at the same index have the same letter, this is where the backtracking comes
        in since we need to visit both of these paths 
        (exponential time)
        Note that because s3 is always determined by how many characters we have taken from s1 and s2,
        we only need to store (i,j) in the memo instead of (i,j,k), we could technically add k
        to the memo key and it would still be the right answer, but it's un-necessary since it doesn't
        result in a unique state that would need to be memoized.

        Time: O(M*N)
        Space: O(M*N)
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        memo = {}
        def dfs(i, j, k):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len_s1 and j == len_s2 and k == len_s3:
                return True
            pick_i = False
            pick_j = False
            if i < len_s1 and s1[i] == s3[k]:
                pick_i = dfs(i+1, j, k+1)
            if j < len_s2 and s2[j] == s3[k]:
                pick_j = dfs(i, j+1, k+1)
            memo[(i,j)] = pick_i or pick_j
            return memo[(i,j)]
        return dfs(0,0,0)
            

