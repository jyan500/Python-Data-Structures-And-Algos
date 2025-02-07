"""
https://leetcode.com/problems/car-fleet/
https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Revisited on 2/7/2025
        Brainstorming:
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]

        the car at position 10 will reach the target in 1 hrs (10 + 1(2))
        the car at position 8 will reach the target in 1 hr (8 + 1(4))
        the car at position 0 will reach the target in 11 hours (1 + 11(1))
        the car at position 5 will reach the target in 7 hours (5 + 7(1)))
        the car at position 3 will reach the target in 3 hours (3 + 3(3))

        Note that we don't need to know the exact point at which two cars intersect,
        just that they will intersect or not
        For example, the car at position 10 and position 8 intersect because
        they both reach the target at the same time
        The car at position 3 intersects with position 5 because it takes 
        7 hours to get to the target, and only 3 hours for the car at position 3,
        so they will intersect at some point, and become a fleet. At this point,
        you'd set the stack element to be the slower of the two cars, and 
        assume that the position would be the position of the car that was further ahead.

        Approach:
        1) Create an array of tuples like so (position ,speed), and then sort by
        position in descending order
        2) Create a stack that represents the car fleets, add tuple at index 0
        to the stack
        3) iterate through arr starting at index 1
            calculate time it takes for top of stack to reach target
            calculate time it takes for arr[i] to reach target
            if arr[i] time <= top of stack:
                stack[-1] = (position of car that has greater position, speed of slower car)
        4) return length of stack

        This question is more of an intervals style question of constantly
        updating the top of the stack, rather than having to use an inner while loop to 
        pop out the stack until a condition is reached.

        Time: O(NLogN)
        Space: O(N)

        """
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x: x[0], reverse=True)
        stack = [cars[0]]
        for i in range(1, len(cars)):
            curPosition, curSpeed = cars[i]
            prevPosition, prevSpeed = stack[-1]
            curTimeToTarget = (target - curPosition)/curSpeed
            prevTimeToTarget = (target - prevPosition)/prevSpeed
            # the current car will intersect with the previous,
            # so we need to merge them, taking the prevPosition (since we sorted
            # and that position is further ahead) 
            if curTimeToTarget <= prevTimeToTarget:
                stack[-1] = (prevPosition, min(curSpeed, prevSpeed))
            else:
                stack.append(cars[i])
        return len(stack)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        how long does it take for each to reach the destination?

        0                  10
            4     6    8
        (target - position)/speed = time
        I'd first put the position and speed together, and then sort it in reverse order,
        so you know which car is likely to reach the target first

        9/26/2024 I managed to successfully solve this problem, I recalled some aspects
        of the neetcode solution such as determining intersection by calculating the time needed to reach the target, 
        but I think this solution seems to make more sense to me.
        This seems similar to a "merge intervals" style problem where you merge together the cars 
        based on the time it takes to reach the target.
        Time: O(NLogN)
        Space: O(N)
        """
        # sort by position, and then speed, so that we can see which car is closest to the target
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append((position[i], speed[i]))
        posSpeed.sort(key=lambda x: (x[0], x[1]), reverse=True)
        # keep a stack which shows the vehicle that's closest to the target
        res = [posSpeed[0]]
        for i in range(1, len(posSpeed)):
            # get the car that's in front of the current car
            prevPos, prevSpeed = res[-1]
            pos, speed = posSpeed[i]
            prevTimeToTarget = (target - prevPos)/prevSpeed
            timeToTarget = (target - pos)/speed
            # if it takes the current car less time to reach the target then the previous,
            # that means they will intersect, so we merge the previous with the current
            # inheriting the slower car's speed since the cars cannot pass each other
            if (timeToTarget <= prevTimeToTarget):
                res[-1] = (prevPos, prevSpeed)
            else:
                # otherwise, just append the current car as the previous and current will not intersect
                res.append((pos, speed))
        return len(res)
                
             
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
            