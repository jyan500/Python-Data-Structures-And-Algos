class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Revisited on 9/12/2025 with the same solution. I had some intuition that it might be
        related to the subarray of sum equals K problem, but I got thrown off that it was in the sliding window section.
        
        Brute Force
        use nested loops to get all subarrays and check the sum of each
        Time: O(N^2), where N is the length of the array
        Space: O(1)
        """
        """
        cur = 0
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur += nums[j]
                if cur == goal:
                    count += 1
            cur = 0
        return count
        """

        """
        Prefix Sum Solution
        This is basically the same problem as subarray sum equals K
        using a hashmap, we store all the current sums, and we want to check
        if current sum - goal exists in our map. If so, this means that this number
        actually corresponds to the amount of subarrays that sum to the goal

        O(N) Time
        O(N) Space
        
        example:
        1 0 1 0 1
        goal = 2
        
        the reason you start the counter off with {0: 1} is in the case the array
        is only length 1, (i.e nums = [1], and goal = 1. If you didn't do this, it would not trigger
        the "if curSum - goal in counter" condition, so res wouldn't get incremented by one. And then 
        the for loop would end, resulting in an answer of 0 instead of 1.
        
        counter = {0: 1}
        nums = [1, 0, 1, 0, 1]
        goal = 2
        curSum = 0
        
        1st iteration
        ---------------
        curSum += nums[0] should be 1
        1 - 2 = -1, which is not in counter
        curSum[1] = 1
        {0: 1, 1: 1}
        
        2nd iteration
        ---------------
        curSum += nums[1] should be 1
        1 - 2 = -1, which is not in counter
        curSum[1] = 2
        {0: 1, 1: 2}
        
        3rd iteration
        ---------------
        curSum += nums[2] = 2
        2 - 2 = 0, which is IN counter. You can see that {0: 1, 1: 2} so far
        in the counter, so we increment res by 1.
        Also curSum[2] = 1
        {0: 1, 1:2, 2:1}
        1 0 1 0 1
        * * * 
        (note that in this case, it's subtracting the subarray of sum "0", which means the remainder is
        only the *)
        
        4th iteration
        ------------------
        curSum += nums[3] = 2
        2 - 2 = 0, which is IN counter. You can see that {0: 1, 1:2, 2:1} so far,
        so increment res by 1
        also curSum[2] += 1 is now 2
        {0:1, 1:2, 2:2}
        1 0 1 0 1
        * * * *
        (note that in this case, it's subtracting the subarray of sum "0", which means the remainder is
        only the *)
        
        5th iteration
        ------------------
        curSum += nums[4] = 3
        3 - 2 = 1, which is IN counter. You can see that {0: 1, 1:2, 2:2} so far,
        so increment res by counter[1] this time, 2 + 2 = 4
        
        note that the reason this works is that
        the subarray indicated by 3 - 2 = 1, shows that there are two subarrays that sum to 1.
        Therefore, there must also be two subarrays that sum to the goal of 2 
        
        1 0 1 0 1
        - * * * *

        1 0 1 0 1
        - - * * * 

        the - sums to 1, but the * sums to 2, so you can see that there are 2 subarrays that sum to 1 which were found earlier
        in the 1st and 2nd iterations of the for loop,
        and 2 subarrays that sum to the goal of 2
        
        """
        counter = {0:1}
        res = 0
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum - goal in counter:
                res += counter[curSum - goal]
            if curSum in counter:
                counter[curSum] += 1
            else:
                counter[curSum] = 1
            
        return res