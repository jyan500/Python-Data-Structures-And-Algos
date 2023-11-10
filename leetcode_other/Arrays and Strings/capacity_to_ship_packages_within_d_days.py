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

        