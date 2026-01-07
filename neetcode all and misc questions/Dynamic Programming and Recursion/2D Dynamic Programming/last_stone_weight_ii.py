class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        solved on 1/7/2026
        One way to solve this would be to just brute force it using backtracking,
        this would be exponential time.

        stones = [2,7,4,1,8,1]
        2 and 7 -> 5
        5 4 1 8 1
        mash 5 -> 4
        1 1 8 1
        mash 1 1
        8 1
        mash 8 1
        7

        back track to 1 1 8 1
        mash 1 8 -> 7
        7 1 1 
        and so on

        the base case would be if the len(elements) reaches one, then
        we'd just compare it to the global min and return the final answer 
        after figuring out all combinations.

        ********** Optimal *************
        https://youtu.be/gdXkkmzvR3c

        The key to optimizing the solution is realizing that it doesn't matter what order
        we smash the rocks in. It's about getting the total sum and then dividing the rocks
        into two separate piles that are closest to the value of total sum / 2

        for example, stones = [2,7,4,1,8,1]

        the total sum is 23, so the closest we can get to dividing the two piles is 
        11 and 12. we can see that if you were to pick all rocks and mash them, you'd be
        left with 1, which is exactly the answer we're looking for.

        But to actually figure out how to get closest to the midpoint (looking for one pile) 
        is where the recursion comes in. In particular, we'd use the knapsack idea 
        of either choosing the current element, or skipping it. And then getting the sum of the pile
        closest to total sum / 2

        This would be a 2-D DP problem since we need to track both the current index, and
        also the total in our pile so far.

        Time Complexity: O(N*total), where total is the pile value that's closest to totalSum/2
        Space: O(N*total)

        """
        # Brute Force exponential solution
        # self.res = float("inf")
        # def dfs(elements):
        #     # if there's only one element left, take it against the minimum
        #     if len(elements) == 1:
        #         self.res = min(elements[0], self.res)
        #         return 
        #     for i in range(1, len(elements)):
        #         diff = abs(elements[i] - elements[0])
        #         # filter both rocks from the list and continue the recursion
        #         filtered = [elements[j] for j in range(len(elements)) if j != 0 and j != i]
        #         # replace the leftmost element with the difference between the two elements we found
        #         # if the difference was not 0
        #         dfs(filtered if diff == 0 else [diff] + filtered)
   
        # dfs(stones)
        # return self.res

        stoneSum = sum(stones)
        # we want to take the ceiling here since if total sum is an odd number,
        # this is so we get as close to the target as possible, even if we go over.
        # i.e ceil(23/2) = 12, so we're looking for a pile value that's >= 12
        target = ceil(stoneSum/2)
        memo = {}
        def dfs(i, total):
            # base case, total goes over the target or equal to the target
            # base case, we've reached the end of the array
            if i >= len(stones) or total >= target:
                # subtract the value of this pile with the total to get the value of the second
                # pile
                secondPileTotal = stoneSum - total
                # then subtract the values from each pile to get the minimum amount that can be leftover
                return abs(secondPileTotal-total)
            if (i, total) in memo:
                return memo[(i,total)]
            # we want to minimize the value we get in the pile, so we take the min between
            # the two possibilities of taking or skipping    
            take = dfs(i+1, total+stones[i])
            skip = dfs(i+1, total)
            memo[(i, total)] = min(take,skip)
            return memo[(i,total)]
        return dfs(0,0)