class Solution:
    """
        Revisited 10/8/2025
        Except it uses a while loop for the binary search instead of recursion, its much easier
        to understand the way the answer is saved in this solution compared to the recursive version
    """
    def maximumCandies(self, candies: List[int], k: int) -> int:
        totalCandies = sum(candies)
        if totalCandies < k:
            return 0
        l = 1
        r = totalCandies//k

        def isValid(amount):
            numPiles = 0
            # take the proposed amount, and see how many piles you can make
            # by doing integer division on the amount at candies[i] by the proposed amount
            # for example, if the proposed amount of candies is 4, and candies = [5, 8, 6], with k = 3
            # 4 goes into 5 one time evenly, so one pile is made
            # 4 goes into 8 2 times evenly, so two piles are made
            # 4 goes into 6 1 time evenly, so one piles is made
            # the total piles here is 4, which is >= 3, so this would be a valid answer, but
            # we could move our indices in binary search to check the right side for a potentially
            # bigger answer.
            for i in range(len(candies)):
                numPiles += (candies[i]//amount)
            return numPiles >= k
        res = 0
        while l <= r:
            mid = l + (r-l)//2
            if isValid(mid):
                # we want to save the previous answer that we found, so that in case
                # we go to the next amount and its no longer valid, this will be our answer
                res = mid
                # set the left index to mid + 1 to search the right side
                l = mid + 1
            else:
                r = mid - 1
        return res

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        Binary Search over a range
        candies = [5 8 6] k = 3 children

        lower bound
        - you could give one candy to each child
        upper bound
        - you could give the total amount of candies divided by amount of children (sum(candies)/k)

        use binary search on this range to figure out what the optimal amount of 
        candies is that can be given to each child

        within binary search, you'll want to see if the amount of candies that we chose is valid, 
        for each candies[i], do candies[i]/amount to see how many piles we can split into. And then sum
        all the piles together. If the piles >= k, we know this is valid.

        edge case:
        check to see if the total amount of candies < k, return 0
        since there aren't enough candies to be distributed to all children

        Also, one incorrect thought process is to think that the answer is always just min(candies).
        This is incorrect because:
        [1, 100, 100] k = 3
        In this example, you can split candies[1] into two piles of 50, candies[2] into two piles of 50
        and 1 cannot be split. However, you can see that there 3 piles of 50 (out of the 4) that can be given
        to the children. So min(candies) is not the answer here. The problem states that it's okay to not use all the piles
        of candies.

        This is also one of the strange examples where you need to alter the binary search to use l ... mid - 1 and mid + 1 ... r
        and change the base case to l > r. The reasoning is that in this particular problem, our optimal answer is usually found
        by searching to the right. Therefore, we might run into a case where we hit the upper bound, and the recursion ends,
        but we would need to return the LAST valid answer, and not the upper bound. By doing
        """
        from math import floor
        totalCandies = sum(candies)
        if totalCandies < k:
            return 0
        lowerBound = 1 
        upperBound = floor(totalCandies/k)
        
        def canDistribute(amount):
            numPiles = 0
            for i in range(len(candies)):
                numPiles += floor(candies[i]/amount)
            return numPiles >= k
        
        def binarySearch(l, r):
            mid = l + (r-l)//2
            # note the it's l > r and NOT l >= r, because if we hit the upper bound, we need the 
            # the LAST valid answer, and not the upper bound
            if l > r:
                return r
            # note that if this amount of candies creates enough piles,
            # since we want the max possible, we can search right to potentially find a greater value
            if canDistribute(mid):
                return binarySearch(mid+1, r)
            else:
                # note that because of the base case change, we cannot include mid in the search space when
                # searching left, otherwise this would cause infinite recursion
                return binarySearch(l, mid-1)
        return binarySearch(lowerBound, upperBound)

        