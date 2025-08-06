class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        https://leetcode.com/problems/grumpy-bookstore-owner/description/?source=submission-ac
        8/5/2025
        1) Add up all the satisfied customers (where grumpy[i] == 0) first
        2) Apply a sliding window of length 0 to minutes - 1 initially in the first window 0 ... minutes to 
        see the initial gain
        3) Whenever we're inside the sliding window, we treat this as the window where 
        the owner is using the "secret" technique and is not grumpy. We add the
        corresponding customer value when grumpy[index] == 1 to the initial gain. If the left pointer falls out
        of the window, subtract from the initial gain.

        Time complexity:
        O(N) 
        O(1)
        """
        # Non optimal solution, pick a range from i to i + minutes,
        # and then sum all the satisfied customers around it
        # maxRange = 0
        # for i in range(len(customers)):
        #     sumRange = sum(customers[i:i+minutes])
        #     for k in range(0, i):
        #         if grumpy[k] == 0:
        #             sumRange += customers[k]
        #     for j in range(i+minutes, len(customers)):
        #         if grumpy[j] == 0:
        #             sumRange += customers[j]
        #     maxRange = max(sumRange, maxRange)
        # return maxRange
        
        # if we knew the sum of satisfied customers outside of our immediate range,
        # we wouldn't need to repeat the calculations every step
        totalSatisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                totalSatisfied += customers[i]
        l = 0
        r = minutes

        initSumRange = 0
        # now we examine windows of length minutes, and we sum
        # up any corresponding customer values where grumpy[i] == 1,
        # since inside this window, we treat it as if the "secret" technique
        # is being used to remain non-grumpy, so we can count any values of grumpy[i] == 1
        for k in range(0, minutes):
            if grumpy[k] == 1:
                initSumRange += customers[k]

        maxGain = initSumRange

        # slide the window so we maintain the minutes interval
        # if the left most pointer falls out of the window and the owner is grumpy,
        # remove that value from the running total
        # otherwise, we add the next value where the owner is grumpy (since we're treating it
        # as if they weren't grumpy since they're using the technique)
        while (r < len(customers)):
            if grumpy[l] == 1:
                initSumRange -= customers[l]
            elif grumpy[r] == 1:
                initSumRange += customers[r]
            maxGain = max(maxGain, initSumRange)
            l += 1
            r += 1    
        # in the end, we should've found the window where the max gain from using the technique to remain non-grumpy
        return maxGain + totalSatisfied