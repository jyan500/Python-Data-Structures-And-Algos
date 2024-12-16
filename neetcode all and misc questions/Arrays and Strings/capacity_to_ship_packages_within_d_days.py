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

        