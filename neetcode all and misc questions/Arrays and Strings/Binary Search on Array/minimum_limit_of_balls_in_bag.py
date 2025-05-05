class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        Key: Binary Search over a Range

        https://www.youtube.com/watch?v=MQlC8EoOdZ0&t=528s&ab_channel=NeetCodeIO
        A similar problem: https://www.youtube.com/watch?v=GKSSr2xkR8A&t=5s&ab_channel=NeetCodeIO
        Also similar to Koko Eating Bananas

        You need to find a number by iterating from 1 to the maximum value in nums, where for each number, the total sum of ceil(x / your_number) - 1 for all x in nums is less than or equal to max_operations.

        This solution can be converted to binary search, since we have a range
        from 1 ... max(nums)

        Explanation:
        The reasoning on why the range is 1 ... max(nums) is because 
        if we were to perform 0 operations, this would give us a penalty of max(nums), representing
        the upper bound.
        and then 1 represents the smallest demoninator, since if we had enough operations
        theoretically to split the balls into groups of 1 ball each, that would technically
        be the best answer (assuming we had enough operations)

        Whereas, as we perform more operations, we'd expect to get a smaller penalty since
        we're dividing.

        The reasoning behind ceil(x/balls)-1, is that this is the "optimal" way of distributing
        the amount of balls that we have.

        For example, if we had 11 balls and we were aiming for a penalty of 4 balls,
        we would do ceil(11/4) which is 3, subtracted by one 1, which is 2. 2 represents
        the total amount of operations it would take to get the distribution, where the max
        value of that distribution is 4

        Splitting 11 into 3 groups would take 2 operations
        11
        -> 8 3 (splits into 8 and 3)
        -> 4 4 3 (splits the 8 into 4 4)

        4 4 3
        _ _ _

        When we perform this ceil(x/balls)-1 operation in a loop, we're getting the best possible way to distribute the balls to get the penalty value we need that is <= the max amount of operations
        """
        from math import ceil
        def canDivide(maxPenaltyValue):
            operations = 0
            for i in range(len(nums)):
                operations += (ceil(nums[i]/maxPenaltyValue) - 1)
                # if we can't divide all the balls optimally to get this maxPenaltyValue
                if operations > maxOperations:
                    return False
            return True
        """
        O(Max(nums)*N) Linear Scan Solution
        """
        """
        # iterating from 1 ... maxPenaltyValue
        maxPenaltyValue = max(nums)
        for i in range(1, maxPenaltyValue + 1):
            # starting from the lower to the upper bound, as soon as canDivide
            # becomes true, we return here. since this would be the minimum possible penalty
            if canDivide(i):
                return i
        """
        """
        O(Log(Max(nums)) * N) solution using Binary Search
        """
        # iterating from 1 ... maxPenaltyValue
        maxPenaltyValue = max(nums)
        def binarySearch(l, r):
            # note that if l exceeds r, this means we get the most optimal
            # way of distributing given our max amount of operations, 
            # so we would want to pick l instead of r here, since l
            # is the lower penalty value
            if l >= r:
                return l
            mid = l + (r-l)//2
            # if we pick the midpoint and this is a valid way to distribute,
            # we can continue left to see if we can get a lower penalty value
            if canDivide(mid):
                return binarySearch(l, mid)
            # otherwise, we need to check right, which would decrease the amount of operations
            # but in turn also increase the penalty value
            else:
                return binarySearch(mid+1, r)
        return binarySearch(1, maxPenaltyValue)

        
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        First attempt 5/5/2025
        Recursive approach?

        nums = [9] maxOperations = 2
        1 8
        2 7
        3 6
        4 5
        ----- at this point, we don't need to check anymore since it's a permutation
        rather than combination, order doesn't matter
        5 4
        6 3 ... etc

        at 1, 8
        we can't split 1 into any more,
        8 splits into [4, 4]
        [1, 4, 4], we've reached the max operations at 2, so the max penalty is 4

        try 2, 7
        we can split 2 into 1, 1
        and 7 can be split, this is another recursive tree
        1 6
        2 5
        3 4
        ----
        
        O(2^N) exponential time
        Exceeds memory limit on leetcode
        """
        self.min = float("inf")
        def canSplit(split):
            for i in range(len(split)):
                if split[i] != 1:
                    return True
            return False

        def dfs(split, n):
            if n == 0 or not canSplit(split):
                # return the max number of balls in this configuration
                self.min = min(self.min, max(split))
                return
            # can we split it into two integers? anything above 1 can split into 2
            for k in range(len(split)):
                num = split[k]
                if num > 1:
                    # integer division by 2 to get the splits
                    # i.e 7, [1,6], [2,5], [3,4]
                    for i in range(num//2):
                        dfs([i+1, num-i-1] + split[:k] + split[k+1:], n-1)  
        dfs(nums, maxOperations)
        return self.min
        
