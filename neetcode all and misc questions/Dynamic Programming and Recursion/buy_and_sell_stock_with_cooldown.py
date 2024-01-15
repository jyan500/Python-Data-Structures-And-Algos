"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
https://www.youtube.com/watch?v=I7j0F7AHpb8&ab_channel=NeetCode
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.memo = dict()
        def traverse(i, canBuy):
            """
            Approach: 
            If you did not sell yet (meaning you're looking to buy)
            1) Can buy
            3) Can Cooldown

            If you did buy:
            1) Can sell
            2) Can Cooldown
                 
            At each point, you want to keep track of the total profit and either
            1) Subtract price[i] off the recursive result if you bought at i 
            2) Add price[i] to the recursive result if you sold at i
        
            base case:
            i is at the end of the list, return a profit of 0

            The base algorithm is O(2^n), but in order to optimize it, we need to 
           	use a dictionary to keep track of results we've already calculated, specifically
           	within each configuration of the index, as well as our decision of whether we bought/sold at this index 

			{
				(i, canBuy): profit at i 
			}

			With memoization, this turns it into O(N) time (but using O(N) space)

			Tips:	
			1) Draw out a decision tree in a similar way to the neetcode video when approaching these recursive problems
			2) Think about at each step, what we need to store as the key, value pair in the memoization table. In this case,
			it's both the index AND whether we can buy since in the decision tree, this can lead to two different profit outcomes, we 
			need to distinguish between them to avoid overwriting an answer in our memoization table.
			
            """
            # if we already know the max profit we can achieve at this index,
            # and also at the same configuration where we either bought or sold at this index,
            # just recall that result
            if (i, canBuy) in self.memo:
                return self.memo[(i, canBuy)]
            if i >= len(prices):
                return 0
            if canBuy:
                # if we buy on this day, it means we need to subtract prices[i] off of our total profit,
                # since we're using our profit to buy a stock
                buy = traverse(i+1, not canBuy) - prices[i]
                cooldown = traverse(i+1, canBuy)
                self.memo[(i, canBuy)] = max(buy, cooldown)
                return self.memo[(i, canBuy)]
            else:
                # if we sell, we can add prices[i] to our profit
                # it also means we must do i+2 instead of i+1 since we need to
                # take a cooldown day
                sell = traverse(i+2, not canBuy) + prices[i]
                cooldown = traverse(i+1, canBuy)
                self.memo[(i, canBuy)] = max(sell, cooldown)
                return self.memo[(i, canBuy)]
        return traverse(0, True)