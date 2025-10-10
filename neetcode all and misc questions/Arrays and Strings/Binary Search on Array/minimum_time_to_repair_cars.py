class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        Revisited on 10/10/2025, writing the solution in a while loop instead
        what is the lower bound and upper bound?
        the lower bound is 1 minute
        the upper bound is the time it takes if the lowest ranked mechanic fixed all the cars,
        which would be (i.e [4,3,2,1], ranked 4 would be the slowest, taking 4 * (10**2) = 400 minutes)

        since the mechanics can all repair cars simultaneously, we're looping through each mechanic,
        and checking how many cars they can repair in the given minutes. If the number of cars they can all
        repair >= cars, this means this is a valid number. But we could do better if we decreased the amount of minutes
        and re-checked again.

        We can take advantage of binary search here by cutting the search space in half every time, instead of looping
        from the lower to upper bound and checking how many cars each mechanic can fix in the given amount of minutes.

        Time complexity: O(M * Log(upper bound)), where M is the amount of mechanics, and upper bound is the 
        max amount of time it could take to fix all the cars
        Space: O(1)

        """
        import math
        l = 1
        r = max(ranks) * (cars ** 2)

        # check the amount of cars that each mechanic can fix during the given time frame
        # (since they can all work together at the same time)
        # if the amount of cars >= cars, its possible for them to fix all the cars in the given time frame.
        # since the equation is given as numMinutes = r * (n**2), we have to solve for N,
        # num cars = floor(sqrt(numMinutes/r)), floor is to round down, since you can't have a fraction of a car 
        def isValid(minutes):
            numCars = 0
            for i in range(len(ranks)):
                numCarsFixed = math.floor(math.sqrt(minutes/ranks[i]))
                numCars += numCarsFixed
            return numCars >= cars
        
        res = 0
        while (l <= r):
            mid = l + (r-l)//2
            # if all mechanics can fix all cars in the given time frame, search the left side
            # to potentially find a better answer
            if isValid(mid):
                # save the answer, but allow it to be overwritten in case we find a better answer
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        Binary Search on Range:

        if you have rank 4 mechanic fix all the cars, how long would that take?
        ranks = [4,3,2,1] cars = 10
        4 * 10^2 = 400 minutes
        This would be the upperbound

        in terms of lowerbounds, 1 minute would make sense since
        it's assumed that it'd take at least one minute to fix a car
        since it's at least r * n^2, and rank must be at least one

        With the lower and upper bound,
        we now have a total maximum time that we can pass in to see
        if it's possible to distribute this among all the mechanics

        for example, in the first example of a lower bound of 1 and upper bound
        of 400, if we picked a total of 200 minutes

        r * n^2 minutes, and we have 200 minutes, calculate for N?
        assuming we start with the best mechanic first, r = 1
        1 * n^2 minutes = 200 minutes
        sqrt(200 minutes/ rate of 1) would be the amount of cars that this mechanic can take

        we then apply this equation to each mechanic. Note the reason we do this is because
        every mechanic works IN PARALLEL, so we can think of N amount of cars being worked on at the same time
        during those minutes. 

        You can see with the lower and upper bound that this is a binary search problem,
        where we pick a minimum time needed to repair all cars, and see if its actually possible
        for all mechanics to repair all the cars given their rates. If its not possible,
        we would search to the right side to pick a higher upper bound. Otherwise, 
        we search left to see if we can get a smaller minimum time.

        Time complexity:
        O(RLog(upperbound)), where N is the total amount of ranks, and upperbound is the upperbound on minutes
        it'd take for the slowest mechanic to complete all cars 
        
        """
        from math import sqrt, floor
        # check to see if given a minimum amount of minutes,
        # if mechanics can fix all cars
        # the equation to find the total time for a mechanic given
        # their rank r and num cars n is r * n^2.
        # therefore if we already know the time, r * n^2 = time
        # to solve for n, it would be n = sqrt(time/r)
        # we would also take the floor since we can only fix a whole
        # number of cars and not a decimal, since if the sqrt(time/r)
        # ends up being a decimal, we have to assume they can only fully
        # complete the floor() amount
        def canFix(minTime):
            totalCars = 0
            for i in range(len(ranks)):
                totalCars += floor(sqrt(minTime/ranks[i]))
            # if the total number of cars >= cars, that means
            # all mechanics can fix the given amount of cars during
            # this time period when they are all working at the same time
            return totalCars >= cars
     
        def binarySearch(l, r):
            if l >= r:
                return l
            minimumTime = l + (r-l)//2
            if canFix(minimumTime):
                return binarySearch(l, minimumTime)
            else:
                return binarySearch(minimumTime+1, r)


        lowerBound = 1
        upperBound = max(ranks) * (cars**2)
        return binarySearch(lowerBound, upperBound)