class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/greatest-sum-divisible-by-three/

        Brute Force
        sort the array in ascending order
        add all the numbers together and save the total
        using backtracking:
            loop through the array starting from the smallest number first
                subtract this number from the total and see if its divisible by 3
                if its not divisible, recur further down, where we've chosen this element and
                not we have the remaining
        
        Exponential solution, can try memoizing?
        
        According to claude, this is a 2-D DP problem, because our key has to keep track
        of two different things within a tuple.

        The first being:
        1) the current index
        2) the current remainder (which is the current sum % 3)

        we only track the current remainder (rather than the current sum) because divisibility by 3
        depends only on the remainder.

        In terms of tracking both the index and remainder, the reasoning is that if the given state (index, current sum % 3) has already been found,
        they'll produce the same maximum achievable sum that's divisible by 3.

        Also we don't need to do a pre-sort, and can just apply the knapsack theory of either:
        1) take the current value and move onto the next
        2) skip the current value and move onto the next

        when we take the value, we are taking the current remainder, adding the current value, and then taking
        that value and performing mod 3 onto it to get the new remainder.

        Key Insight: Why Remainder Works
        Full input: [3,6,5,1,8]

        Let's trace taking [5, 1, 8]:

        Start: remainder = 0
        Take 5: sum = 5, remainder = 5 % 3 = 2
        Take 1: sum = 6, remainder = (2 + 1) % 3 = 0
        Take 8: sum = 14, remainder = (0 + 8) % 3 = 2 ✗ (not divisible)

        Let's trace taking [3, 6]:

        Start: remainder = 0
        Take 3: sum = 3, remainder = 3 % 3 = 0
        Take 6: sum = 9, remainder = (0 + 6) % 3 = 0 ✓ (divisible!)

        Memoization in Action
        Notice that dp(1, 0) appears multiple times:

        When we skip element 3 from dp(0, 0)
        When we take element 3 from dp(0, 0) (since 3 % 3 = 0)

        Without memoization: We'd compute this subtree twice
        With memoization: We compute it once and reuse the result

        Time: O(N)
        Space: O(N)

        """

        """ 
        # my initial solution, exponential time
        nums.sort()
        total = sum(nums)
        N = len(nums)
        self.max = float("-inf")
        def search(i, cur):
            if cur % 3 == 0:
                self.max = max(cur, self.max)
            if i > N:
                return
            for k in range(i, N):
                search(k+1, cur-nums[k])
        search(0, total)
        return self.max
        """

        """ optimized approach """
        N = len(nums)
        memo = {}
        
        def dp(i, remainder):
            # Base case: processed all elements
            if i == N:
                return 0 if remainder == 0 else float('-inf')
            
            # Check memo
            if (i, remainder) in memo:
                return memo[(i, remainder)]
            
            # Option 1: Skip current number
            skip = dp(i + 1, remainder)
            
            # Option 2: Take current number
            take = nums[i] + dp(i + 1, (remainder + nums[i]) % 3)
            
            # Store and return best option
            memo[(i, remainder)] = max(skip, take)
            return memo[(i, remainder)]
        
        return dp(0, 0)
