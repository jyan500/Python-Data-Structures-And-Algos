class Solution:
    def numTrees(self, n: int) -> int:
        """
        https://neetcode.io/solutions/unique-binary-search-trees
        This problem uses a unique concept called catalan numbers, which involves DP

        the idea is that if you have a single tree node, there is only one way to make a BST (this is the base case)
        now if you have two nodes, there are 2 ways to make a BST
        i.e if n = 2, 
        you have these two cases:
           1
             2
        and 
           2
        1

        if you have three nodes, there are 5 different cases ( as seen in the problem statement )

        Note that the recurrence relation is as follows:
        if you have 3 nodes, notice that it's actually a combination of two different possibilities
        Assuming you pick the middle node (1, 2, 3)
        the amount of BSTs you can make is actually numTrees(1 node) * numTrees(1 nodes)
        If you pick the rightmost node (3), 
        numTrees(2 nodes)
        If you pick the leftmost node(1),
        numTrees(2 nodes)

        we know that if there are 2 nodes, there can only be two possible trees (the values themselves don't matter)

        so the answer is picking a given root, find the amount of combinations left side * amount of combinations on the right side
        
        The time complexity as is would be exponential O(3^N), but this can be reduced to O(N^2) by using memoization


        """
        self.memo = {}
        def search(n):
            # if N == 1, there's only one way to make a BST
            if n <= 1:
                return 1
            if n in self.memo:
                return self.memo[n]
            res = 0
            for i in range(n):
                amt = i + 1
                if amt > 1 and amt < n:
                    # take the combinations that can be made on the left, and the combinations that can be made on the right and multiply together
                    # to get the total
                    res += search(amt-1) * search(n-amt)
                # if we're at 1, we only return the amount of combinations on the remaining on the right
                elif amt == 1:
                    res += search(n-amt)
                # if we're at the last element, we only return the amount of combinations remaining on the left
                else:
                    res += search(amt-1)
            # memoize the amount of combinations that can be made at this current amount
            self.memo[n] = res
            return res
        return search(n)

        