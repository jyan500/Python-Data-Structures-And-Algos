"""
https://leetcode.com/problems/koko-eating-bananas/
"""
class Solution:

    def minEatingSpeedOptimized(self, piles: List[int], h: int) -> int:
        import math
        """
        Thinking about optimizations ...
        1) Binary Search? 
        - Our search space is sorted (1 ... max amount of bananas in order)
        - If we know that a given rate is not enough to eat all bananas, 
        there's no point in checking any numbers less than this amount. So we can search
        the right half.

        1) Binary searching from 1 ... max(piles)
            - check to see if our rate is valid, where mid is our current rate, can we consume all the bananas
            before time runs out?
            - if so, check the left half to see if we can find a smaller rate
            - if not valid, we need a greater number, so check the right half to find a greater rate

        This solution passes,
        Time complexity: O(length of piles array * Log(maxPiles))
        Space Complexity: O(1)
        """
        def isRateValid(rate, piles):
            timeLeft = h
            # if we didn't finish this loop, and timeLeft has run out
            # this cannot be a valid answer
            for j in range(len(piles)):
                remaining = piles[j]  
                # time taken is essentially a ceiling division
                # how many whole number of times does rate go into remaining?
                # i.e 7 bananas, rate = 3
                # it would take 3 turns to eat all 7 bananas, which is ceiling(remaining/rate)
                timeTaken = math.ceil(remaining/rate)
                timeLeft -= timeTaken
                
                if timeLeft < 0:
                    return False          
            # if we finish this loop, this is a valid rate
            return True

        def helper(left, right, piles):
            mid = left + (right - left) // 2
            # if our rate is valid, check to see if we can find a smaller number by 
            # searching the left half
            # if our search has complete, that means we should've found the min amount where
            # the rate is still valid
            if left >= right:
                return mid
            if isRateValid(mid, piles):
                return helper(left, mid, piles)
            # if our rate is not valid, we need a greater amount, so search the right half
            else:
                return helper(mid+1, right, piles)

        return helper(1, max(piles), piles)





    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """ 
        O(N^M) solution below, TLE's
        Concept:
        1) Loop from 1 to the max amount of bananas in all the piles, this will be the banana
        consumption rate/hour
        2) loop through the piles, checking to see the amount of time taken to consume the pile,
        which is math.ceil(pile amount / our rate)
        3) if we run out of time before our inner loop finishes, this cannot be a valid answer,
        so we need to break out and try a different rate
        4) If we do manage to finish all bananas with timeLeft >= 0, that should be an answer.
        """
        import math
        k = min(piles)
        res = max(piles)
        for rate in range(1, max(piles)):
            timeLeft = h
            # if we didn't finish this loop, and timeLeft has run out
            # this cannot be a valid answer
            ranOutOfTime = False
            for j in range(len(piles)):
                remaining = piles[j]  
                # time taken is essentially a ceiling division
                # how many whole number of times does rate go into remaining?
                # i.e 7 bananas, rate = 3
                # it would take 3 turns to eat all 7 bananas, which is ceiling(remaining/rate)
                timeTaken = math.ceil(remaining/rate)
                timeLeft -= timeTaken
                    
                if timeLeft < 0:
                    ranOutOfTime = True
                    break            
            # if we finish this loop, and there's still time left
            # record our answer if it's smaller than res
            if not ranOutOfTime and timeLeft >= 0:
                res = min(rate, res)
                break
        return res
                