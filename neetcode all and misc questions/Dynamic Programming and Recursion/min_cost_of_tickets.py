'''
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.

https://leetcode.com/problems/minimum-cost-for-tickets/

some initial thoughts when solving: 

brute force approach?

find all different combinations that you can buy tickets and pick the combination which results in the minimum amount of money spent

choose the lowest cost pass (the 1 day pass)
2 (that will cover you for day 1)

what other options do you have now?
1. choose another one day pass
2. choose a seven day pass
3. choose a 30 day pass

recursive subproblem
'''

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.search(days, costs, 0)

    def minCostTicketsMemoize(self, days:List[int], costs:List[int]) -> int:
    	memo = dict()
    	return self.search(days, costs, 0, memo)

    ## TLE solution which is O(2^n) 
    def search(self, days, costs, day_index):
        ## if our day index has reached or surpassed the length of the days list
        ## that means that we've covered all of our travels, so just return 0 
        ## since there's no need to buy any more tickets
        if (day_index >= len(days)):
            return 0
        totals = []
        for i in range(len(costs)):
           
            ## for each ticket, we figure out how many days we can cover, and determine the next index within the days array where we would need to buy another ticket
            
            ## we want to continue to recur and pass the index that we found, which is increasing
            ## until it reaches or exceeds the end of the array
            ## at the same time, we want to add the costs[i] to represent the total cost so far 
            ## of our ticket prices
            if (i == 0):
                ## print('picked 1 day pass')
               
                day_index_1_day = self.findRemainingDaysOfTravel(1, days, day_index)
               
                totals.append(self.search(days, costs, day_index_1_day) + costs[i])
            elif (i == 1):
                ## print('picked 7 day pass')
                day_index_7_day = self.findRemainingDaysOfTravel(7, days, day_index)
                totals.append(self.search(days, costs, day_index_7_day) + costs[i])
            else:
                ## print('picked 30 day pass')
                day_index_30_day = self.findRemainingDaysOfTravel(30, days, day_index)
                totals.append(self.search(days, costs, day_index_30_day) + costs[i])
           
        ## out of the totals for each ticket type, we want to pick the minimum out of the three
        ## and return
        min_total = min(totals)
        return min_total
   	
   	## Memoized solution which is O(3N), where N is the length of days , and 3 represents the different ticket types
   	## O(N) space for the memo dict
    def searchMemoize(self, days, costs, day_index, memo):
        ## for our memoization, at a specific day (days[day_index]), we may have
        ## already calculated what the minimum cost can be at this point, so we can just return
        ## this value instead of re-calculating it
    	if (day_index in memo):
    		return memo[day_index]
    	if (day_index >= len(days)):
            return 0
        totals = []
        for i in range(len(costs)):
            if (i == 0):
                day_index_1_day = self.findRemainingDaysOfTravel(1, days, day_index)
                totals.append(self.search(days, costs, day_index_1_day) + costs[i])
            elif (i == 1):
                day_index_7_day = self.findRemainingDaysOfTravel(7, days, day_index)
                totals.append(self.search(days, costs, day_index_7_day) + costs[i])
            else:
                day_index_30_day = self.findRemainingDaysOfTravel(30, days, day_index)
                totals.append(self.search(days, costs, day_index_30_day) + costs[i])
           
        min_total = min(totals)

        ## we can store in our memo table the day_index, as well as the minimum cost
        ## so that at a specific day, we'll already know the minimum cost so we don't 
        ## need to recalculate in case we reach the same day_index within our recursion
        memo[day_index]=min_total
        return min_total

    def findRemainingDaysOfTravel(self, num_days, days, day_index):
        
        ## if we buy a 1 day pass, we'll always just cover the one day we're currently on 
        ## so just return day_index + 1
        if (num_days == 1):
            return day_index + 1
        
        ## if we buy a 7 or 30 day pass, we'll have to figure out based on the 0th index of days,
        ## how many days we have covered
        elif (num_days == 7 or num_days == 30):
            
            ## we calculate the highest day we can cover by taking our current days_index value 
            ## and adding to the num days
            days_covered = days[day_index] + num_days
            
            ## we start i at our day index since we don't need to recalculate it back from i = 0
            ## since we've already covered indices less than day_index
            i = day_index
            while (i < len(days)):
                ## if our current travel day exceeds the days_covered variable,
                ## we've found the amount of travel we can cover with our ticket
                ## so we just need to return the index representing the day at which we'd need to buy another ticket (which is i)
                if (days[i] >= days_covered):
                    break
                i+=1
            return i
