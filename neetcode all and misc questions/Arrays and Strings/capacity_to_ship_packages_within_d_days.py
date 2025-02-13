class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Revisited again on 2/13/2025, was able to fully conceptualize the problem
        this time without reference, but still messed up an edge case.
        I wrote the numDays function out in a way that makes more sense to me.

        weights = [1,2,3,4,5,6,7,8,9,10], days = 5
        worst case: take 10 days, shipping one package at a time, where the max capacity is 10
        you must have a minimum capacity that's >= the max element in weights
        best case: capacity = sum(weights), where you ship everything in one day

        By establishing these bounds, we now have a means of applying binary search between
        the range of min capacity and max capacity

        We also have to define function that calculates the amount of days it'll take to ship everything
        based on the capacity of the ship, so then once we figure out the amount of days based on capacity,
        we check whether its either greater or less than our target amount of days.

        If it's greater than our target, we need to increase the capacity so it'll take less days, so search
        right side. Otherwise, we search the left side to see if we can decrease the capacity in order
        to get a more optimal answer (since we want the min capacity as our answer.)

        for example:
        capacity = 11
        first day: 1 + 2 + 3 + 4 = 10, cannot add any more otherwise > 11
        second day: 5 + 6, cannot add any more otherwise > 11
        third day: 7
        fourth day: 8
        fifth day: 9
        sixth day: 10

        so if capacity was 11, it'll take 6 days


        """
        minCapacity = max(weights)
        maxCapacity = sum(weights)

        def numDays(maxCap):
            amtDays = 0
            curCapacity = 0
            for i in range(len(weights)):
                curCapacity += weights[i]
                # if we've exceeded the capacity set, 
                # reset the capacity to the current weight and
                # increment days
                if curCapacity > maxCap:
                    amtDays += 1
                    curCapacity = weights[i]
            # since there are no more weights to add, 
            # if we're still <= capacity, add this remaining day
            # for example, after adding iterating the last element in the example above,
            # we'd still have a curCapacity of 10, so we need to account for this since its <= maxCap
            if curCapacity <= maxCap:
                amtDays += 1
            return amtDays
        
        def binarySearch(l, r):

            mid = l + (r-l)//2
            # if we exhausted the current search space, return the capacity we've chosen
            if (l >= r):
                return mid
            # mid represents the capacity we will choose
            amtDays = numDays(mid)
            # if amtDays > max days allowed, need to choose a greater capacity 
            # to decrease the amtDays
            if amtDays > days:
                return binarySearch(mid+1, r)
            # otherwise, search the other side to decrease capacity and get closer to amount of days
            # with lower capacity
            else:
                return binarySearch(l, mid)
                            
        
        return binarySearch(minCapacity, maxCapacity)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Revisited on 12/16/2024 (with same solution as below)
        similar concept to koko eating bananas but different calculation concept
        binary search from max(weights) to sum(weights), which is the max amount you could ship,
        but would require the greatest capacity
        the min being the biggest individual weight of the list of weights,
        since you'd need at least that amount for that one shipment
        
        when doing binary search between those bounds, you'd get a particular capacity
        
        Given a particular capacity for shipment, calculate the amount of days it'd take to ship all the items in the weights list
        Calculate by continuously adding the weights[i] to a given amount cur, and then once cur > capacity, reset the cur back
        to the current weight, and increase the amount of days.
        
        if l >= r:
            we've exhausted our search space, so we should be at the most optimal answer. return mid
        if calculated days <= days:
            we can further optimize the answer by searching the left side to decrease capacity even further
        else:
            we need to increase the capacity so we can ship more and decrease the amount of days, thus searching the right side

        Time complexity:
        O(N*LogM), where M is the amount of days, and N is the amount of weights in the input
        
        Space: O(1), no additional space
        
        """
        
        def numDays(capacity, weights):
            # start at days = 1 because it takes at least one day 
            # to make a shipment, even if we're able to ship everything in weights list
            # based on the capacity
            days = 1
            cur = 0
            for i in range(len(weights)):
                cur += weights[i]
                if cur > capacity:
                    days += 1
                    # we reset cur to the current weight to show that
                    # we start a new "shipment" at this current weight 
                    # rather than resetting back to 0
                    cur = weights[i]
            return days
        
        def binarySearch(l, r, weights):
            mid = l + (r-l)//2
            d = numDays(mid, weights)
            # if l >= r, we've exhausted the search space
            if l >= r:
                return mid
            # if we are <= the amount of days, we might be able to optimize
            # further by decreasing the capacity
            if d <= days:
                return binarySearch(l, mid, weights)
            else:
                return binarySearch(mid+1, r, weights)
        
        return binarySearch(max(weights), sum(weights), weights)
            
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Key Concept:
        1) When we load ships, the smallest possible capacity is the item with the heaviest weight
        The largest possible capacity is the sum of all the weights
        2) We can perform an O(N) operation to figure out how many days it'll take to load up all the ships with the given capacity. 
        3) Then use, binary search to search between the smallest and largest possible capacity until we find the smallest possible capacity that still loads up all the ships in the right amount of days
        
        Time complexity:
        O(N*LogM), where M is the amount of days, and N is the amount of weights in the input
        
        Space: O(1), no additional space
        
        https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/346505/Binary-classification-Python.-Detailed-explanation-Turtle-Code
        https://www.youtube.com/watch?v=ER_oLmdc-nw&t=697s&ab_channel=NeetCodeIO
        """
            
        def getNumDays(weights, capacity):
            # initialize days = 1 rather than days = 0,
            # because at max capacity (= sum of weights), that'll take one day by default
            # notice that we only add days += 1 when the current weight >
            # capacity and not >= capacity for that reason
            days = 1
            cur = 0
            for i in range(len(weights)):
                cur += weights[i]
                if cur > capacity:
                    cur = weights[i]
                    days += 1
            return days
        
        # the left and right refer to the smallest possible capacity, and the largest possible capacity
        # for each ship
        left = max(weights)
        right = sum(weights)
        
        def binarySearch(left, right, weights, days):
            mid = left + (right-left)//2
            numDays = getNumDays(weights, mid)
            if left >= right:
                return left
            # if the number of days exceeds the target, we need to search the right half
            # to increase our capacity for each ship
            elif numDays > days:
                return binarySearch(mid + 1, right, weights, days)
            # if the number of days is less, we still search the left half to find an even
            # smaller capacity
            else:
                return binarySearch(left, mid, weights, days)
            
        return binarySearch(left, right, weights, days)

        