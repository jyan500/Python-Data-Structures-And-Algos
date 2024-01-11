"""
https://leetcode.com/problems/car-fleet/
https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        """
        Important Concepts:
        -A car fleet can merge with another car fleet
        -A single car is considered a car fleet
        
        1) Creating a tuple of position, speed, and sorting by position in reverse
        so we can look at ones that are closer to the target first
        2) When looking at two cars, we can calculate the time it takes to reach the target
        by calculating the difference in position divided by speed ( target - position ) / speed
            -within our stack, we store the time taken to reach the target
        3) If the 2nd car reaches the target before the first, these cars will become a fleet, and we need to "merge" these two vehicles by simply popping out the faster car that we just added (which is the top of the stack) 
        
        Time complexity: O(NLogN)
        Space: O(N)
        
        Example:
        
        target = 12
        position = [10, 8, 0, 5, 3] speed = [2, 4, 1, 1, 3]
        
        Gets the sorted version
        [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
        
        1st iteration
        timeToReachTarget = (12 - 10)/2 = 1
        stack = [1]
        
        2nd iteration
        timeToReachTarget = (12 - 8)/4 = 1
        
        stack = [1, 1]
        
        collision occurs, removes top of the stack
        
        stack = [1]
        
        3rd iteration
        timeToReachTarget = (12 - 5)/1=7
        
        stack = [1, 7]
        
        4th iteration
        timeToReachTarget = (12 - 3)/3 = 3
        stack = [1, 7, 3]
        
        
        collision occurs, removes top of stack
        stack = [1, 7]
        
        5th iteration
        timeToReachTarget = (12 - 0)/1 = 12
        stack = [1, 7, 12]
        
        returns 3
        
        """
        stack = []
        pairs = [[p,s] for p, s in zip(position, speed)]
        sortedPairs = sorted(pairs, key=lambda x: x[0], reverse= True)
        for p, s in sortedPairs:
            timeToReachTarget = (target - p) / s
            stack.append(timeToReachTarget)
            # if the car we just added surpasses the previous car (stack[-2]), merge into car fleet
            # by popping out the faster car we just added
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()           
        return len(stack)
            