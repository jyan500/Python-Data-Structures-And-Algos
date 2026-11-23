class Solution:
    def integerBreak(self, n: int) -> int:
        """
        1-D DP
        for each number, consider breaking it into two parts, and
        recursively computing the best product for each part

        You can either break a given number further, or keep it as is, which
        is where the backtracking takes place, you would want to take the max between
        these two decisions

        Time Complexity: O(N^2)
        Space: O(N)
        """
        # in this problem, we actually cache
        # the base case when num is 1, we cannot split this further,
        # so the max product is 1
        memo = {1:1}
        def dfs(num):
            if num in memo:
                return memo[num]
            # on the very first run, num will be equal to the original input,
            # so this forces us to make a split 
            to_split = 0 if num == n else num
            # from 1 to num - 1 means i and num - i will always add up to num
            for i in range(1, num):
                to_split = max(dfs(i) * dfs(num - i), to_split)
            memo[num] = to_split
            return memo[num]
        return dfs(n)
