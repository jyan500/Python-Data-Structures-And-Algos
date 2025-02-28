class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        keep a pointer where if the current price is less than the buying price,
        we can set the buying price to be the current price, as we can generate more profit this way.
        If the price is greater than buying price, that means we are selling at a profit,
        so we calculate max(current max, current price - buying price)
		O(N) Time O(1) Space
		Revisited 9/25/2024
        Revisited 2/28/2025
        https://neetcode.io/problems/buy-and-sell-crypto
        """
        buy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if (prices[i] < buy):
                buy = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - buy)
        return maxProfit
        
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://www.youtube.com/watch?v=mj7N8pLCJ6w&ab_channel=NickWhiteNickWhiteVerified
'''
class Solution:
	def alternateSolution(self, prices: List[int]) -> int:
		maxProf = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxProf = max(maxProf, prices[sell] - prices[buy])
            # we update the "buy" index if the selling price is less than the buying price,
            # since we should be able to make a greater profit using the selling price
            # if it's less
            else:
                buy = sell
            sell += 1
        return maxProf

	def maxProfit(self, prices: List[int]) -> int:
		## O(N) time, O(1) space
		min_val = float('inf')
        max_val = 0
        for i in range(len(prices)):
        	## update min if the current price is less than the min value 
            if (prices[i] < min_val):
                min_val = prices[i]
            else:
            	## if we're not on a min value (which means the current i value is greater than min)
            	## calculate the profit to see how much we can make on this day, 
            	## and see if its greater than the max_val so far
                max_val = max(max_val, prices[i] - min_val)
        return max_val

	def bruteForce(self, prices: List[int]) -> int:
		## brute force O(N^2) approach
	    max_so_far = 0
	    for i in range(len(prices)):
	        lowest = prices[i]
	        for j in range(i, len(prices)):
	            cur = prices[j] - prices[i]
	            if cur > max_so_far:
	                max_so_far = cur
	    return max_so_far