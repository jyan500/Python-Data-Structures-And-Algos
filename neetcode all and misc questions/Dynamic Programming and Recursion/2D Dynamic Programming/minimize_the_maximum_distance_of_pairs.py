class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        https://neetcode.io/solutions/minimize-the-maximum-difference-of-pairs
        so you want to always compare the smallest possible elements, and then subtract them,
        and find the max value of the differences between each of these pairs

        example 1:
        10 1 2 7 1 3, p = 2
        you can see that the smallest differences you can get are 1 - 1 = 0, and 3 - 2 = 1,
        note that you can't do 2 and 1, because one of those "1"s have already been chosen,
        they have to be a pair of elements that haven't already been chosen according to the problem.

        4 2 1 2, p = 1

        Brute Force:
        sort?
        1 1 2 3 7 10
        iterate in pairs based on the value of p, find the absolute value difference
        once you've found the smallest pair, pop out the elements at these indices so they can't be re-chosen
        take the max between these absolute value differences

        the issue with this algorithm is that it doesn't work for cases like this
        1 1 0 3

        where when you sort it, you get 0 1 1 3
        it always tries to find the smallest possible difference first, which results in an incorrect answer
        for example, the algorithm picks 1 1 first
        then the only elements left are 0 3, which results in a max difference of 3.
        but in reality, the actual optimal answer is 0 1, and 1 3, which results in a max difference of 2
        
        Note that this solution makes sense, but gets memory limit exceeded!
        ------------------------------------------------------------------------
        so recursion/dynamic programming seems like the better approach

        Approach for 2-D Top Down Dynamic Programming:
        1) Sort the array first, this is because it's faster to find a solution when we're comparing elements
        that are smaller in distance
        2) Recursive function that takes in index, and the amount of pairs found

        Base Case:
        ----------
        Note there are two base cases where you've made enough pairs, or you're at the end of the array and
        cannot make any more pairs

        in the example: [1 1 0 3], [0 1 1 3] (when sorted), p = 2
        it makes sense that if you pick [0 1] and [1 3], there are no pairs that can be chosen,
        because you can only pick [1 1], and inf or [1 3] and inf as the remaining

        if pairs == p,
            that means we've found enough pairs to make a comparison, return 0 (technically you just return
            the smallest element that will result in MAX(element, placeholder) = element), but 0 works here
            because it meets the edge case where p = 0, return 0)
        if i >= N - 1:
            return float("inf"), this is because we can't compare an element that's out of bounds, this also means
            we cannot make any more pairs.
            What usually ends up happening is that you will the compare the MAX(previous pair, float("inf")) and return float("inf"
            )
        Recurrence relation (knapsack, with a variation):
        -------------------------------------------------
        a) you can choose the current pair at index i and index i + 1
        and then, you would need to skip to i + 2, since you can't choose the element at i + 1
        as the next pair (similar concept to house robber problem)

        b) or, you can skip, so you skip to i + 1 instead.

        Now because we want to find the min(max(difference)), we first take the max between
        the current pair we calculate in this recursive call AND the result of the next recursive call at i + 2
        Since we are choosing a pair, we increment pairs + 1
        
        choose = Max(nums[i+1]-nums[i], search(i+2, pairs+1))

        Then for skip, we don't increment pairs since we're not including the pair i, i + 1
        skip = search(i+1, pairs)

        So we want to take the minimum between these two results:
        min(choose, skip)

        we can use memoization to store the min max difference at this particular (i, pairs)

        Time: O(N*P)
        Space: O(N*P)

        Example execution:
        nums = [1 1 0 3] p = 2

        sorted = [0 1 1 3]

        1st call
        i = 0
        starts with the pair
        [0, 1], difference of 1
        Max(1, search(i+2, pairs + 1))

        2nd call
        i = 2
        pairs = 1
        starts with pair
        [1, 3], difference of 2
        Max(2, search(i+2, pairs + 1))

        3rd call
        i = 4
        pairs = 2
        
        Base Case: pairs == p
        return 0

        Backtracks to 2nd call
        i = 2
        pairs = 1
        Max(2, 0) = 2
        Skip = search(i+1, pairs)

        4th call
        i = 3
        pairs = 1
        Base Case reached, i >= N - 1
        return float("inf")

        back to 2nd call
        i = 2 
        pairs = 1
        skip = float("inf")
        Min(float("inf"), 2) = 2
        return 2

        back to 1st call
        i = 0
        starts with the pair
        [0, 1], difference of 1
        search(i+2, pairs + 1) evaluates to 2
        Max(1, 2) = 2

        skip(i+1, pairs)

        5th call
        i = 1
        pairs = 0
        picks nums[i+1] and nums[i], which is [1,1], difference of 0
        Max(0, search(i+2, pairs + 1))

        6th call
        i = 3
        pairs = 1
        i <= N - 1, return float("inf")

        backtracks to 5th call
        i = 1
        pairs = 0
        search(i+2, pairs + 1) evaluates to float("inf")
        max(0, float("inf")) = 0

        skip(i+1, pairs)

        7th call
        i = 2
        pairs = 0
        picks nums[i+1] and nums[i], for [3, 1], difference of 2
        max(2, search(i+2, pairs+1))

        8th call
        i = 4
        pairs = 1
        base case reached, i >= N - 1
        returns float("inf")

        backtracks to 7th call
        i = 2
        pairs = 0
        search(i+2, pairs+1) evaluates to float("inf")
        choose = max(2, float("inf")) = float("inf")

        skip(i+1, pairs) => will go ahead and skip this one, as it also returns float("inf"), backtracking
        to this call...

        min(float("inf"), float("inf")) = float("inf")
        returns float("inf")

        backtracks to 5th call:
        i = 1
        pairs = 0
        search(i+2, pairs + 1) evaluates to float("inf")
        max(0, float("inf")) = float("inf")
        skip(i+1, pairs) evalutes to float("inf")

        min(float("inf"), float("inf")) evalutes to float("inf")
        returns float("inf")

        Backtracks to 1st call:
        i = 0
        Max(1, 2) = 2
        skip(i+1, pairs) now evaluates to float("inf")
        min(2, float("inf")) returns 2

        Answer = 2
        """
        n = len(nums)
        nums.sort()
        dp = {}

        def dfs(i, pairs):
            if pairs == p:
                return 0
            if i >= n - 1:
                return float('inf')
            if (i, pairs) in dp:
                return dp[(i, pairs)]

            take = max(nums[i + 1] - nums[i], dfs(i + 2, pairs + 1))
            skip = dfs(i + 1, pairs)
            dp[(i, pairs)] = min(take, skip)
            return dp[(i, pairs)]

        return dfs(0, 0) 

        """
        The optimal binary search solution is here, I've pasted it just for acceptance sakes on leetcode,
        but I prefer the DP solution more even though it doesn't pass on LC
        Time: O(NLogN) + O(NLogN)
        """
        """
        if p == 0:
            return 0
        
        def isValid(threshold):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False
        
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        res = nums[-1] - nums[0]
        
        while l <= r:
            m = l + (r - l) // 2
            if isValid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
                
        return res
        """